from shortcuts import HotkeyManager
import time
import tkinter as tk

def on_hotkey():
    print("Hotkey Ctrl+Shift+Z was pressed!")

if __name__ == "__main__":
    hm = HotkeyManager()
    hm.start(on_hotkey)

    print("Test running. Press Ctrl+Shift+Z in any application.")
    print("You should see messages appear here in the terminal.")
    print("Press Ctrl+C or close this window to stop.")

    # Keep the script alive – tkinter root hidden, just to process events
    root = tk.Tk()
    root.withdraw()
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Stopping test.")