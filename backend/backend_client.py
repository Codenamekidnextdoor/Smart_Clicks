import time

from popup_ui import SmartPopup, MouseTracker
from shortcuts import HotkeyManager
from text_capture import get_selected_text


# ---------------- SYSTEM INIT ----------------
popup = SmartPopup()
mouse = MouseTracker()


# ---------------- MAIN ACTION ----------------
def on_hotkey_trigger():
    print("\n🔥 HOTKEY TRIGGERED")

    text = get_selected_text()

    print(f"[DEBUG] Highlighted text: {repr(text)}")

    if not text.strip():
        text = "No text selected"

    x, y = mouse.get_position()
    print(f"[MOUSE POSITION] ({x}, {y})")

    # update UI FIRST
    popup.text_box.delete("1.0", "end")
    popup.text_box.insert("1.0", text)

    # then open popup safely
    popup.root.after(1, lambda: popup.open(x, y))


# ---------------- START SYSTEM ----------------
if __name__ == "__main__":

    print("===================================")
    print(" SMART CLICK MAIN SYSTEM STARTING")
    print("===================================\n")

    # Start hotkey listener
    hotkey = HotkeyManager("b")  # Cmd/Ctrl + Shift + B
    hotkey.start(on_hotkey_trigger)

    print("System running...")
    print("Press hotkey to trigger popup\n")

    # Run popup UI loop (IMPORTANT: must block main thread)
    popup.run()