"""
SmartClick Popup Window (CustomTkinter)
Borderless, always-on-top overlay that appears at the cursor when text is selected.
"""

import customtkinter as ctk
import queue
import logging
from threading import Thread
from typing import Callable, List, Dict

logger = logging.getLogger(__name__)

C_BG    = "#0f0f0f"
C_SURF  = "#181818"
C_SURF2 = "#222222"
C_SURF3 = "#2c2c2c"
C_BORDER= "#333333"
C_ACCENT= "#00e676"
C_BLUE  = "#40c4ff"
C_RED   = "#ff5252"
C_ORANGE= "#ffab40"
C_PURPLE= "#ce93d8"
C_TEXT  = "#ffffff"
C_TEXT2 = "#b0b0b0"
C_TEXT3 = "#5a5a5a"

ACTIONS = [
    ("\U0001f4ac  Chat",      "chat",      "#0d1f2d", C_BLUE,   "#1a2e3a"),
    ("\U0001f4dd  Summarize", "summarize", "#0d1f0d", C_ACCENT, "#1a3a1a"),
    ("\u270f\ufe0f   Rewrite",  "rewrite",   "#2d1f0d", C_ORANGE, "#3a2a0d"),
    ("\U0001f4a1  Explain",   "explain",   "#1e0d2d", C_PURPLE, "#2a1a3a"),
]


