from pynput import mouse
import threading

class MouseTracker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.listener = None

    def _on_move(self, x, y):
        self.x = x
        self.y = y

    def _on_click(self, x, y, button, pressed):
        if pressed:
            print(f"[Mouse Click] at ({x}, {y})")

    def start(self):
        def run():
            self.listener = mouse.Listener(
                on_move=self._on_move,
                on_click=self._on_click
            )
            self.listener.start()
            self.listener.join()

        thread = threading.Thread(target=run, daemon=True)
        thread.start()

    def get_position(self):
        return self.x, self.y


# Simple test run
if __name__ == "__main__":
    tracker = MouseTracker()
    tracker.start()

    import time
    while True:
        print(tracker.get_position())
        time.sleep(1)