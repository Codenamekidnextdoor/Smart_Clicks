import keyboard
import threading
import logging

logger = logging.getLogger(__name__)

class HotkeyManager:
    def __init__(self, hotkey: str = "ctrl+shift+z"):
        self.hotkey = hotkey
        self.callback = None
        self._running = False

    def start(self, callback):
        if self._running:
            logger.warning("Hotkey listener already running")
            return
        self.callback = callback

        def _threaded():
            threading.Thread(target=self.callback, daemon=True).start()

        keyboard.add_hotkey(self.hotkey, _threaded)
        self._running = True
        logger.info(f"Hotkey {self.hotkey} registered")

    def stop(self):
        if self._running:
            keyboard.remove_hotkey(self.hotkey)
            self._running = False
            logger.info("Hotkey unregistered")