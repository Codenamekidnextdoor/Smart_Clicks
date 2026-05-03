import time

from popup_ui import SmartPopup
from shortcuts import HotkeyManager

popup = SmartPopup()


def on_hotkey():
    print("🔥 HOTKEY CALLBACK FIRED")

    popup.open("Hello from hotkey!")


if __name__ == "__main__":

    print("SMART CLICK RUNNING")

    hotkey = HotkeyManager("b")
    hotkey.start(on_hotkey)

    popup.run()