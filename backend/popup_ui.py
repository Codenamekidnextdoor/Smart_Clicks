import tkinter as tk
from mouse_detection import MouseTracker


class SmartPopup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Click")

        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # Initialize as None, but will be set in _build_ui()
        self.text_box: tk.Text | None = None
        self.output: tk.Label | None = None

        self._build_ui()

        # start hidden
        self.root.withdraw()

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

    def open(self, x, y):
        x, y = int(x), int(y)

        self.root.geometry(f"350x200+{x+10}+{y+10}")

        # IMPORTANT: make it visible BEFORE anything else
        self.root.deiconify()
        self.root.lift()
        self.root.attributes("-topmost", True)

        # Ensure text_box is initialized before calling focus_set
        if self.text_box is not None:
            self.text_box.focus_set()

        print(f"[POPUP OPENED] at ({x}, {y})")

    def close(self):
        self.root.withdraw()

    def run(self):
        self.root.mainloop()
