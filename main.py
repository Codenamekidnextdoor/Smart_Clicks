"""
SmartClick - AI-Powered Cursor Layer
Main application entry point that orchestrates all components.
"""

import sys
import logging
import signal
from pathlib import Path
from threading import Thread
import time

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from cursor_layer.detector import TextSelectionDetector
from cursor_layer.popup import SmartClickPopup
from ai_integration.bob_client import WatsonxClient, MockWatsonxClient
from database.db_manager import DatabaseManager
from ui.main_window import SmartClickMainWindow
from backend.shortcuts import HotkeyManager
from backend.text_capture import get_selected_text

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SmartClickApp:
    """
    Main SmartClick application.
    Coordinates text detection, popup display, and AI interactions.
    """
    
    def __init__(self, use_mock: bool = False, main_window: 'SmartClickMainWindow' = None):
        """
        Initialize SmartClick application.
        
        Args:
            use_mock: Use mock AI client for testing (default: False)
            main_window: The main control window (provides shared Tk root)
        """
        logger.info("Initializing SmartClick...")

        self.main_window = main_window
        
        # Initialize database
        self.db = DatabaseManager()
        logger.info("Database initialized")
        
        # Initialize AI client
        if use_mock:
            self.ai_client = MockWatsonxClient()
            logger.info("Using mock AI client")
        else:
            # Load config from database
            api_key = self.db.get_setting('watsonx_api_key')
            project_id = self.db.get_setting('watsonx_project_id')
            endpoint = self.db.get_setting('watsonx_endpoint')
            
            if not all([api_key, project_id]):
                logger.warning("IBM watsonx credentials not configured. Using mock client.")
                self.ai_client = MockWatsonxClient()
            else:
                try:
                    self.ai_client = WatsonxClient(
                        api_key=api_key,
                        project_id=project_id,
                        endpoint=endpoint
                    )
                    logger.info("IBM watsonx client initialized")
                except Exception as e:
                    logger.error(f"Failed to initialize watsonx client: {e}")
                    logger.info("Falling back to mock client")
                    self.ai_client = MockWatsonxClient()
        
        # Shared Tk root from main window (so popup uses Toplevel, not a second Tk)
        root = main_window.get_root() if main_window else None

        # Initialize popup
        self.popup = SmartClickPopup(on_action=self._handle_popup_action, root=root)
        logger.info("Popup initialized")
        
        # Initialize text detector (not started until enable() is called)
        self.detector = TextSelectionDetector(
            callback=self._handle_text_selection
        )
        logger.info("Text detector initialized")

        # Hotkey manager — Ctrl+Shift+Z captures selected text
        self.hotkey = HotkeyManager(key="z")
        logger.info("Hotkey manager initialized")
        
        # Current session
        self.current_session_id = None
        
        # Running / enabled flags
        self.running = False
        self._enabled = False
        self._detector_thread = None
        
    def start(self):
        """
        Prepare the application.  The Tk event loop is owned by
        SmartClickMainWindow and is started there; we only need to mark
        ourselves as running here.
        """
        logger.info("SmartClick ready.")
        self.running = True

    def enable(self):
        """Start monitoring text selection."""
        if self._enabled:
            return
        self._enabled = True
        # Start clipboard-poll detector
        self._detector_thread = Thread(target=self.detector.start, daemon=True)
        self._detector_thread.start()
        # Register Ctrl+Shift+Z hotkey
        try:
            self.hotkey.start(self._handle_hotkey)
            logger.info("Ctrl+Shift+Z hotkey registered")
        except Exception as e:
            logger.warning(f"Could not register hotkey: {e}")
        logger.info("Text detector started (enabled)")
        if self.main_window:
            self.main_window.set_status("enabled — monitoring text selection")

    def disable(self):
        """Stop monitoring text selection."""
        if not self._enabled:
            return
        self._enabled = False
        self.detector.stop()
        try:
            self.hotkey.stop()
        except Exception:
            pass
        self.popup.hide()
        logger.info("Text detector stopped (disabled)")
        if self.main_window:
            self.main_window.set_status("disabled")

    def _handle_hotkey(self):
        """Called when Ctrl+Shift+Z is pressed — capture highlighted text."""
        try:
            text = get_selected_text()
            if text and text.strip():
                import win32api
                cursor_pos = win32api.GetCursorPos()
                self._handle_text_selection(text.strip(), cursor_pos)
            else:
                logger.debug("Hotkey fired but no text was selected")
        except Exception as e:
            logger.error(f"Hotkey handler error: {e}")
            
    def stop(self):
        """Stop the SmartClick application."""
        logger.info("Stopping SmartClick...")
        self.running = False

        # Stop detector and hotkey
        self.detector.stop()
        try:
            self.hotkey.stop()
        except Exception:
            pass

        # Close database
        self.db.close()

        # Destroy popup
        self.popup.destroy()

        logger.info("SmartClick stopped")
        
    def _handle_text_selection(self, text: str, cursor_pos: tuple):
        """
        Handle text selection event from detector.
        
        Args:
            text: Selected text
            cursor_pos: Cursor position (x, y)
        """
        logger.info(f"Text selected: {text[:50]}... at {cursor_pos}")
        
        # Create new session
        self.current_session_id = self.db.create_session(
            selected_text=text,
            cursor_pos=cursor_pos
        )
        
        # Schedule the popup on the main Tk thread — Tkinter is NOT thread-safe
        # and this callback runs from the detector's background thread.
        x, y = cursor_pos
        root = self.main_window.get_root() if self.main_window else None
        if root:
            root.after(0, lambda t=text, px=x, py=y: self.popup.show(t, px + 10, py + 10))
        else:
            self.popup.show(text, x + 10, y + 10)
        
    def _handle_popup_action(self, action: str, text: str):
        """
        Handle action from popup.
        
        Args:
            action: Action name (summarize, rewrite, explain, chat)
            text: Text to process (selected text or user message)
        """
        logger.info(f"Handling action: {action}")
        
        try:
            # Add user message to database
            if self.current_session_id:
                self.db.add_message(
                    self.current_session_id,
                    'user',
                    f"{action}: {text}" if action != 'chat' else text
                )
            
            # Process with AI
            if action == "summarize":
                response = self.ai_client.summarize(self.popup.selected_text)
                
            elif action == "rewrite":
                response = self.ai_client.rewrite(self.popup.selected_text)
                
            elif action == "explain":
                response = self.ai_client.explain(self.popup.selected_text)
                
            elif action == "chat":
                # Get conversation history
                messages = []
                if self.current_session_id:
                    db_messages = self.db.get_session_messages(self.current_session_id)
                    messages = [
                        {'role': msg['role'], 'content': msg['content']}
                        for msg in db_messages
                    ]
                
                # Add context about selected text
                context = f"Context: User selected this text: '{self.popup.selected_text}'"
                
                response = self.ai_client.chat(
                    message=text,
                    context=context,
                    history=messages
                )
                
            else:
                response = f"Unknown action: {action}"
                
            # Add response to popup
            self.popup.add_assistant_message(response)
            
            # Add response to database
            if self.current_session_id:
                self.db.add_message(
                    self.current_session_id,
                    'assistant',
                    response
                )
                
            logger.info(f"Action completed: {action}")
            
        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            logger.error(error_msg)
            self.popup.add_assistant_message(error_msg)


