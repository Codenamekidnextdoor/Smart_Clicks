# SmartClick - AI-Powered Cursor Layer

SmartClick brings IBM Bob AI directly into any application you're working in. Highlight text anywhere on your system, and instantly access AI-powered assistance through an elegant popup interface.

## 🌟 Features

- **System-Wide Text Selection**: Works across all applications - browsers, IDEs, documents, email clients
- **Instant AI Access**: Popup appears immediately when you select text
- **Multiple AI Actions**:
  - 💬 **Chat**: Have a conversation about the selected text
  - 📝 **Summarize**: Get concise summaries
  - ✏️ **Rewrite**: Improve or rephrase text
  - 💡 **Explain**: Get detailed explanations
- **Context-Aware**: Maintains conversation context throughout the session
- **Chat History**: All interactions are saved locally in SQLite
- **Expandable Interface**: Quick actions popup expands into full chat interface
- **IBM watsonx Integration**: Powered by enterprise-grade AI

## 📋 Prerequisites

- **Windows 10/11** (currently Windows-only)
- **Python 3.8+**
- **IBM watsonx Account** with API credentials ([Get credentials](docs/GET_WATSONX_CREDENTIALS.md))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SmartClick.git
cd SmartClick
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Setup

Configure your IBM watsonx credentials:

```bash
python main.py --setup
```

Enter your:
- IBM watsonx API Key
- Project ID
- Endpoint URL (optional)
- Keyboard shortcut (optional)

### 4. Start SmartClick

```bash
python main.py
```

That's it! SmartClick is now running in the background.

## 💡 How to Use

1. **Select Text**: Highlight any text in any application
2. **Wait for Popup**: SmartClick popup appears automatically
3. **Choose Action**: Click one of the quick action buttons:
   - 💬 Chat - Opens full chat interface
   - 📝 Summarize - Get a summary
   - ✏️ Rewrite - Improve the text
   - 💡 Explain - Get an explanation
4. **Continue Conversation**: In chat mode, ask follow-up questions

### Keyboard Shortcuts

- **Escape**: Close popup
- **Enter**: Send message (in chat mode)
- **Shift+Enter**: New line (in chat mode)

## 🧪 Testing Without IBM watsonx

You can test SmartClick without IBM watsonx credentials using the mock client:

```bash
python main.py --mock
```

This uses simulated AI responses for testing the interface and workflow.

## 📁 Project Structure

```
SmartClick/
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
│
├── cursor_layer/                # Text detection and popup
│   ├── detector.py             # System-wide text selection detection
│   └── popup.py                # Popup window interface
│
├── ai_integration/              # IBM watsonx integration
│   └── bob_client.py           # AI client (real + mock)
│
├── database/                    # Data persistence
│   └── db_manager.py           # SQLite database manager
│
├── app/                         # Configuration UI
│   └── setup.py                # Setup/settings interface
│
└── docs/                        # Documentation
    ├── ARCHITECTURE.md          # System architecture
    ├── DEVELOPMENT_PLAN.md      # Development roadmap
    ├── API_INTEGRATION.md       # API integration guide
    └── GET_WATSONX_CREDENTIALS.md  # Credential setup guide
```

## 🔧 Configuration

Configuration is stored in `~/.smartclick/config.json`:

```json
{
  "watsonx_api_key": "your-api-key",
  "watsonx_project_id": "your-project-id",
  "watsonx_endpoint": "https://us-south.ml.cloud.ibm.com",
  "keyboard_shortcut": "Ctrl+Shift+A"
}
```

Database is stored in `~/.smartclick/smartclick.db`

## 🗄️ Database Schema

SmartClick uses SQLite to store:

- **Sessions**: Each text selection creates a session
- **Messages**: All chat messages (user + assistant)
- **Settings**: User preferences and configuration
- **Context**: Additional context for sessions

## 🔌 API Integration

SmartClick integrates with IBM watsonx using the official Python SDK:

```python
from ai_integration.bob_client import WatsonxClient

client = WatsonxClient(
    api_key="your-api-key",
    project_id="your-project-id"
)

# Summarize text
summary = client.summarize("Your text here...")

# Chat with context
response = client.chat(
    message="Explain this",
    context="Selected text: ...",
    history=[...]
)
```

See [API_INTEGRATION.md](docs/API_INTEGRATION.md) for detailed documentation.

## 🐛 Troubleshooting

### Popup Not Appearing

1. Check that SmartClick is running: `python main.py`
2. Try selecting text again
3. Check logs for errors

### IBM watsonx Connection Issues

1. Verify credentials in setup: `python main.py --setup`
2. Test connection in setup interface
3. Check [IBM Cloud status](https://cloud.ibm.com/status)
4. Use mock mode for testing: `python main.py --mock`

### Text Detection Not Working

1. Ensure you're selecting text (not just clicking)
2. Try copying text to clipboard (Ctrl+C)
3. Check Windows permissions for clipboard access

## 📊 Development Status

- ✅ Core text detection system
- ✅ Popup interface with quick actions
- ✅ IBM watsonx integration
- ✅ Chat interface with history
- ✅ SQLite database for persistence
- ✅ Configuration UI
- 🚧 Keyboard shortcuts (planned)
- 🚧 System tray icon (planned)
- 🚧 Auto-start on Windows boot (planned)

## 🛣️ Roadmap

### Phase 1: MVP (Current)
- [x] Text selection detection
- [x] Basic popup interface
- [x] IBM watsonx integration
- [x] Chat functionality
- [x] Database storage

### Phase 2: Enhancement
- [ ] Custom keyboard shortcuts
- [ ] System tray integration
- [ ] Auto-start on boot
- [ ] Settings panel
- [ ] Theme customization

### Phase 3: Advanced Features
- [ ] Multi-language support
- [ ] Custom AI prompts
- [ ] Export chat history
- [ ] Cloud sync (optional)
- [ ] Browser extension integration

See [DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md) for detailed roadmap.

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

[MIT License](LICENSE)

## 🙏 Acknowledgments

- IBM watsonx for AI capabilities
- Python community for excellent libraries
- All contributors and testers

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/SmartClick/issues)
- **Email**: support@smartclick.ai

## 🔐 Privacy & Security

- All data stored locally on your machine
- No telemetry or tracking
- IBM watsonx API calls follow IBM's privacy policy
- API keys stored securely in local config file

---

**Made with ❤️ for productivity enthusiasts**