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

        # Small settle time before simulating the key
        time.sleep(0.05)

        # Simulate copy shortcut (Cmd+C on macOS, Ctrl+C elsewhere)
        with keyboard.pressed(_MODIFIER):
            keyboard.press('c')
            keyboard.release('c')

        # macOS needs more time for the clipboard to update than Windows/Linux
        time.sleep(0.35 if _IS_MAC else 0.2)

        selected_text = pyperclip.paste()

        # Restore previous clipboard content
        pyperclip.copy(previous_clipboard)

        return selected_text.strip()

    except Exception as e:
        print(f"[TEXT CAPTURE ERROR] {e}")
        # On macOS a common cause is missing Accessibility permission
        if _IS_MAC:
            print("[TEXT CAPTURE] On macOS, grant Accessibility access:")
            print("  System Settings → Privacy & Security → Accessibility → add Terminal (or your app)")
        return ""
