import tkinter as tk


class SmartPopup:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Smart Click")
        self.root.geometry("350x200")

        self.text_box = tk.Text(self.root, height=5)
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)

        close_btn = tk.Button(self.root, text="Close", command=self.close)
        close_btn.pack()

        self.root.withdraw()  # start hidden

    def open(self, text="Hello"):
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", text)

        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

        print("[POPUP OPENED]")

    def close(self):
        self.root.withdraw()

    def run(self):
        self.root.mainloop()