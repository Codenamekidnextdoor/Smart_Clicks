"""
Text Selection Detector for SmartClick
Detects when a user highlights text in any Windows application
and captures the selected text along with cursor position.
"""

import win32gui
import win32con
import win32clipboard
import pyperclip
import time
import threading
from typing import Optional, Tuple, Callable
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextSelectionDetector:
    """
    Monitors system-wide text selection events on Windows.
    Uses clipboard monitoring and Windows API to detect highlighted text.
    """
    
    def __init__(self, callback: Callable[[str, Tuple[int, int]], None]):
        """
        Initialize the text selection detector.
        
        Args:
            callback: Function to call when text is selected.
                     Receives (selected_text, cursor_position) as arguments.
        """
        self.callback = callback
        self.last_clipboard_content = ""
        self.monitoring = False
        self.monitor_thread = None
        
    def start(self):
        """Start monitoring for text selection events."""
        if self.monitoring:
            logger.warning("Detector is already running")
            return
            
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Text selection detector started")
        
    def stop(self):
        """Stop monitoring for text selection events."""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        logger.info("Text selection detector stopped")
        
    def _monitor_loop(self):
        """Main monitoring loop that checks for clipboard changes."""
        # Seed with whatever is already in the clipboard so we don't fire
        # a false-positive the moment the detector starts.
        self.last_clipboard_content = self._get_clipboard_text() or ""

        while self.monitoring:
            try:
                # Check clipboard for new content
                current_clipboard = self._get_clipboard_text()
                
                if current_clipboard and current_clipboard != self.last_clipboard_content:
                    # New text detected in clipboard
                    if len(current_clipboard.strip()) > 0:
                        cursor_pos = self._get_cursor_position()
                        
                        logger.info(f"Text selected: {current_clipboard[:50]}...")
                        logger.info(f"Cursor position: {cursor_pos}")
                        
                        # Call the callback with selected text and position
                        self.callback(current_clipboard, cursor_pos)
                        
                    self.last_clipboard_content = current_clipboard
                    
            except Exception as e:
                logger.error(f"Error in monitor loop: {e}")
                
            # Check every 200ms for responsiveness
            time.sleep(0.2)
            
    def _get_clipboard_text(self) -> Optional[str]:
        """
        Get text content from Windows clipboard.
        
        Returns:
            Clipboard text content or None if clipboard is empty/unavailable.
        """
        try:
            # Try using pyperclip first (simpler)
            text = pyperclip.paste()
            return text if text else None
        except Exception as e:
            logger.debug(f"Pyperclip failed, trying win32clipboard: {e}")
            
        # Fallback to win32clipboard
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
                text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
                win32clipboard.CloseClipboard()
                return text
            win32clipboard.CloseClipboard()
        except Exception as e:
            logger.debug(f"Win32clipboard failed: {e}")
            try:
                win32clipboard.CloseClipboard()
            except:
                pass
                
        return None
        
    def _get_cursor_position(self) -> Tuple[int, int]:
        """
        Get current cursor position on screen.
        
        Returns:
            Tuple of (x, y) coordinates in pixels.
        """
        try:
            import win32api
            x, y = win32api.GetCursorPos()
            return (x, y)
        except Exception as e:
            logger.error(f"Failed to get cursor position: {e}")
            return (0, 0)
            
    def get_active_window_info(self) -> dict:
        """
        Get information about the currently active window.
        
        Returns:
            Dictionary with window title, class name, and process info.
        """
        try:
            hwnd = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            
            return {
                'hwnd': hwnd,
                'title': window_title,
                'class': class_name,
            }
        except Exception as e:
            logger.error(f"Failed to get window info: {e}")
            return {
                'hwnd': 0,
                'title': 'Unknown',
                'class': 'Unknown',
            }


class KeyboardShortcutDetector:
    """
    Alternative detector using keyboard shortcuts.
    Listens for Ctrl+C or custom shortcuts to detect text selection.
    """
    
    def __init__(self, callback: Callable[[str, Tuple[int, int]], None]):
        """
        Initialize keyboard shortcut detector.
        
        Args:
            callback: Function to call when shortcut is triggered.
        """
        self.callback = callback
        self.monitoring = False
        
    def start(self):
        """Start listening for keyboard shortcuts."""
        try:
            from pynput import keyboard
            
            def on_press(key):
                try:
                    # Check for Ctrl+C
                    if hasattr(key, 'char') and key.char == 'c':
                        # Check if Ctrl is pressed
                        if keyboard.Controller().pressed(keyboard.Key.ctrl):
                            # Wait a moment for clipboard to update
                            time.sleep(0.1)
                            text = pyperclip.paste()
                            if text:
                                detector = TextSelectionDetector(self.callback)
                                cursor_pos = detector._get_cursor_position()
                                self.callback(text, cursor_pos)
                except Exception as e:
                    logger.debug(f"Key press error: {e}")
                    
            self.listener = keyboard.Listener(on_press=on_press)
            self.listener.start()
            self.monitoring = True
            logger.info("Keyboard shortcut detector started")
            
        except ImportError:
            logger.error("pynput not installed. Install with: pip install pynput")
            
    def stop(self):
        """Stop listening for keyboard shortcuts."""
        if hasattr(self, 'listener'):
            self.listener.stop()
        self.monitoring = False
        logger.info("Keyboard shortcut detector stopped")


# Example usage
if __name__ == "__main__":
    def on_text_selected(text: str, position: Tuple[int, int]):
        """Callback function when text is selected."""
        print(f"\n{'='*50}")
        print(f"Text Selected: {text[:100]}...")
        print(f"Cursor Position: {position}")
        print(f"{'='*50}\n")
        
    # Create and start detector
    detector = TextSelectionDetector(on_text_selected)
    detector.start()
    
    print("SmartClick Text Detector Running...")
    print("Highlight any text and copy it (Ctrl+C) to test")
    print("Press Ctrl+C in terminal to stop")
    
    try:
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping detector...")
        detector.stop()
        print("Detector stopped")

# Made with Bob
