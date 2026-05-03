from pynput import keyboard
import platform


class HotkeyManager:
    def __init__(self, key="b"):
        self.callback = None

        system = platform.system()

        if system == "Darwin":
            self.hotkey = f"<cmd>+<shift>+{key}"
        else:
            self.hotkey = f"<ctrl>+<shift>+{key}"

    def _trigger(self):
        print("[HOTKEY TRIGGERED]")
        if self.callback:
            self.callback()

    def start(self, callback):
        self.callback = callback

        self.listener = keyboard.GlobalHotKeys({
            self.hotkey: self._trigger
        })

        self.listener.start()

        print(f"[HOTKEY REGISTERED] {self.hotkey}")