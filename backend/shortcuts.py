from pynput import keyboard
import threading


class HotkeyManager:
    def __init__(self, key="b"):
        self.key = key
        self.callback = None

    def start(self, callback):
        self.callback = callback

        def on_press(key):
            try:
                if key.char == self.key:
                    print("[HOTKEY TRIGGERED]")
                    if self.callback:
                        self.callback()
            except:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()