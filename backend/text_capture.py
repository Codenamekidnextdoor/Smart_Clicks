import pyperclip
import pyautogui
import time
import logging

logger = logging.getLogger(__name__)

def get_selected_text():
    """
    Copy currently highlighted text from any active application.
    Returns the text, or empty string if nothing was selected.
    """
    # 1. Save existing clipboard content
    try:
        old = pyperclip.paste()
    except Exception:
        old = ""

    # 2. Clear clipboard so we can detect a new copy
    try:
        pyperclip.copy("")
        time.sleep(0.05)
    except Exception:
        pass

    # 3. Send Ctrl+C to the active window
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)   # wait for clipboard to update

    # 4. Read whatever landed in the clipboard
    selected = pyperclip.paste()

    # 5. Restore the original clipboard (polite)
    try:
        pyperclip.copy(old)
    except Exception as e:
        logger.warning(f"Could not restore clipboard: {e}")

    # 6. If the clipboard didn't change, nothing was selected
    if not selected or selected == old:
        return ""
    return selected