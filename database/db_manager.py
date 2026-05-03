"""
SQLite Database Manager for SmartClick
Handles chat history, context storage, and user settings.
"""

import sqlite3
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Manages SQLite database for SmartClick.
    Stores chat history, selected text context, and user preferences.
    """
    
    def __init__(self, db_path: str = None):
        """
        Initialize database manager.
        
        Args:
            db_path: Path to SQLite database file (default: ~/.smartclick/smartclick.db)
        """
        if db_path is None:
            db_dir = Path.home() / ".smartclick"
            db_dir.mkdir(exist_ok=True)
            db_path = str(db_dir / "smartclick.db")
            
        self.db_path = db_path
        self.conn = None
        
        # Initialize database
        self.connect()
        self.create_tables()
        
    def connect(self):
        """Connect to SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
            logger.info(f"Connected to database: {self.db_path}")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise
            
    def create_tables(self):
        """Create database tables if they don't exist."""
        try:
            cursor = self.conn.cursor()
            
            # Sessions table - stores text selection sessions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    selected_text TEXT NOT NULL,
                    application_name TEXT,
                    window_title TEXT,
                    cursor_x INTEGER,
                    cursor_y INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Messages table - stores chat messages
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
                )
            """)
            
            # Settings table - stores user preferences
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Context table - stores additional context for sessions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS context (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER NOT NULL,
                    context_type TEXT NOT NULL,
                    context_data TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
                )
            """)
            
            # Create indexes for better performance
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_messages_session 
                ON messages(session_id, created_at)
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_sessions_created 
                ON sessions(created_at DESC)
            """)
            
            self.conn.commit()
            logger.info("Database tables created/verified")
            
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise
            
    def create_session(self, selected_text: str, app_name: str = None, 
                      window_title: str = None, cursor_pos: tuple = None) -> int:
        """
        Create a new session.
        
        Args:
            selected_text: The text that was selected
            app_name: Name of the application
            window_title: Title of the window
            cursor_pos: Tuple of (x, y) cursor position
            
        Returns:
            Session ID
        """
        try:
            cursor = self.conn.cursor()
            
            cursor_x, cursor_y = cursor_pos if cursor_pos else (None, None)
            
            cursor.execute("""
                INSERT INTO sessions (selected_text, application_name, window_title, cursor_x, cursor_y)
                VALUES (?, ?, ?, ?, ?)
            """, (selected_text, app_name, window_title, cursor_x, cursor_y))
            
            self.conn.commit()
            session_id = cursor.lastrowid
            
            logger.info(f"Created session {session_id}")
            return session_id
            
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            raise
            
    def add_message(self, session_id: int, role: str, content: str) -> int:
        """
        Add a message to a session.
        
        Args:
            session_id: Session ID
            role: Message role ('user' or 'assistant')
            content: Message content
            
        Returns:
            Message ID
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                INSERT INTO messages (session_id, role, content)
                VALUES (?, ?, ?)
            """, (session_id, role, content))
            
            # Update session timestamp
            cursor.execute("""
                UPDATE sessions SET updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (session_id,))
            
            self.conn.commit()
            message_id = cursor.lastrowid
            
            logger.info(f"Added {role} message to session {session_id}")
            return message_id
            
        except Exception as e:
            logger.error(f"Failed to add message: {e}")
            raise
            
    def get_session_messages(self, session_id: int) -> List[Dict[str, Any]]:
        """
        Get all messages for a session.
        
        Args:
            session_id: Session ID
            
        Returns:
            List of message dictionaries
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT id, role, content, created_at
                FROM messages
                WHERE session_id = ?
                ORDER BY created_at ASC
            """, (session_id,))
            
            messages = [dict(row) for row in cursor.fetchall()]
            return messages
            
        except Exception as e:
            logger.error(f"Failed to get messages: {e}")
            return []
            
    def get_session(self, session_id: int) -> Optional[Dict[str, Any]]:
        """
        Get session details.
        
        Args:
            session_id: Session ID
            
        Returns:
            Session dictionary or None
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT * FROM sessions WHERE id = ?
            """, (session_id,))
            
            row = cursor.fetchone()
            return dict(row) if row else None
            
        except Exception as e:
            logger.error(f"Failed to get session: {e}")
            return None
            
    def get_recent_sessions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent sessions.
        
        Args:
            limit: Maximum number of sessions to return
            
        Returns:
            List of session dictionaries
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT s.*, COUNT(m.id) as message_count
                FROM sessions s
                LEFT JOIN messages m ON s.id = m.session_id
                GROUP BY s.id
                ORDER BY s.updated_at DESC
                LIMIT ?
            """, (limit,))
            
            sessions = [dict(row) for row in cursor.fetchall()]
            return sessions
            
        except Exception as e:
            logger.error(f"Failed to get recent sessions: {e}")
            return []
            
    def set_setting(self, key: str, value: Any):
        """
        Save a setting.
        
        Args:
            key: Setting key
            value: Setting value (will be JSON encoded)
        """
        try:
            cursor = self.conn.cursor()
            
            value_json = json.dumps(value)
            
            cursor.execute("""
                INSERT OR REPLACE INTO settings (key, value, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            """, (key, value_json))
            
            self.conn.commit()
            logger.info(f"Setting saved: {key}")
            
        except Exception as e:
            logger.error(f"Failed to save setting: {e}")
            raise
            
    def get_setting(self, key: str, default: Any = None) -> Any:
        """
        Get a setting value.
        
        Args:
            key: Setting key
            default: Default value if not found
            
        Returns:
            Setting value or default
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT value FROM settings WHERE key = ?
            """, (key,))
            
            row = cursor.fetchone()
            if row:
                return json.loads(row['value'])
            return default
            
        except Exception as e:
            logger.error(f"Failed to get setting: {e}")
            return default
            
    def delete_old_sessions(self, days: int = 30) -> int:
        """
        Delete sessions older than specified days.
        
        Args:
            days: Number of days to keep
            
        Returns:
            Number of sessions deleted
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                DELETE FROM sessions
                WHERE created_at < datetime('now', '-' || ? || ' days')
            """, (days,))
            
            self.conn.commit()
            deleted = cursor.rowcount
            
            logger.info(f"Deleted {deleted} old sessions")
            return deleted
            
        except Exception as e:
            logger.error(f"Failed to delete old sessions: {e}")
            return 0
            
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")


# Example usage
if __name__ == "__main__":
    # Create database manager
    db = DatabaseManager()
    
    # Create a test session
    session_id = db.create_session(
        selected_text="Machine learning is a subset of AI",
        app_name="Chrome",
        window_title="Wikipedia - Machine Learning",
        cursor_pos=(100, 200)
    )
    
    print(f"Created session: {session_id}")
    
    # Add messages
    db.add_message(session_id, "user", "Can you explain this?")
    db.add_message(session_id, "assistant", "Machine learning allows computers to learn from data...")
    
    # Get messages
    messages = db.get_session_messages(session_id)
    print(f"\nMessages in session {session_id}:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    
    # Get recent sessions
    recent = db.get_recent_sessions(5)
    print(f"\nRecent sessions: {len(recent)}")
    
    # Save/get settings
    db.set_setting("theme", "dark")
    theme = db.get_setting("theme")
    print(f"\nTheme setting: {theme}")
    
    # Close
    db.close()

# Made with Bob
