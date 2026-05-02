import keyboard
import pyautogui

def smart_click():
    x, y = pyautogui.position()
    print("🔥 Smart Click Triggered")
    print(f"Cursor position → x:{x}, y:{y}")

keyboard.add_hotkey('ctrl+shift+a', smart_click)

print("Listening for Smart Click shortcut...")
keyboard.wait()