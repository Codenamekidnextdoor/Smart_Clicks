from shortcuts import HotkeyManager
from text_capture import get_selected_text
import tkinter as tk

def on_hotkey():
    text = get_selected_text()
    if text:
        print(f"Captured ({len(text)} chars): {text[:100]}...")
    else:
        print("No text selected or copy failed.")

if __name__ == "__main__":
    hm = HotkeyManager()
    hm.start(on_hotkey)

    print("=== Hotkey + Capture Test ===")
    print("1. Go to ANY application (browser, IDE, Notepad).")
    print("2. Highlight some text.")
    print("3. Press Ctrl+Shift+Z.")
    print("The captured text will appear here in the terminal.")
    print("Press Ctrl+C or close this window to stop.\n")

    root = tk.Tk()
    root.withdraw()
    root.mainloop()