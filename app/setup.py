"""
SmartClick Setup Application
Simple GUI for configuring IBM watsonx credentials and application settings.
"""
 
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from pathlib import Path
import logging
 
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class SmartClickSetup:
    """
    Setup wizard for SmartClick configuration.
    Allows users to enter API credentials and configure settings.
    """
    
    def __init__(self):
        """Initialize the setup application."""
        self.root = tk.Tk()
        self.root.title("SmartClick Setup")
        self.root.geometry("600x750")
        self.root.resizable(False, False)
        
        # Configuration file path
        self.config_dir = Path.home() / ".smartclick"
        self.config_file = self.config_dir / "config.json"
        
        # Ensure config directory exists
        self.config_dir.mkdir(exist_ok=True)
        
        # Load existing config if available
        self.config = self.load_config()
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        """Create all UI widgets."""
        # Title
        title_frame = tk.Frame(self.root, bg="#0f62fe", height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="🤖 SmartClick Setup",
            font=("Arial", 24, "bold"),
            bg="#0f62fe",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Scrollable canvas
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, padx=40, pady=30)
 
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
 
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
 
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
 
        # Use scrollable_frame as content_frame
        content_frame = scrollable_frame
        
        # Instructions
        instructions = tk.Label(
            content_frame,
            text="Configure your IBM watsonx credentials to get started",
            font=("Arial", 11),
            fg="#525252"
        )
        instructions.pack(pady=(0, 20))
        
        # API Key
        api_key_label = tk.Label(
            content_frame,
            text="IBM watsonx API Key:",
            font=("Arial", 10, "bold")
        )
        api_key_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.api_key_entry = tk.Entry(content_frame, width=50, show="*")
        self.api_key_entry.pack(fill=tk.X, pady=(0, 5))
        self.api_key_entry.insert(0, self.config.get("api_key", ""))
        
        api_key_help = tk.Label(
            content_frame,
            text="Get your API key from: https://cloud.ibm.com/iam/apikeys",
            font=("Arial", 8),
            fg="#666666"
        )
        api_key_help.pack(anchor=tk.W, pady=(0, 15))
        
        # Project ID
        project_id_label = tk.Label(
            content_frame,
            text="watsonx Project ID:",
            font=("Arial", 10, "bold")
        )
        project_id_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.project_id_entry = tk.Entry(content_frame, width=50)
        self.project_id_entry.pack(fill=tk.X, pady=(0, 5))
        self.project_id_entry.insert(0, self.config.get("project_id", ""))
        
        project_id_help = tk.Label(
            content_frame,
            text="Find your Project ID in the watsonx project URL",
            font=("Arial", 8),
            fg="#666666"
        )
        project_id_help.pack(anchor=tk.W, pady=(0, 15))
        
        # Endpoint
        endpoint_label = tk.Label(
            content_frame,
            text="API Endpoint (optional):",
            font=("Arial", 10, "bold")
        )
        endpoint_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.endpoint_entry = tk.Entry(content_frame, width=50)
        self.endpoint_entry.pack(fill=tk.X, pady=(0, 5))
        self.endpoint_entry.insert(0, self.config.get("endpoint", "https://us-south.ml.cloud.ibm.com"))
        
        endpoint_help = tk.Label(
            content_frame,
            text="Default: https://us-south.ml.cloud.ibm.com",
            font=("Arial", 8),
            fg="#666666"
        )
        endpoint_help.pack(anchor=tk.W, pady=(0, 15))
        
        # Keyboard Shortcut
        shortcut_label = tk.Label(
            content_frame,
            text="Activation Shortcut:",
            font=("Arial", 10, "bold")
        )
        shortcut_label.pack(anchor=tk.W, pady=(10, 5))
        
        shortcut_frame = tk.Frame(content_frame)
        shortcut_frame.pack(fill=tk.X, pady=(0, 5))
        
        self.shortcut_var = tk.StringVar(value=self.config.get("shortcut", "Ctrl+Shift+S"))
        shortcuts = ["Ctrl+Shift+S", "Ctrl+Alt+S", "Ctrl+Shift+A", "Custom"]
        self.shortcut_combo = ttk.Combobox(
            shortcut_frame,
            textvariable=self.shortcut_var,
            values=shortcuts,
            state="readonly",
            width=20
        )
        self.shortcut_combo.pack(side=tk.LEFT)
        
        shortcut_help = tk.Label(
            content_frame,
            text="Keyboard shortcut to activate SmartClick",
            font=("Arial", 8),
            fg="#666666"
        )
        shortcut_help.pack(anchor=tk.W, pady=(0, 20))
 
        # Divider
        divider = tk.Frame(content_frame, height=2, bg="#e0e0e0")
        divider.pack(fill=tk.X, pady=(10, 20))
        
        # Buttons
        button_frame = tk.Frame(content_frame)
        button_frame.pack(pady=20)
        
        test_button = tk.Button(
            button_frame,
            text="Test Connection",
            command=self.test_connection,
            bg="#f4f4f4",
            fg="#161616",
            font=("Arial", 10),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        test_button.pack(side=tk.LEFT, padx=5)
        
        save_button = tk.Button(
            button_frame,
            text="Save & Start",
            command=self.save_and_start,
            bg="#0f62fe",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=30,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        save_button.pack(side=tk.LEFT, padx=5)
 
        # Status label
        self.status_label = tk.Label(
            content_frame,
            text="",
            font=("Arial", 9),
            fg="#0f62fe"
        )
        self.status_label.pack(pady=(10, 0))
        
    def load_config(self) -> dict:
        """
        Load existing configuration from file.
        
        Returns:
            Configuration dictionary
        """
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                logger.info("Configuration loaded")
                return config
            except Exception as e:
                logger.error(f"Failed to load config: {e}")
                
        return {}
        
    def save_config(self) -> bool:
        """
        Save configuration to file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            config = {
                "api_key": self.api_key_entry.get().strip(),
                "project_id": self.project_id_entry.get().strip(),
                "endpoint": self.endpoint_entry.get().strip(),
                "shortcut": self.shortcut_var.get(),
            }
            
            # Validate required fields
            if not config["api_key"]:
                messagebox.showerror("Error", "API Key is required")
                return False
                
            if not config["project_id"]:
                messagebox.showerror("Error", "Project ID is required")
                return False
                
            # Save to file
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
                
            logger.info(f"Configuration saved to {self.config_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            messagebox.showerror("Error", f"Failed to save configuration: {e}")
            return False
            
    def test_connection(self):
        """Test connection to IBM watsonx API."""
        api_key = self.api_key_entry.get().strip()
        project_id = self.project_id_entry.get().strip()
        
        if not api_key or not project_id:
            messagebox.showwarning("Warning", "Please enter API Key and Project ID first")
            return
 
        # Update status
        self.status_label.config(text="Testing connection...", fg="#0f62fe")
        self.root.update()
            
        # Show testing message
        test_window = tk.Toplevel(self.root)
        test_window.title("Testing Connection")
        test_window.geometry("300x100")
        test_window.transient(self.root)
        test_window.grab_set()
        
        label = tk.Label(test_window, text="Testing connection...", font=("Arial", 11))
        label.pack(pady=30)
        
        self.root.update()
        
        try:
            from ai_integration.bob_client import create_client
            
            client = create_client(api_key, project_id)
            response = client.generate_text("Hello", max_tokens=10)
            
            test_window.destroy()
            self.status_label.config(text="✅ Connection successful!", fg="green")
            messagebox.showinfo("Success", "Connection successful!\n\nYour credentials are working.")
            
        except Exception as e:
            test_window.destroy()
            self.status_label.config(text="❌ Connection failed. Check your credentials.", fg="red")
            messagebox.showerror("Connection Failed", f"Failed to connect:\n\n{str(e)}\n\nPlease check your credentials.")
            
    def save_and_start(self):
        """Save configuration and start SmartClick."""
        if self.save_config():
            self.status_label.config(text="✅ Configuration saved!", fg="green")
            messagebox.showinfo(
                "Success",
                "Configuration saved successfully!\n\nSmartClick will now start in the background.\n\nHighlight any text and press Ctrl+C to activate."
            )
            self.root.quit()
            
    def run(self):
        """Run the setup application."""
        self.root.mainloop()
 
 
def main():
    """Main entry point for setup application."""
    app = SmartClickSetup()
    app.run()
 
 
if __name__ == "__main__":
    main()
 
# Made with Bob