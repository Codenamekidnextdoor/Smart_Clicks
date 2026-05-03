import time

from popup_ui import SmartPopup, MouseTracker
from shortcuts import HotkeyManager
from text_capture import get_selected_text

popup = SmartPopup()
mouse = MouseTracker()


def on_hotkey_trigger():
    print("\n🔥 HOTKEY TRIGGERED")

    text = get_selected_text()
    print(f"[DEBUG] Highlighted text: {repr(text)}")

    if not text.strip():
        text = "No text selected"

    x, y = mouse.get_position()

    def update_ui():
        popup.text_box.delete("1.0", "end")
        popup.text_box.insert("1.0", text)
        popup.open(x, y)

    popup.root.after(0, update_ui)


if __name__ == "__main__":

    print("===================================")
    print(" SMART CLICK SYSTEM STARTING")
    print("===================================\n")

    # 1. START HOTKEYS FIRST (but NO triggers yet)
    hotkey = HotkeyManager("b")
    hotkey.start(on_hotkey_trigger)

    # 2. START UI MAIN LOOP LAST (CRITICAL)
    print("UI starting...")
    popup.run()