def run_setup():
    """Run the setup application."""
    logger.info("Running setup...")
    
    # Import and run setup
    from app.setup import SmartClickSetup
    
    setup = SmartClickSetup()
    setup.run()


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='SmartClick - AI-Powered Cursor Layer')
    parser.add_argument(
        '--setup',
        action='store_true',
        help='Run setup configuration'
    )
    parser.add_argument(
        '--mock',
        action='store_true',
        help='Use mock AI client for testing'
    )
    
    args = parser.parse_args()
    
    # Run setup if requested
    if args.setup:
        run_setup()
        return

    # ── Build main window first so we have a Tk root ──────────────────────────
    # (app is passed in after construction so the window can call app.enable /
    #  app.disable; we wire the reference back once the app is ready)
    main_window = SmartClickMainWindow(app=None)

    # ── Create the app, sharing the Tk root ───────────────────────────────────
    app = SmartClickApp(use_mock=args.mock, main_window=main_window)
    main_window.app = app          # back-wire so buttons work

    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        logger.info("Signal received, shutting down...")
        app.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Mark app as ready (detector starts only when user presses Enable)
    app.start()

    # ── Hand control to Tkinter event loop (blocks until window is closed) ────
    try:
        main_window.run()
    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)
        app.stop()
        sys.exit(1)


if __name__ == "__main__":
    main()

# Made with Bob