class SmartClickPopup:
    """Floating popup showing near the cursor after text is selected."""

    def __init__(self, on_action: Callable = None, root: ctk.CTk = None):
        self.on_action  = on_action
        self._root      = root
        self.window     = None
        self.selected_text  = ""
        self.cursor_pos     = (0, 0)
        self.expanded       = False
        self.update_queue   = queue.Queue()
        self._loading       = False
        self._loading_after = None
        self._drag_x = self._drag_y = 0
        self._placeholder_active = False
        self._chat_frame  = None
        self._input_box   = None
        self._send_btn    = None
        self._loading_row = None

    # ---- Public API ----------------------------------------------------------

    def show(self, text: str, x: int, y: int):
        self.selected_text = text
        self.cursor_pos    = (x, y)
        if not self._alive():
            self._create()
        elif not self.expanded:
            # Only rebuild compact view if we're not already in an active chat —
            # resetting while expanded would destroy the input box (the "lock" bug).
            self._reset()
            self._position()
        # If expanded (chat open), just update context silently without wiping the UI.
        self.window.deiconify()
        self.window.lift()
        self.window.attributes("-topmost", True)

    def hide(self):
        if self._alive():
            self.window.withdraw()

    def destroy(self):
        if self._alive():
            self.window.destroy()
        self.window = None

    def add_assistant_message(self, message: str):
        """Thread-safe delivery of AI response."""
        if self._root:
            self._root.after(0, lambda m=message: self._on_ai(m))
        else:
            self._on_ai(message)

    def load_history(self, messages: List[Dict]):
        """Populate chat with messages from the database (reopen session)."""
        if not self.expanded:
            self._build_expanded()
        for msg in messages:
            self._bubble(msg.get("role", "user"), msg.get("content", ""))

    # ---- Window lifecycle ----------------------------------------------------

    def _alive(self) -> bool:
        try:
            return self.window is not None and self.window.winfo_exists()
        except Exception:
            return False

    def _create(self):
        if self._root is not None:
            self.window = ctk.CTkToplevel(self._root)
        else:
            self._own_root = ctk.CTk()
            ctk.set_appearance_mode("dark")
            self.window = self._own_root

        self.window.title("Smart Click")
        self.window.configure(fg_color=C_BG)
        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)
        try:
            self.window.attributes("-alpha", 0.97)
        except Exception:
            pass
        self.window.bind("<Escape>", lambda e: self.hide())
        # Single container frame — we destroy/recreate only its children,
        # never the CTkToplevel's own internal widgets.
        self._container = ctk.CTkFrame(self.window, fg_color=C_BG, corner_radius=0)
        self._container.pack(fill="both", expand=True)
        self._build_compact()
        self._position()
        self._poll()

    def _reset(self):
        self.expanded = False
        self._build_compact()

    def _clear(self):
        # Only destroy our container's children — never window-level widgets,
        # which would corrupt CTkToplevel's internal canvas/frame references.
        if self._container and self._container.winfo_exists():
            for w in self._container.winfo_children():
                try:
                    w.destroy()
                except Exception:
                    pass
        self._chat_frame = self._input_box = self._send_btn = None
        self._loading_row = None

    # ---- Compact view --------------------------------------------------------

    def _build_compact(self):
        self._clear()
        self.expanded = False
        self.window.geometry("330x248")

        outer = self._outer()
        self._drag_bar(outer, "\u2736  Smart Click")

        preview = (self.selected_text[:64] + "\u2026") if len(self.selected_text) > 64 else self.selected_text
        pf = ctk.CTkFrame(outer, fg_color=C_SURF)
        pf.pack(fill="x", padx=12, pady=(6, 2))
        ctk.CTkLabel(
            pf,
            text=f'"{preview}"',
            font=ctk.CTkFont(size=10, slant="italic"),
            text_color=C_TEXT3,
            wraplength=295,
            justify="left",
            anchor="w",
        ).pack(fill="x")

        grid = ctk.CTkFrame(outer, fg_color=C_SURF)
        grid.pack(fill="both", expand=True, padx=12, pady=(4, 10))
        grid.grid_columnconfigure((0, 1), weight=1)

        for idx, (label, action, bg, fg, border) in enumerate(ACTIONS):
            r, c = divmod(idx, 2)
            ctk.CTkButton(
                grid,
                text=label,
                command=lambda a=action: self._on_btn(a),
                fg_color=bg,
                hover_color=C_SURF3,
                text_color=fg,
                font=ctk.CTkFont(size=12, weight="bold"),
                height=40,
                corner_radius=8,
                border_width=1,
                border_color=border,
                anchor="w",
            ).grid(row=r, column=c, padx=3, pady=3, sticky="ew")

    # ---- Expanded chat view --------------------------------------------------

    def _build_expanded(self):
        self._clear()
        self.expanded = True
        self.window.geometry("400x560")

        outer = self._outer()
        self._drag_bar(outer, "\u2736  Smart Click Chat", collapse=True)

        ctx = ctk.CTkFrame(outer, fg_color=C_SURF3, corner_radius=0)
        ctx.pack(fill="x")
        preview = (self.selected_text[:90] + "\u2026") if len(self.selected_text) > 90 else self.selected_text
        ctk.CTkLabel(
            ctx,
            text=f'Context: "{preview}"',
            font=ctk.CTkFont(size=10, slant="italic"),
            text_color=C_TEXT3,
            wraplength=370,
            justify="left",
            anchor="w",
        ).pack(fill="x", padx=14, pady=6)

        self._chat_frame = ctk.CTkScrollableFrame(outer, fg_color=C_BG, corner_radius=0)
        self._chat_frame.pack(fill="both", expand=True)
        self._chat_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkFrame(outer, height=1, fg_color=C_BORDER).pack(fill="x")
        ia = ctk.CTkFrame(outer, fg_color=C_SURF2, corner_radius=0)
        ia.pack(fill="x")
        row = ctk.CTkFrame(ia, fg_color=C_SURF2)
        row.pack(fill="x", padx=10, pady=8)

        self._input_box = ctk.CTkTextbox(
            row,
            height=56,
            fg_color=C_SURF3,
            text_color=C_TEXT3,
            font=ctk.CTkFont(size=12),
            corner_radius=8,
            border_width=1,
            border_color=C_BORDER,
            wrap="word",
            activate_scrollbars=False,
        )
        self._input_box.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self._input_box.insert("0.0", "Ask anything\u2026")
        self._placeholder_active = True
        # Bind to the inner tk.Text widget — CTkTextbox is a frame wrapper;
        # focus/keyboard events land on ._textbox, not the outer container.
        inner_tb = self._input_box._textbox
        inner_tb.bind("<FocusIn>",  self._ph_clear)
        inner_tb.bind("<FocusOut>", self._ph_restore)
        inner_tb.bind("<Return>",   self._on_return)

        self._send_btn = ctk.CTkButton(
            row,
            text="\u2191",
            command=self._send,
            width=48, height=56,
            fg_color="#0d2b0d", hover_color="#1a4a1a",
            text_color=C_ACCENT,
            font=ctk.CTkFont(size=22, weight="bold"),
            corner_radius=8,
        )
        self._send_btn.pack(side="right")
        self._position()

    # ---- Shared widget helpers -----------------------------------------------

    def _outer(self) -> ctk.CTkFrame:
        f = ctk.CTkFrame(self._container, fg_color=C_SURF, corner_radius=12,
                         border_width=1, border_color=C_BORDER)
        f.pack(fill="both", expand=True, padx=1, pady=1)
        return f

    def _drag_bar(self, parent, title: str, collapse: bool = False):
        bar = ctk.CTkFrame(parent, fg_color=C_SURF2, corner_radius=0, height=34)
        bar.pack(fill="x")
        bar.pack_propagate(False)
        inner = ctk.CTkFrame(bar, fg_color=C_SURF2)
        inner.pack(fill="both", expand=True, padx=8)

        ctk.CTkLabel(inner, text=title, font=ctk.CTkFont(size=11, weight="bold"),
                     text_color=C_ACCENT).pack(side="left", pady=6)
        bx = ctk.CTkFrame(inner, fg_color=C_SURF2)
        bx.pack(side="right", pady=5)
        if collapse:
            ctk.CTkButton(bx, text="\u2212", command=self._collapse,
                          width=24, height=24, fg_color=C_SURF2, hover_color=C_SURF3,
                          text_color=C_TEXT2, font=ctk.CTkFont(size=14),
                          corner_radius=4).pack(side="left", padx=2)
        ctk.CTkButton(bx, text="\u2715", command=self.hide,
                      width=24, height=24, fg_color=C_SURF2, hover_color="#3a1515",
                      text_color=C_TEXT3, font=ctk.CTkFont(size=11),
                      corner_radius=4).pack(side="left", padx=2)

        for w in [bar, inner]:
            w.bind("<ButtonPress-1>", self._ds)
            w.bind("<B1-Motion>",     self._dm)

    # ---- Chat bubbles --------------------------------------------------------

    def _bubble(self, role: str, text: str):
        if not self._chat_frame or not self._chat_frame.winfo_exists():
            return
        if role == "context":
            ctk.CTkLabel(self._chat_frame, text=text,
                         font=ctk.CTkFont(size=10, slant="italic"),
                         text_color=C_TEXT3, wraplength=350,
                         justify="left", anchor="w"
                         ).pack(fill="x", padx=14, pady=(8, 4))
            self._scroll_bot()
            return

        is_user = (role == "user")
        row = ctk.CTkFrame(self._chat_frame, fg_color=C_BG)
        row.pack(fill="x", padx=8, pady=3)
        bcol  = "#0d1f2d" if is_user else C_SURF2
        bbord = "#1a2e3a" if is_user else C_BORDER
        side  = "right" if is_user else "left"
        pad   = (60, 4) if is_user else (4, 60)

        bub = ctk.CTkFrame(row, fg_color=bcol, corner_radius=10,
                           border_width=1, border_color=bbord)
        bub.pack(side=side, padx=pad)
        ctk.CTkLabel(bub, text="You" if is_user else "Bob \u2736",
                     font=ctk.CTkFont(size=9, weight="bold"),
                     text_color=C_BLUE if is_user else C_ACCENT,
                     anchor="w").pack(anchor="w", padx=10, pady=(7, 1))
        ctk.CTkLabel(bub, text=text, font=ctk.CTkFont(size=11),
                     text_color=C_TEXT, wraplength=250,
                     justify="left", anchor="w").pack(anchor="w", padx=10, pady=(1, 8))
        self._scroll_bot()

    def _scroll_bot(self):
        try:
            self._chat_frame.after(
                60, lambda: self._chat_frame._parent_canvas.yview_moveto(1.0))
        except Exception:
            pass

    # ---- Loading indicator ---------------------------------------------------

    def _show_loading(self):
        if not self._chat_frame or not self._chat_frame.winfo_exists():
            return
        self._loading = True
        self._loading_row = ctk.CTkFrame(self._chat_frame, fg_color=C_BG)
        self._loading_row.pack(fill="x", padx=8, pady=3)
        bub = ctk.CTkFrame(self._loading_row, fg_color=C_SURF2, corner_radius=10,
                           border_width=1, border_color=C_BORDER)
        bub.pack(side="left", padx=(4, 60))
        self._loading_lbl = ctk.CTkLabel(bub, text="Bob is thinking \u25cf",
                                          font=ctk.CTkFont(size=11, slant="italic"),
                                          text_color=C_TEXT3)
        self._loading_lbl.pack(padx=14, pady=10)
        if self._send_btn and self._send_btn.winfo_exists():
            self._send_btn.configure(state="disabled", text="\u2026")
        self._anim(0)

    def _anim(self, step: int):
        if not self._loading:
            return
        dots = ["\u25cf", "\u25cf \u25cf", "\u25cf \u25cf \u25cf", "\u25cf \u25cf"]
        if hasattr(self, "_loading_lbl") and self._loading_lbl.winfo_exists():
            self._loading_lbl.configure(text=f"Bob is thinking  {dots[step % 4]}")
            self._loading_after = self._loading_lbl.after(
                380, lambda: self._anim(step + 1))

    def _hide_loading(self):
        self._loading = False
        if self._loading_after:
            try:
                self.window.after_cancel(self._loading_after)
            except Exception:
                pass
            self._loading_after = None
        if self._loading_row:
            try:
                self._loading_row.destroy()
            except Exception:
                pass
            self._loading_row = None
        if self._send_btn and self._send_btn.winfo_exists():
            self._send_btn.configure(state="normal", text="\u2191")

    # ---- AI response ---------------------------------------------------------

    def _on_ai(self, message: str):
        self._hide_loading()
        if not self.expanded:
            self._build_expanded()
        self._bubble("assistant", message)

    # ---- Action handlers -----------------------------------------------------

    def _on_btn(self, action: str):
        if action == "chat":
            self._build_expanded()
            return
        self._build_expanded()
        self._bubble("user", f"{action.capitalize()} this text")
        self._show_loading()
        if self.on_action:
            Thread(target=self.on_action, args=(action, self.selected_text), daemon=True).start()

    def _send(self):
        if not self._input_box or not self._input_box.winfo_exists():
            return
        text = self._input_box.get("0.0", "end").strip()
        placeholder = "Ask anything\u2026"
        # Guard only on actual content — never on the flag alone, which can
        # fall out of sync when FocusIn doesn't fire on the outer wrapper.
        if not text or text == placeholder:
            return
        self._placeholder_active = False  # sync flag with reality
        self._input_box.delete("0.0", "end")
        self._ph_restore(None)
        self._bubble("user", text)
        self._show_loading()
        if self.on_action:
            Thread(target=self.on_action, args=("chat", text), daemon=True).start()

    def _collapse(self):
        self.expanded = False
        self._build_compact()
        self._position()

    # ---- Input placeholder ---------------------------------------------------

    def _on_return(self, event):
        if event.state & 0x1:
            return
        self._send()
        return "break"

    def _ph_clear(self, event):
        if self._placeholder_active and self._input_box:
            self._input_box.delete("0.0", "end")
            self._input_box.configure(text_color=C_TEXT)
            self._placeholder_active = False

    def _ph_restore(self, event):
        if not self._input_box:
            return
        if not self._input_box.get("0.0", "end").strip():
            self._input_box.delete("0.0", "end")
            self._input_box.insert("0.0", "Ask anything\u2026")
            self._input_box.configure(text_color=C_TEXT3)
            self._placeholder_active = True

    # ---- Window drag ---------------------------------------------------------

    def _ds(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def _dm(self, event):
        if not self._alive():
            return
        nx = self.window.winfo_x() + event.x - self._drag_x
        ny = self.window.winfo_y() + event.y - self._drag_y
        self.window.geometry(f"+{nx}+{ny}")

    # ---- Screen positioning --------------------------------------------------

    def _position(self):
        if not self._alive():
            return
        x, y = self.cursor_pos
        self.window.update_idletasks()
        w  = self.window.winfo_width()
        h  = self.window.winfo_height()
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = max(10, min(x, sw - w - 10))
        y = max(10, min(y, sh - h - 10))
        self.window.geometry(f"+{x}+{y}")

    # ---- Queue poll (thread-safe fallback) -----------------------------------

    def _poll(self):
        try:
            while True:
                kind, data = self.update_queue.get_nowait()
                if kind == "message":
                    self._on_ai(data)
        except queue.Empty:
            pass
        if self._alive():
            self.window.after(100, self._poll)
