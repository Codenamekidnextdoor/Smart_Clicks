import tkinter as tk
from pynput import mouse


# ---------------- MOUSE TRACKER ----------------
class MouseTracker:
    def __init__(self):
        self.position = (0, 0)
        self.listener = mouse.Listener(on_move=self.on_move)
        self.listener.start()

    def on_move(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position


# ---------------- SMART POPUP ----------------
class SmartPopup:
    def __init__(self):
        self.root = tk.Tk()

        # 🔥 CRITICAL FIX: prevent macOS activation / focus steal
        self.root.withdraw()              # MUST be first
        self.root.overrideredirect(True)

        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.98)

        self.root.update_idletasks()     # stabilize window before showing

        self.text_box = None
        self.output = None

        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(fill="both", expand=True)

        self.text_box = tk.Text(
            frame,
            height=3,
            bg="#2b2b2b",
            fg="white",
            insertbackground="white"
        )
        self.text_box.pack(padx=10, pady=10, fill="x")

        self.output = tk.Label(
            frame,
            text="Ask something...",
            bg="#1e1e1e",
            fg="white",
            wraplength=320,
            justify="left"
        )
        self.output.pack(padx=10, pady=5, fill="both", expand=True)

        close_btn = tk.Button(
            frame,
            text="Close",
            command=self.close,
            bg="#ff4d4d",
            fg="white"
        )
        close_btn.pack(pady=5)

    # ---------------- PUBLIC API ----------------
    def open(self, x, y):
        x, y = int(x), int(y)

        self.root.geometry(f"350x200+{x+10}+{y+10}")

        # 🔥 CRITICAL: show WITHOUT activating app
        self.root.update_idletasks()

        self.root.deiconify()

        # force stacking only (NOT focus)
        self.root.lift()
        self.root.attributes("-topmost", True)

        # re-assert topmost without triggering focus
        self.root.after(10, lambda: self.root.attributes("-topmost", True))

        print(f"[POPUP OPENED] at ({x}, {y})")

    def close(self):
        self.root.withdraw()

    def run(self):
        self.root.mainloop()