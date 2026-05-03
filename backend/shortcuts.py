from pynput import keyboard
import threading
import platform

class HotkeyManager:
    def __init__(self, key="z"):
        self.key = key
        self.callback = None
        self.listener = None

        system = platform.system()

        if system == "Darwin":  # macOS
            self.hotkey = f"<cmd>+<shift>+{self.key}"
        else:  # Windows/Linux
            self.hotkey = f"<ctrl>+<shift>+{self.key}"

    def _on_activate(self):
        if self.callback:
            threading.Thread(target=self.callback, daemon=True).start()

    def start(self, callback):
        self.callback = callback

        print(f"[Hotkey Registered] {self.hotkey}")

        self.listener = keyboard.GlobalHotKeys({
            self.hotkey: self._on_activate
        })

        self.listener.start()

        # IMPORTANT: keep program alive
        self.listener.join()

    def stop(self):
        if self.listener:
            self.listener.stop()


"""# ---------------- TEST ----------------
if __name__ == "__main__":

    def test_callback():
        print("\n🔥 SMART CLICK TRIGGERED")
        print("System working...")
        time.sleep(1)
        print("Done.\n")

    manager = HotkeyManager("b")
    manager.start(test_callback)

    print("Press hotkey (Ctrl/Cmd + Shift + B)")
    print("Running...")

    while True:
        time.sleep(1)"""