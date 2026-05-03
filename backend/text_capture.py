import sys
import time
import pyperclip
from pynput.keyboard import Key, Controller

keyboard = Controller()

# macOS uses Cmd+C; Windows and Linux use Ctrl+C
_IS_MAC = sys.platform == 'darwin'
_MODIFIER = Key.cmd if _IS_MAC else Key.ctrl


def get_selected_text():
    try:
        # Store old clipboard
        previous_clipboard = pyperclip.paste()

        time.sleep(0.05)

        # Simulate copy shortcut (Cmd+C on macOS, Ctrl+C elsewhere)
        with keyboard.pressed(_MODIFIER):
            keyboard.press('c')
            keyboard.release('c')

        # Give the OS time to update clipboard
        time.sleep(0.2)

        selected_text = pyperclip.paste()

        # Restore previous clipboard content
        pyperclip.copy(previous_clipboard)

        return selected_text.strip()

    except Exception as e:
        print(f"[TEXT CAPTURE ERROR] {e}")
        return ""
