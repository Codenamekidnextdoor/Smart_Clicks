import tkinter as tk


class SmartPopup:
    def __init__(self):
        self.root = tk.Tk()

        # 🔥 remove from taskbar + no window chrome
        self.root.overrideredirect(True)

        # 🔥 make it floating overlay
        self.root.attributes("-topmost", True)

        # 🔥 reduce focus stealing
        self.root.attributes("-alpha", 0.97)

        # 🔥 TRY macOS "utility window" style (important)
        try:
            self.root.attributes("-type", "utility")
        except:
            pass

        # position somewhere safe initially
        self.root.geometry("350x200+100+100")

        self.text_box = tk.Text(self.root, height=5)
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)

        close_btn = tk.Button(self.root, text="Close", command=self.close)
        close_btn.pack()

        self.root.withdraw()

    def open(self, text="Hello", x=300, y=300):
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", text)

        # position near cursor
        self.root.geometry(f"350x200+{x}+{y}")

        self.root.deiconify()

        # 🔥 critical: do NOT force focus
        self.root.lift()
        self.root.attributes("-topmost", True)

        # try to push focus back to previous app (best effort)
        self.root.after(10, lambda: self.root.attributes("-topmost", True))

        print("[POPUP OPENED]")

    def close(self):
        self.root.withdraw()

    def run(self):
        self.root.mainloop()