# SmartClick Quick Start Guide

Get SmartClick up and running in 5 minutes!

## 🎯 Goal

By the end of this guide, you'll have SmartClick running on your Windows machine, ready to provide AI assistance for any text you select.

## ⚡ Fast Track (3 Steps)

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the SmartClick directory:

```bash
pip install -r requirements.txt
```

This installs:
- IBM watsonx SDK
- Windows API libraries (pywin32, pyperclip)
- Other utilities

### Step 2: Configure (Choose One)

**Option A: Use Mock AI (No credentials needed)**
```bash
python main.py --mock
```
Perfect for testing the interface without IBM watsonx.

**Option B: Use Real IBM watsonx**
```bash
python main.py --setup
```
Enter your IBM watsonx credentials when prompted.

### Step 3: Start Using

1. **Select any text** in any application
2. **SmartClick popup appears** automatically
3. **Click an action**: Chat, Summarize, Rewrite, or Explain
4. **Get AI assistance** instantly!

## 📝 Detailed Setup

### Prerequisites Check

Before starting, verify you have:

- ✅ Windows 10 or 11
- ✅ Python 3.8 or higher
  ```bash
  python --version
  ```
- ✅ pip (Python package manager)
  ```bash
  pip --version
  ```

### Installation Steps

#### 1. Clone or Download

```bash
# If using Git
git clone https://github.com/yourusername/SmartClick.git
cd SmartClick

# Or download and extract ZIP, then navigate to folder
cd path/to/SmartClick
```

#### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt:
.\venv\Scripts\activate.bat
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed ibm-watson-machine-learning-1.0.335 ...
```

#### 4. Configure IBM watsonx (Optional)

If you have IBM watsonx credentials:

```bash
python main.py --setup
```

The setup window will open. Enter:

1. **API Key**: Your IBM Cloud API key
2. **Project ID**: Your watsonx project ID
3. **Endpoint**: (Optional) Default is US-South
4. **Keyboard Shortcut**: (Optional) For future use

Click **Test Connection** to verify, then **Save**.

**Don't have credentials?** See [GET_WATSONX_CREDENTIALS.md](docs/GET_WATSONX_CREDENTIALS.md)

#### 5. Start SmartClick

**With IBM watsonx:**
```bash
python main.py
```

**With Mock AI (for testing):**
```bash
python main.py --mock
```

You should see:
```
INFO - Initializing SmartClick...
INFO - Database initialized
INFO - IBM watsonx client initialized
INFO - Popup initialized
INFO - Text detector initialized
INFO - Starting SmartClick...
INFO - Text detector started
```

## 🎮 Using SmartClick

### Basic Usage

1. **Open any application** (browser, Word, Notepad, etc.)
2. **Select/highlight some text**
3. **SmartClick popup appears** near your cursor
4. **Choose an action**:
   - 💬 **Chat**: Opens full chat interface
   - 📝 **Summarize**: Get a quick summary
   - ✏️ **Rewrite**: Improve or rephrase
   - 💡 **Explain**: Get detailed explanation

### Chat Mode

1. Click **💬 Chat** button
2. Popup expands to full chat interface
3. Type your question in the input box
4. Press **Enter** to send (Shift+Enter for new line)
5. Bob responds with AI-powered answers
6. Continue the conversation!

### Quick Actions

For one-off tasks, use the quick action buttons:

- **Summarize**: "Summarize this article for me"
- **Rewrite**: "Make this more professional"
- **Explain**: "Explain this concept in simple terms"

The popup expands automatically to show the result.

### Keyboard Shortcuts

- **Escape**: Close popup
- **Enter**: Send message (in chat)
- **Shift+Enter**: New line (in chat)

## 🧪 Testing

### Test 1: Basic Text Selection

1. Open Notepad
2. Type: "Machine learning is a subset of artificial intelligence"
3. Select the text
4. SmartClick popup should appear

### Test 2: Quick Action

1. With text selected, click **📝 Summarize**
2. Popup expands showing summary
3. Verify the response makes sense

### Test 3: Chat Conversation

1. Select some text
2. Click **💬 Chat**
3. Type: "Can you explain this in simple terms?"
4. Press Enter
5. Verify you get a response
6. Ask a follow-up question

## 🔧 Troubleshooting

### Popup Not Appearing

**Problem**: Selected text but no popup

**Solutions**:
1. Check SmartClick is running (look for console window)
2. Try copying text (Ctrl+C) - this triggers detection
3. Restart SmartClick: Close and run `python main.py` again

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'xyz'`

**Solution**:
```bash
pip install -r requirements.txt --force-reinstall
```

### IBM watsonx Connection Failed

**Problem**: "Failed to connect to IBM watsonx"

**Solutions**:
1. Verify credentials: `python main.py --setup`
2. Test with mock mode: `python main.py --mock`
3. Check internet connection
4. Verify IBM Cloud status: https://cloud.ibm.com/status

### Python Not Found

**Problem**: `'python' is not recognized...`

**Solution**:
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart terminal/PowerShell

### Permission Errors

**Problem**: Access denied or permission errors

**Solution**:
1. Run PowerShell/Command Prompt as Administrator
2. Or install in user directory (no admin needed)

## 📊 What's Happening Behind the Scenes

When you run SmartClick:

1. **Database initialized**: SQLite database created at `~/.smartclick/smartclick.db`
2. **AI client connected**: Connects to IBM watsonx (or mock)
3. **Text detector started**: Monitors clipboard for text selection
4. **Popup ready**: Invisible window ready to appear

When you select text:

1. **Detection**: Clipboard monitor detects text selection
2. **Session created**: New session saved to database
3. **Popup shown**: Window appears at cursor position
4. **Action processed**: Your choice sent to AI
5. **Response displayed**: AI response shown in popup
6. **History saved**: Conversation saved to database

## 🎓 Next Steps

Now that SmartClick is running:

1. **Try different applications**: Browser, Word, PDF reader, email
2. **Experiment with actions**: See what works best for different tasks
3. **Use chat mode**: Have longer conversations about complex topics
4. **Check history**: Your conversations are saved in the database
5. **Customize settings**: Run `python main.py --setup` to adjust

## 📚 Learn More

- **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Development Plan**: [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md)
- **API Integration**: [docs/API_INTEGRATION.md](docs/API_INTEGRATION.md)
- **Full README**: [README.md](README.md)

## 💬 Need Help?

- Check [README.md](README.md) troubleshooting section
- Review documentation in [docs/](docs/)
- Open an issue on GitHub
- Email: support@smartclick.ai

## 🎉 Success!

You're now ready to use SmartClick! Select any text and let Bob help you understand, improve, or discuss it.

**Pro Tip**: Keep SmartClick running in the background. It uses minimal resources and is always ready when you need it.

---

**Happy SmartClicking! 🚀**