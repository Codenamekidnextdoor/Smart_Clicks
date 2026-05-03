import time
import pyperclip
from pynput.keyboard import Key, Controller

keyboard = Controller()


def get_selected_text():
    try:
        # store old clipboard
        previous_clipboard = pyperclip.paste()

        time.sleep(0.05)

        # trigger copy
        with keyboard.pressed(Key.cmd):
            keyboard.press('c')
            keyboard.release('c')

        # IMPORTANT: give OS time to update clipboard
        time.sleep(0.2)

        selected_text = pyperclip.paste()

        # restore clipboard safely
        pyperclip.copy(previous_clipboard)

        return selected_text.strip()

    except Exception as e:
        print(f"[TEXT CAPTURE ERROR] {e}")
        return ""