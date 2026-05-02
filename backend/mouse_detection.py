import pyautogui
import time

def get_cursor_position():
    x, y = pyautogui.position()
    return x, y

def monitor_cursor(interval=0.1):
    print("Tracking cursor... (Ctrl+C to stop)")
    
    last_pos = None

    while True:
        x, y = get_cursor_position()

        if last_pos != (x, y):
            print(f"Cursor moved → x:{x}, y:{y}")
            last_pos = (x, y)

        time.sleep(interval)

if __name__ == "__main__":
    monitor_cursor()