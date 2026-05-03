"""
SmartClick - Main Control Window (CustomTkinter)
"""

import customtkinter as ctk
import logging
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

logger = logging.getLogger(__name__)

# ── Palette ────────────────────────────────────────────────────────────────────
C_BG      = "#0a0a0a"
C_SURFACE = "#141414"
C_SURF2   = "#1e1e1e"
C_SURF3   = "#282828"
C_BORDER  = "#2a2a2a"
C_ACCENT  = "#00e676"
C_BLUE    = "#40c4ff"
C_RED     = "#ff5252"
C_TEXT    = "#ffffff"
C_TEXT2   = "#9e9e9e"
C_TEXT3   = "#5a5a5a"



class SmartClickMainWindow:
    """
    Main control window.
    Left: Enable / Disable / About buttons + session history.
    Right: How-To-Setup and How-To-Use info cards.
    """

    def __init__(self, app=None):
        self.app = app
        self._enabled = False
        self._history_items = []

        self.root = ctk.CTk()
        self.root.configure(fg_color=C_BG)
        self.root.title("Smart Click")
        self.root.resizable(False, False)

        W, H = 860, 560
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self._build_ui()

    # ── Layout ─────────────────────────────────────────────────────────────────

    def _build_ui(self):
        outer = ctk.CTkFrame(self.root, fg_color=C_BG)
        outer.pack(fill="both", expand=True, padx=22, pady=16)

        # Title row
        title_row = ctk.CTkFrame(outer, fg_color=C_BG)
        title_row.pack(fill="x", pady=(0, 4))

        ctk.CTkLabel(
            title_row,
            text="✦  Smart Click",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
            text_color=C_ACCENT,
        ).pack(side="left")

        self._status_dot = ctk.CTkLabel(
            title_row,
            text="●  Disabled",
            font=ctk.CTkFont(size=12),
            text_color=C_RED,
        )
        self._status_dot.pack(side="right", padx=4)

        ctk.CTkFrame(outer, height=1, fg_color=C_BORDER).pack(fill="x", pady=(6, 14))

        # Two columns
        content = ctk.CTkFrame(outer, fg_color=C_BG)
        content.pack(fill="both", expand=True)

        left = ctk.CTkFrame(content, fg_color=C_BG, width=270)
        left.pack(side="left", fill="y", padx=(0, 16))
        left.pack_propagate(False)

        right = ctk.CTkFrame(content, fg_color=C_BG)
        right.pack(side="left", fill="both", expand=True)

        self._build_controls(left)
        self._build_history(left)
        self._build_info_panels(right)

    # ── Controls (left top) ────────────────────────────────────────────────────

    def _build_controls(self, parent):
        ctk.CTkLabel(
            parent,
            text="CONTROLS",
            font=ctk.CTkFont(size=9, weight="bold"),
            text_color=C_TEXT3,
        ).pack(anchor="w", pady=(0, 6))

        self._enable_btn = ctk.CTkButton(
            parent,
            text="  ▶   Enable",
            command=self._on_enable,
            fg_color="#152b15",
            hover_color="#1e4a1e",
            text_color=C_ACCENT,
            font=ctk.CTkFont(size=13, weight="bold"),
            height=44,
            corner_radius=8,
            border_width=1,
            border_color="#1a4a1a",
            anchor="w",
        )
        self._enable_btn.pack(fill="x", pady=(0, 6))

        self._disable_btn = ctk.CTkButton(
            parent,
            text="  ■   Disable",
            command=self._on_disable,
            fg_color="#2b1515",
            hover_color="#4a1e1e",
            text_color=C_RED,
            font=ctk.CTkFont(size=13, weight="bold"),
            height=44,
            corner_radius=8,
            border_width=1,
            border_color="#4a1a1a",
            anchor="w",
        )
        self._disable_btn.pack(fill="x", pady=(0, 6))

        ctk.CTkButton(
            parent,
            text="  ?   What is Smart Click",
            command=self._on_about,
            fg_color="#15152b",
            hover_color="#1e1e4a",
            text_color=C_BLUE,
            font=ctk.CTkFont(size=12),
            height=40,
            corner_radius=8,
            border_width=1,
            border_color="#1a2e3a",
            anchor="w",
        ).pack(fill="x", pady=(0, 12))

        ctk.CTkFrame(parent, height=1, fg_color=C_BORDER).pack(fill="x", pady=(0, 10))

    # ── Session history (left bottom) ──────────────────────────────────────────

    def _build_history(self, parent):
        hdr = ctk.CTkFrame(parent, fg_color=C_BG)
        hdr.pack(fill="x", pady=(0, 6))

        ctk.CTkLabel(
            hdr,
            text="RECENT SESSIONS",
            font=ctk.CTkFont(size=9, weight="bold"),
            text_color=C_TEXT3,
        ).pack(side="left")

        ctk.CTkButton(
            hdr,
            text="↺",
            command=self._refresh_history,
            width=26,
            height=22,
            fg_color=C_BG,
            hover_color=C_SURFACE,
            text_color=C_TEXT3,
            font=ctk.CTkFont(size=13),
            corner_radius=6,
        ).pack(side="right")

        self._history_scroll = ctk.CTkScrollableFrame(
            parent,
            fg_color=C_SURFACE,
            corner_radius=8,
        )
        self._history_scroll.pack(fill="both", expand=True)

        self._no_sessions_lbl = ctk.CTkLabel(
            self._history_scroll,
            text="No sessions yet.\nEnable and select some text!",
            font=ctk.CTkFont(size=11),
            text_color=C_TEXT3,
            justify="center",
        )
        self._no_sessions_lbl.pack(pady=20)

    # ── Info cards (right) ─────────────────────────────────────────────────────

    def _build_info_panels(self, parent):
        self._make_card(
            parent,
            "How To Setup",
            [
                "1.  Press  Enable  in  this  window",
                "2.  Allow  changes  if  prompted",
                "3.  You're  all  set!",
            ],
        )
        ctk.CTkFrame(parent, height=12, fg_color=C_BG).pack()
        self._make_card(
            parent,
            "How To Use",
            [
                "1.  Highlight  text  in  any  application",
                "2.  Press  Ctrl + Shift + Z",
                "3.  Ask  Smart  Click  anything  you  like",
            ],
        )

    def _make_card(self, parent, title, lines):
        card = ctk.CTkFrame(
            parent,
            fg_color=C_SURFACE,
            corner_radius=10,
            border_width=1,
            border_color=C_BORDER,
        )
        card.pack(fill="both", expand=True)

        inner = ctk.CTkFrame(card, fg_color=C_SURFACE)
        inner.pack(fill="both", expand=True, padx=18, pady=14)

        ctk.CTkLabel(
            inner,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=C_ACCENT,
            anchor="w",
        ).pack(fill="x")

        ctk.CTkFrame(inner, height=1, fg_color="#1a4a2a").pack(fill="x", pady=(6, 10))

        for line in lines:
            ctk.CTkLabel(
                inner,
                text=line,
                font=ctk.CTkFont(size=12, family="Consolas"),
                text_color=C_TEXT2,
                anchor="w",
            ).pack(fill="x", pady=3)

    # ── Callbacks ──────────────────────────────────────────────────────────────

    def _on_enable(self):
        if self.app:
            self.app.enable()
        self._enabled = True
        self._status_dot.configure(text="●  Active", text_color=C_ACCENT)
        self._enable_btn.configure(fg_color="#1e4a1e")
        self._disable_btn.configure(fg_color="#2b1515")
        self._refresh_history()

    def _on_disable(self):
        if self.app:
            self.app.disable()
        self._enabled = False
        self._status_dot.configure(text="●  Disabled", text_color=C_RED)
        self._enable_btn.configure(fg_color="#152b15")
        self._disable_btn.configure(fg_color="#4a1e1e")

    def _on_about(self):
        dlg = ctk.CTkToplevel(self.root)
        dlg.title("What is Smart Click?")
        dlg.configure(fg_color=C_BG)
        dlg.resizable(False, False)
        dlg.grab_set()
        dlg.lift()
        dlg.focus_force()

        dlg.update_idletasks()
        pw = self.root.winfo_x() + self.root.winfo_width() // 2
        ph = self.root.winfo_y() + self.root.winfo_height() // 2
        dlg.geometry(f"460x360+{pw - 230}+{ph - 180}")

        card = ctk.CTkFrame(
            dlg,
            fg_color=C_SURFACE,
            corner_radius=12,
            border_width=1,
            border_color=C_BORDER,
        )
        card.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            card,
            text="✦  What is Smart Click?",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color=C_ACCENT,
        ).pack(pady=(20, 4))

        ctk.CTkFrame(card, height=1, fg_color="#1a4a2a").pack(fill="x", padx=20, pady=(0, 12))

        info = (
            "Smart Click is an AI-powered cursor layer that\n"
            "watches for selected text anywhere on your screen.\n\n"
            "Highlight text, press  Ctrl + Shift + Z,  and a\n"
            "popup appears near your cursor offering:\n\n"
            "  💬  Chat           Ask anything about the text\n"
            "  📝  Summarize   Get a concise summary\n"
            "  ✏️   Rewrite        Rewrite in a different tone\n"
            "  💡  Explain         Get a clear explanation\n\n"
            "All conversations are saved automatically."
        )
        ctk.CTkLabel(
            card,
            text=info,
            font=ctk.CTkFont(size=12),
            text_color=C_TEXT2,
            justify="left",
        ).pack(padx=24, pady=(0, 16))

        ctk.CTkButton(
            card,
            text="Got it",
            command=dlg.destroy,
            fg_color="#152b15",
            hover_color="#1e4a1e",
            text_color=C_ACCENT,
            width=130,
            height=36,
            corner_radius=8,
        ).pack(pady=(0, 20))

    # ── History panel ──────────────────────────────────────────────────────────

    def _refresh_history(self):
        for item in self._history_items:
            try:
                item.destroy()
            except Exception:
                pass
        self._history_items.clear()

        if not self.app:
            return

        try:
            sessions = self.app.db.get_recent_sessions(limit=15)
        except Exception:
            return

        if not sessions:
            self._no_sessions_lbl.pack(pady=20)
            return

        self._no_sessions_lbl.pack_forget()

        for session in sessions:
            self._add_history_item(session)

    def _add_history_item(self, session):
        raw = session.get("selected_text", "")
        preview = (raw[:44] + "…") if len(raw) > 44 else raw
        msg_count = session.get("message_count", 0)
        time_str = self._time_ago(session.get("updated_at", ""))

        item = ctk.CTkFrame(
            self._history_scroll,
            fg_color=C_SURF2,
            corner_radius=6,
            cursor="hand2",
        )
        item.pack(fill="x", pady=2, padx=2)

        inner = ctk.CTkFrame(item, fg_color=C_SURF2)
        inner.pack(fill="x", padx=10, pady=6)

        ctk.CTkLabel(
            inner,
            text=f'"{preview}"',
            font=ctk.CTkFont(size=11),
            text_color=C_TEXT,
            anchor="w",
        ).pack(fill="x")

        meta = ctk.CTkFrame(inner, fg_color=C_SURF2)
        meta.pack(fill="x", pady=(2, 0))

        ctk.CTkLabel(
            meta,
            text=f"{msg_count} msg{'s' if msg_count != 1 else ''}",
            font=ctk.CTkFont(size=10),
            text_color=C_TEXT3,
            anchor="w",
        ).pack(side="left")

        ctk.CTkLabel(
            meta,
            text=time_str,
            font=ctk.CTkFont(size=10),
            text_color=C_TEXT3,
            anchor="e",
        ).pack(side="right")

        sid = session.get("id")
        sel_text = session.get("selected_text", "")
        for w in [item, inner, meta]:
            w.bind("<Button-1>", lambda e, s=sid, t=sel_text: self._reopen_session(s, t))

        self._history_items.append(item)

    def _reopen_session(self, session_id, selected_text):
        if not (self.app and self.app.popup):
            return
        try:
            import win32api
            x, y = win32api.GetCursorPos()
        except Exception:
            x, y = 400, 300

        self.app.current_session_id = session_id
        self.app.popup.show(selected_text, x + 10, y + 10)
        try:
            messages = self.app.db.get_session_messages(session_id)
            self.app.popup.load_history(messages)
        except Exception as e:
            logger.error(f"Failed to load session history: {e}")

    @staticmethod
    def _time_ago(ts):
        if not ts:
            return ""
        try:
            dt = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
            now = datetime.now(dt.tzinfo) if dt.tzinfo else datetime.now()
            s = (now - dt).total_seconds()
            if s < 60:   return "just now"
            if s < 3600: return f"{int(s // 60)}m ago"
            if s < 86400: return f"{int(s // 3600)}h ago"
            return f"{int(s // 86400)}d ago"
        except Exception:
            return ""

    # ── Lifecycle ──────────────────────────────────────────────────────────────

    def _on_close(self):
        if self.app:
            self.app.stop()
        self.root.destroy()

    def set_status(self, message: str):
        def _upd():
            if "enabled" in message.lower() or "active" in message.lower():
                self._status_dot.configure(text="●  Active", text_color=C_ACCENT)
            else:
                self._status_dot.configure(text="●  Disabled", text_color=C_RED)
        self.root.after(0, _upd)

    def get_root(self):
        return self.root

    def run(self):
        self.root.mainloop()
