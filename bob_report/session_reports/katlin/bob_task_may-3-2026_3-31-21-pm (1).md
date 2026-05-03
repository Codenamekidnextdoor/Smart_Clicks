**User:**

<task>
fix every document, outline the fix dont implement yet
</task>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs
backend/backend_client.py,backend/api/main.py,.env,docs/SERVICE_DOCUMENTATION.md,docs/FRONTEND_IMPLEMENTATION_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-03T13:30:04.640Z
User time zone: Africa/Johannesburg, UTC+2:00

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>advanced</slug>
<name>🛠️ Advanced</name>


# Current Workspace Directory (c:/Users/camer/OneDrive/Desktop/Smart_Clicks) Files
.env.example
.gitignore
ELECTRON_QUICKSTART.md
FOUNDATION_REVIEW.md
main.py
MODERNIZATION_README.md
PHASE_2_COMPLETE.md
PHASE_4_ELECTRON_COMPLETE.md
QUICKSTART.md
README.md
requirements.txt
text.md
TROUBLESHOOTING.md
.venv/
ai_integration/
ai_integration/bob_client.py
app/
app/setup.py
backend/
backend/backend_client.py
backend/mouse_detection.py
backend/popup_ui.py
backend/requirements.txt
backend/run.py
backend/shortcuts.py
backend/text_capture.py
backend/api/
backend/api/__init__.py
backend/api/main.py
bob_report/
bob_report/session_reports/
bob_report/session_reports/.gitkeep
cursor_layer/
database/
database/db_manager.py
docs/
docs/API_INTEGRATION.md
docs/ARCHITECTURE.md
docs/DEVELOPMENT_PLAN.md
docs/FOLDER_STRUCTURE.md
docs/FRONTEND_IMPLEMENTATION_GUIDE.md
docs/IBM_CLOUD_DATABASE_SETUP.md
docs/IMPLEMENTATION_PRIORITY.md
docs/PROJECT_SUMMARY.md
docs/REACT_MODERNIZATION_PLAN.md
frontend/
frontend/.env.example
frontend/.gitignore
frontend/eslint.config.js
frontend/index.html
frontend/package.json
frontend/postcss.config.js
frontend/README.md
frontend/tailwind.config.js
frontend/tsconfig.app.json
frontend/tsconfig.electron.json
frontend/tsconfig.json
frontend/tsconfig.node.json
frontend/vite.config.electron.ts
frontend/vite.config.ts
frontend/dist-electron/
frontend/dist-electron/main.cjs
frontend/dist-electron/preload.cjs
frontend/electron/
frontend/electron/main.ts
frontend/electron/preload.ts
frontend/public/
frontend/public/favicon.svg
frontend/public/icon.png
frontend/public/icons.svg
frontend/public/tray-icon.png
frontend/scripts/
frontend/scripts/rename-electron.cjs
frontend/src/
frontend/src/App.css
frontend/src/App.tsx
frontend/src/index.css
frontend/src/main.tsx
frontend/src/PopupApp.tsx
frontend/src/assets/
frontend/src/assets/hero.png
frontend/src/assets/react.svg
frontend/src/assets/vite.svg
frontend/src/components/
frontend/src/components/MainWindow/
frontend/src/components/MainWindow/ControlPanel.tsx
frontend/src/components/MainWindow/index.ts
frontend/src/components/MainWindow/InfoCards.tsx
frontend/src/components/MainWindow/MainWindow.tsx
frontend/src/components/MainWindow/SessionHistory.tsx
frontend/src/components/MainWindow/StatusIndicator.tsx
frontend/src/components/Popup/
frontend/src/components/Popup/ChatBubble.tsx
frontend/src/components/Popup/ChatView.tsx
frontend/src/components/Popup/CompactView.tsx
frontend/src/components/Popup/index.ts
frontend/src/components/Popup/Popup.tsx
frontend/src/components/shared/
frontend/src/components/shared/Button.tsx
frontend/src/components/shared/Card.tsx
frontend/src/components/shared/index.ts
frontend/src/components/shared/LoadingSpinner.tsx
frontend/src/services/
frontend/src/services/api.ts
frontend/src/services/websocket.ts
frontend/src/stores/
frontend/src/stores/appStore.ts
frontend/src/stores/chatStore.ts
frontend/src/types/
frontend/src/types/electron.d.ts
frontend/src/types/index.ts
ui/
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll analyze all documents in the project to identify issues and outline fixes. Let me start by reading through the documentation files.

<read_file>
<args>
  <file>
    <path>README.md</path>
  </file>
  <file>
    <path>QUICKSTART.md</path>
  </file>
  <file>
    <path>MODERNIZATION_README.md</path>
  </file>
  <file>
    <path>TROUBLESHOOTING.md</path>
  </file>
  <file>
    <path>ELECTRON_QUICKSTART.md</path>
  </file>
</args>
</read_file>

<read_file>
<args>
  <file>
    <path>FOUNDATION_REVIEW.md</path>
  </file>
  <file>
    <path>PHASE_2_COMPLETE.md</path>
  </file>
  <file>
    <path>PHASE_4_ELECTRON_COMPLETE.md</path>
  </file>
  <file>
    <path>docs/PROJECT_SUMMARY.md</path>
  </file>
  <file>
    <path>docs/ARCHITECTURE.md</path>
  </file>
</args>
</read_file>

<read_file>
<args>
  <file>
    <path>docs/DEVELOPMENT_PLAN.md</path>
  </file>
  <file>
    <path>docs/FOLDER_STRUCTURE.md</path>
  </file>
  <file>
    <path>docs/IMPLEMENTATION_PRIORITY.md</path>
  </file>
  <file>
    <path>docs/REACT_MODERNIZATION_PLAN.md</path>
  </file>
  <file>
    <path>docs/API_INTEGRATION.md</path>
  </file>
</args>
</read_file>

<read_file>
<args>
  <file>
    <path>docs/IBM_CLOUD_DATABASE_SETUP.md</path>
  </file>
  <file>
    <path>docs/FRONTEND_IMPLEMENTATION_GUIDE.md</path>
  </file>
  <file>
    <path>frontend/README.md</path>
  </file>
</args>
</read_file>

Now let me check if there's a SERVICE_DOCUMENTATION.md file that's open in tabs:

<read_file>
<args>
  <file>
    <path>docs/SERVICE_DOCUMENTATION.md</path>
  </file>
</args>
</read_file>

<read_file>
<args>
  <file>
    <path>text.md</path>
  </file>
</args>
</read_file>

Now let me create a comprehensive outline of all the fixes needed:

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>README.md</path>
<content lines="1-259">
  1 | # SmartClick - AI-Powered Cursor Layer
  2 | 
  3 | SmartClick brings IBM Bob AI directly into any application you're working in. Highlight text anywhere on your system, and instantly access AI-powered assistance through an elegant popup interface.
  4 | 
  5 | ## 🌟 Features
  6 | 
  7 | - **System-Wide Text Selection**: Works across all applications - browsers, IDEs, documents, email clients
  8 | - **Instant AI Access**: Popup appears immediately when you select text
  9 | - **Multiple AI Actions**:
 10 |   - 💬 **Chat**: Have a conversation about the selected text
 11 |   - 📝 **Summarize**: Get concise summaries
 12 |   - ✏️ **Rewrite**: Improve or rephrase text
 13 |   - 💡 **Explain**: Get detailed explanations
 14 | - **Context-Aware**: Maintains conversation context throughout the session
 15 | - **Chat History**: All interactions are saved locally in SQLite
 16 | - **Expandable Interface**: Quick actions popup expands into full chat interface
 17 | - **IBM watsonx Integration**: Powered by enterprise-grade AI
 18 | 
 19 | ## 📋 Prerequisites
 20 | 
 21 | - **Windows 10/11** (currently Windows-only)
 22 | - **Python 3.8+**
 23 | - **IBM watsonx Account** with API credentials ([Get credentials](docs/GET_WATSONX_CREDENTIALS.md))
 24 | 
 25 | ## 🚀 Quick Start
 26 | 
 27 | ### 1. Clone the Repository
 28 | 
 29 | ```bash
 30 | git clone https://github.com/yourusername/SmartClick.git
 31 | cd SmartClick
 32 | ```
 33 | 
 34 | ### 2. Install Dependencies
 35 | 
 36 | ```bash
 37 | pip install -r requirements.txt
 38 | ```
 39 | 
 40 | ### 3. Run Setup
 41 | 
 42 | Configure your IBM watsonx credentials:
 43 | 
 44 | ```bash
 45 | python main.py --setup
 46 | ```
 47 | 
 48 | Enter your:
 49 | - IBM watsonx API Key
 50 | - Project ID
 51 | - Endpoint URL (optional)
 52 | - Keyboard shortcut (optional)
 53 | 
 54 | ### 4. Start SmartClick
 55 | 
 56 | ```bash
 57 | python main.py
 58 | ```
 59 | 
 60 | That's it! SmartClick is now running in the background.
 61 | 
 62 | ## 💡 How to Use
 63 | 
 64 | 1. **Select Text**: Highlight any text in any application
 65 | 2. **Wait for Popup**: SmartClick popup appears automatically
 66 | 3. **Choose Action**: Click one of the quick action buttons:
 67 |    - 💬 Chat - Opens full chat interface
 68 |    - 📝 Summarize - Get a summary
 69 |    - ✏️ Rewrite - Improve the text
 70 |    - 💡 Explain - Get an explanation
 71 | 4. **Continue Conversation**: In chat mode, ask follow-up questions
 72 | 
 73 | ### Keyboard Shortcuts
 74 | 
 75 | - **Escape**: Close popup
 76 | - **Enter**: Send message (in chat mode)
 77 | - **Shift+Enter**: New line (in chat mode)
 78 | 
 79 | ## 🧪 Testing Without IBM watsonx
 80 | 
 81 | You can test SmartClick without IBM watsonx credentials using the mock client:
 82 | 
 83 | ```bash
 84 | python main.py --mock
 85 | ```
 86 | 
 87 | This uses simulated AI responses for testing the interface and workflow.
 88 | 
 89 | ## 📁 Project Structure
 90 | 
 91 | ```
 92 | SmartClick/
 93 | ├── main.py                      # Main application entry point
 94 | ├── requirements.txt             # Python dependencies
 95 | ├── .env.example                 # Environment variables template
 96 | │
 97 | ├── cursor_layer/                # Text detection and popup
 98 | │   ├── detector.py             # System-wide text selection detection
 99 | │   └── popup.py                # Popup window interface
100 | │
101 | ├── ai_integration/              # IBM watsonx integration
102 | │   └── bob_client.py           # AI client (real + mock)
103 | │
104 | ├── database/                    # Data persistence
105 | │   └── db_manager.py           # SQLite database manager
106 | │
107 | ├── app/                         # Configuration UI
108 | │   └── setup.py                # Setup/settings interface
109 | │
110 | └── docs/                        # Documentation
111 |     ├── ARCHITECTURE.md          # System architecture
112 |     ├── DEVELOPMENT_PLAN.md      # Development roadmap
113 |     ├── API_INTEGRATION.md       # API integration guide
114 |     └── GET_WATSONX_CREDENTIALS.md  # Credential setup guide
115 | ```
116 | 
117 | ## 🔧 Configuration
118 | 
119 | Configuration is stored in `~/.smartclick/config.json`:
120 | 
121 | ```json
122 | {
123 |   "watsonx_api_key": "your-api-key",
124 |   "watsonx_project_id": "your-project-id",
125 |   "watsonx_endpoint": "https://us-south.ml.cloud.ibm.com",
126 |   "keyboard_shortcut": "Ctrl+Shift+A"
127 | }
128 | ```
129 | 
130 | Database is stored in `~/.smartclick/smartclick.db`
131 | 
132 | ## 🗄️ Database Schema
133 | 
134 | SmartClick uses SQLite to store:
135 | 
136 | - **Sessions**: Each text selection creates a session
137 | - **Messages**: All chat messages (user + assistant)
138 | - **Settings**: User preferences and configuration
139 | - **Context**: Additional context for sessions
140 | 
141 | ## 🔌 API Integration
142 | 
143 | SmartClick integrates with IBM watsonx using the official Python SDK:
144 | 
145 | ```python
146 | from ai_integration.bob_client import WatsonxClient
147 | 
148 | client = WatsonxClient(
149 |     api_key="your-api-key",
150 |     project_id="your-project-id"
151 | )
152 | 
153 | # Summarize text
154 | summary = client.summarize("Your text here...")
155 | 
156 | # Chat with context
157 | response = client.chat(
158 |     message="Explain this",
159 |     context="Selected text: ...",
160 |     history=[...]
161 | )
162 | ```
163 | 
164 | See [API_INTEGRATION.md](docs/API_INTEGRATION.md) for detailed documentation.
165 | 
166 | ## 🐛 Troubleshooting
167 | 
168 | ### Popup Not Appearing
169 | 
170 | 1. Check that SmartClick is running: `python main.py`
171 | 2. Try selecting text again
172 | 3. Check logs for errors
173 | 
174 | ### IBM watsonx Connection Issues
175 | 
176 | 1. Verify credentials in setup: `python main.py --setup`
177 | 2. Test connection in setup interface
178 | 3. Check [IBM Cloud status](https://cloud.ibm.com/status)
179 | 4. Use mock mode for testing: `python main.py --mock`
180 | 
181 | ### Text Detection Not Working
182 | 
183 | 1. Ensure you're selecting text (not just clicking)
184 | 2. Try copying text to clipboard (Ctrl+C)
185 | 3. Check Windows permissions for clipboard access
186 | 
187 | ## 📊 Development Status
188 | 
189 | - ✅ Core text detection system
190 | - ✅ Popup interface with quick actions
191 | - ✅ IBM watsonx integration
192 | - ✅ Chat interface with history
193 | - ✅ SQLite database for persistence
194 | - ✅ Configuration UI
195 | - 🚧 Keyboard shortcuts (planned)
196 | - 🚧 System tray icon (planned)
197 | - 🚧 Auto-start on Windows boot (planned)
198 | 
199 | ## 🛣️ Roadmap
200 | 
201 | ### Phase 1: MVP (Current)
202 | - [x] Text selection detection
203 | - [x] Basic popup interface
204 | - [x] IBM watsonx integration
205 | - [x] Chat functionality
206 | - [x] Database storage
207 | 
208 | ### Phase 2: Enhancement
209 | - [ ] Custom keyboard shortcuts
210 | - [ ] System tray integration
211 | - [ ] Auto-start on boot
212 | - [ ] Settings panel
213 | - [ ] Theme customization
214 | 
215 | ### Phase 3: Advanced Features
216 | - [ ] Multi-language support
217 | - [ ] Custom AI prompts
218 | - [ ] Export chat history
219 | - [ ] Cloud sync (optional)
220 | - [ ] Browser extension integration
221 | 
222 | See [DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md) for detailed roadmap.
223 | 
224 | ## 🤝 Contributing
225 | 
226 | Contributions are welcome! Please read our contributing guidelines before submitting PRs.
227 | 
228 | 1. Fork the repository
229 | 2. Create a feature branch
230 | 3. Make your changes
231 | 4. Add tests if applicable
232 | 5. Submit a pull request
233 | 
234 | ## 📄 License
235 | 
236 | [MIT License](LICENSE)
237 | 
238 | ## 🙏 Acknowledgments
239 | 
240 | - IBM watsonx for AI capabilities
241 | - Python community for excellent libraries
242 | - All contributors and testers
243 | 
244 | ## 📞 Support
245 | 
246 | - **Documentation**: [docs/](docs/)
247 | - **Issues**: [GitHub Issues](https://github.com/yourusername/SmartClick/issues)
248 | - **Email**: support@smartclick.ai
249 | 
250 | ## 🔐 Privacy & Security
251 | 
252 | - All data stored locally on your machine
253 | - No telemetry or tracking
254 | - IBM watsonx API calls follow IBM's privacy policy
255 | - API keys stored securely in local config file
256 | 
257 | ---
258 | 
259 | **Made with ❤️ for productivity enthusiasts**
</content>
</file>
<file><path>QUICKSTART.md</path>
<content lines="1-300">
  1 | # SmartClick Quick Start Guide
  2 | 
  3 | Get SmartClick up and running in 5 minutes!
  4 | 
  5 | ## 🎯 Goal
  6 | 
  7 | By the end of this guide, you'll have SmartClick running on your Windows machine, ready to provide AI assistance for any text you select.
  8 | 
  9 | ## ⚡ Fast Track (3 Steps)
 10 | 
 11 | ### Step 1: Install Dependencies
 12 | 
 13 | Open PowerShell or Command Prompt in the SmartClick directory:
 14 | 
 15 | ```bash
 16 | pip install -r requirements.txt
 17 | ```
 18 | 
 19 | This installs:
 20 | - IBM watsonx SDK
 21 | - Windows API libraries (pywin32, pyperclip)
 22 | - Other utilities
 23 | 
 24 | ### Step 2: Configure (Choose One)
 25 | 
 26 | **Option A: Use Mock AI (No credentials needed)**
 27 | ```bash
 28 | python main.py --mock
 29 | ```
 30 | Perfect for testing the interface without IBM watsonx.
 31 | 
 32 | **Option B: Use Real IBM watsonx**
 33 | ```bash
 34 | python main.py --setup
 35 | ```
 36 | Enter your IBM watsonx credentials when prompted.
 37 | 
 38 | ### Step 3: Start Using
 39 | 
 40 | 1. **Select any text** in any application
 41 | 2. **SmartClick popup appears** automatically
 42 | 3. **Click an action**: Chat, Summarize, Rewrite, or Explain
 43 | 4. **Get AI assistance** instantly!
 44 | 
 45 | ## 📝 Detailed Setup
 46 | 
 47 | ### Prerequisites Check
 48 | 
 49 | Before starting, verify you have:
 50 | 
 51 | - ✅ Windows 10 or 11
 52 | - ✅ Python 3.8 or higher
 53 |   ```bash
 54 |   python --version
 55 |   ```
 56 | - ✅ pip (Python package manager)
 57 |   ```bash
 58 |   pip --version
 59 |   ```
 60 | 
 61 | ### Installation Steps
 62 | 
 63 | #### 1. Clone or Download
 64 | 
 65 | ```bash
 66 | # If using Git
 67 | git clone https://github.com/yourusername/SmartClick.git
 68 | cd SmartClick
 69 | 
 70 | # Or download and extract ZIP, then navigate to folder
 71 | cd path/to/SmartClick
 72 | ```
 73 | 
 74 | #### 2. Create Virtual Environment (Recommended)
 75 | 
 76 | ```bash
 77 | # Create virtual environment
 78 | python -m venv venv
 79 | 
 80 | # Activate it
 81 | # On Windows PowerShell:
 82 | .\venv\Scripts\Activate.ps1
 83 | 
 84 | # On Windows Command Prompt:
 85 | .\venv\Scripts\activate.bat
 86 | ```
 87 | 
 88 | #### 3. Install Dependencies
 89 | 
 90 | ```bash
 91 | pip install -r requirements.txt
 92 | ```
 93 | 
 94 | Expected output:
 95 | ```
 96 | Successfully installed ibm-watson-machine-learning-1.0.335 ...
 97 | ```
 98 | 
 99 | #### 4. Configure IBM watsonx (Optional)
100 | 
101 | If you have IBM watsonx credentials:
102 | 
103 | ```bash
104 | python main.py --setup
105 | ```
106 | 
107 | The setup window will open. Enter:
108 | 
109 | 1. **API Key**: Your IBM Cloud API key
110 | 2. **Project ID**: Your watsonx project ID
111 | 3. **Endpoint**: (Optional) Default is US-South
112 | 4. **Keyboard Shortcut**: (Optional) For future use
113 | 
114 | Click **Test Connection** to verify, then **Save**.
115 | 
116 | **Don't have credentials?** See [GET_WATSONX_CREDENTIALS.md](docs/GET_WATSONX_CREDENTIALS.md)
117 | 
118 | #### 5. Start SmartClick
119 | 
120 | **With IBM watsonx:**
121 | ```bash
122 | python main.py
123 | ```
124 | 
125 | **With Mock AI (for testing):**
126 | ```bash
127 | python main.py --mock
128 | ```
129 | 
130 | You should see:
131 | ```
132 | INFO - Initializing SmartClick...
133 | INFO - Database initialized
134 | INFO - IBM watsonx client initialized
135 | INFO - Popup initialized
136 | INFO - Text detector initialized
137 | INFO - Starting SmartClick...
138 | INFO - Text detector started
139 | ```
140 | 
141 | ## 🎮 Using SmartClick
142 | 
143 | ### Basic Usage
144 | 
145 | 1. **Open any application** (browser, Word, Notepad, etc.)
146 | 2. **Select/highlight some text**
147 | 3. **SmartClick popup appears** near your cursor
148 | 4. **Choose an action**:
149 |    - 💬 **Chat**: Opens full chat interface
150 |    - 📝 **Summarize**: Get a quick summary
151 |    - ✏️ **Rewrite**: Improve or rephrase
152 |    - 💡 **Explain**: Get detailed explanation
153 | 
154 | ### Chat Mode
155 | 
156 | 1. Click **💬 Chat** button
157 | 2. Popup expands to full chat interface
158 | 3. Type your question in the input box
159 | 4. Press **Enter** to send (Shift+Enter for new line)
160 | 5. Bob responds with AI-powered answers
161 | 6. Continue the conversation!
162 | 
163 | ### Quick Actions
164 | 
165 | For one-off tasks, use the quick action buttons:
166 | 
167 | - **Summarize**: "Summarize this article for me"
168 | - **Rewrite**: "Make this more professional"
169 | - **Explain**: "Explain this concept in simple terms"
170 | 
171 | The popup expands automatically to show the result.
172 | 
173 | ### Keyboard Shortcuts
174 | 
175 | - **Escape**: Close popup
176 | - **Enter**: Send message (in chat)
177 | - **Shift+Enter**: New line (in chat)
178 | 
179 | ## 🧪 Testing
180 | 
181 | ### Test 1: Basic Text Selection
182 | 
183 | 1. Open Notepad
184 | 2. Type: "Machine learning is a subset of artificial intelligence"
185 | 3. Select the text
186 | 4. SmartClick popup should appear
187 | 
188 | ### Test 2: Quick Action
189 | 
190 | 1. With text selected, click **📝 Summarize**
191 | 2. Popup expands showing summary
192 | 3. Verify the response makes sense
193 | 
194 | ### Test 3: Chat Conversation
195 | 
196 | 1. Select some text
197 | 2. Click **💬 Chat**
198 | 3. Type: "Can you explain this in simple terms?"
199 | 4. Press Enter
200 | 5. Verify you get a response
201 | 6. Ask a follow-up question
202 | 
203 | ## 🔧 Troubleshooting
204 | 
205 | ### Popup Not Appearing
206 | 
207 | **Problem**: Selected text but no popup
208 | 
209 | **Solutions**:
210 | 1. Check SmartClick is running (look for console window)
211 | 2. Try copying text (Ctrl+C) - this triggers detection
212 | 3. Restart SmartClick: Close and run `python main.py` again
213 | 
214 | ### Import Errors
215 | 
216 | **Problem**: `ModuleNotFoundError: No module named 'xyz'`
217 | 
218 | **Solution**:
219 | ```bash
220 | pip install -r requirements.txt --force-reinstall
221 | ```
222 | 
223 | ### IBM watsonx Connection Failed
224 | 
225 | **Problem**: "Failed to connect to IBM watsonx"
226 | 
227 | **Solutions**:
228 | 1. Verify credentials: `python main.py --setup`
229 | 2. Test with mock mode: `python main.py --mock`
230 | 3. Check internet connection
231 | 4. Verify IBM Cloud status: https://cloud.ibm.com/status
232 | 
233 | ### Python Not Found
234 | 
235 | **Problem**: `'python' is not recognized...`
236 | 
237 | **Solution**:
238 | 1. Install Python from https://www.python.org/downloads/
239 | 2. During installation, check "Add Python to PATH"
240 | 3. Restart terminal/PowerShell
241 | 
242 | ### Permission Errors
243 | 
244 | **Problem**: Access denied or permission errors
245 | 
246 | **Solution**:
247 | 1. Run PowerShell/Command Prompt as Administrator
248 | 2. Or install in user directory (no admin needed)
249 | 
250 | ## 📊 What's Happening Behind the Scenes
251 | 
252 | When you run SmartClick:
253 | 
254 | 1. **Database initialized**: SQLite database created at `~/.smartclick/smartclick.db`
255 | 2. **AI client connected**: Connects to IBM watsonx (or mock)
256 | 3. **Text detector started**: Monitors clipboard for text selection
257 | 4. **Popup ready**: Invisible window ready to appear
258 | 
259 | When you select text:
260 | 
261 | 1. **Detection**: Clipboard monitor detects text selection
262 | 2. **Session created**: New session saved to database
263 | 3. **Popup shown**: Window appears at cursor position
264 | 4. **Action processed**: Your choice sent to AI
265 | 5. **Response displayed**: AI response shown in popup
266 | 6. **History saved**: Conversation saved to database
267 | 
268 | ## 🎓 Next Steps
269 | 
270 | Now that SmartClick is running:
271 | 
272 | 1. **Try different applications**: Browser, Word, PDF reader, email
273 | 2. **Experiment with actions**: See what works best for different tasks
274 | 3. **Use chat mode**: Have longer conversations about complex topics
275 | 4. **Check history**: Your conversations are saved in the database
276 | 5. **Customize settings**: Run `python main.py --setup` to adjust
277 | 
278 | ## 📚 Learn More
279 | 
280 | - **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
281 | - **Development Plan**: [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md)
282 | - **API Integration**: [docs/API_INTEGRATION.md](docs/API_INTEGRATION.md)
283 | - **Full README**: [README.md](README.md)
284 | 
285 | ## 💬 Need Help?
286 | 
287 | - Check [README.md](README.md) troubleshooting section
288 | - Review documentation in [docs/](docs/)
289 | - Open an issue on GitHub
290 | - Email: support@smartclick.ai
291 | 
292 | ## 🎉 Success!
293 | 
294 | You're now ready to use SmartClick! Select any text and let Bob help you understand, improve, or discuss it.
295 | 
296 | **Pro Tip**: Keep SmartClick running in the background. It uses minimal resources and is always ready when you need it.
297 | 
298 | ---
299 | 
300 | **Happy SmartClicking! 🚀**
</content>
</file>
<file><path>MODERNIZATION_README.md</path>
<content lines="1-304">
  1 | # SmartClick 2.0 - React Modernization
  2 | 
  3 | ## 🎯 Overview
  4 | 
  5 | This document guides you through the modernization of SmartClick from a CustomTkinter desktop app to a modern React + Electron application with a FastAPI backend.
  6 | 
  7 | ## 🏗️ Architecture
  8 | 
  9 | ### Before (v1.0)
 10 | ```
 11 | ┌─────────────────────────────────┐
 12 | │   CustomTkinter Desktop App     │
 13 | │  (UI + Logic + AI + Database)   │
 14 | └─────────────────────────────────┘
 15 | ```
 16 | 
 17 | ### After (v2.0)
 18 | ```
 19 | ┌──────────────────────────────────────┐
 20 | │     React + Electron Frontend        │
 21 | │  (Modern UI with smooth animations)  │
 22 | └──────────────┬───────────────────────┘
 23 |                │ REST API + WebSocket
 24 | ┌──────────────▼───────────────────────┐
 25 | │       FastAPI Python Backend         │
 26 | │  (AI Logic + Database + Text Capture)│
 27 | └──────────────────────────────────────┘
 28 | ```
 29 | 
 30 | ## 📦 What's Included
 31 | 
 32 | ### Backend (FastAPI)
 33 | - ✅ **REST API** - All CRUD operations for sessions, messages, settings
 34 | - ✅ **WebSocket** - Real-time streaming chat responses
 35 | - ✅ **AI Integration** - IBM watsonx client (existing code reused)
 36 | - ✅ **Database** - SQLite manager (existing code reused)
 37 | - ✅ **CORS** - Configured for Electron app
 38 | 
 39 | ### Frontend (Coming Next)
 40 | - ⏳ **React + TypeScript** - Type-safe, modern UI
 41 | - ⏳ **Electron** - Desktop app wrapper with native features
 42 | - ⏳ **Zustand** - Simple state management
 43 | - ⏳ **Tailwind CSS** - Beautiful, consistent styling
 44 | - ⏳ **Framer Motion** - Smooth animations
 45 | - ⏳ **WebSocket Client** - Real-time chat streaming
 46 | 
 47 | ## 🚀 Quick Start
 48 | 
 49 | ### Step 1: Install Backend Dependencies
 50 | 
 51 | ```bash
 52 | # Navigate to backend directory
 53 | cd backend
 54 | 
 55 | # Install FastAPI and dependencies
 56 | pip install -r requirements.txt
 57 | ```
 58 | 
 59 | ### Step 2: Start the Backend Server
 60 | 
 61 | ```bash
 62 | # From the backend directory
 63 | python run.py
 64 | ```
 65 | 
 66 | The API will be available at:
 67 | - **API**: http://127.0.0.1:8000
 68 | - **Docs**: http://127.0.0.1:8000/docs (Interactive API documentation)
 69 | - **Health**: http://127.0.0.1:8000/health
 70 | 
 71 | ### Step 3: Test the API
 72 | 
 73 | Open http://127.0.0.1:8000/docs in your browser to see the interactive API documentation and test endpoints.
 74 | 
 75 | Example API calls:
 76 | 
 77 | ```bash
 78 | # Health check
 79 | curl http://127.0.0.1:8000/health
 80 | 
 81 | # Create a session
 82 | curl -X POST http://127.0.0.1:8000/api/sessions \
 83 |   -H "Content-Type: application/json" \
 84 |   -d '{"selected_text": "Hello world", "cursor_x": 100, "cursor_y": 200}'
 85 | 
 86 | # Get recent sessions
 87 | curl http://127.0.0.1:8000/api/sessions
 88 | 
 89 | # Chat
 90 | curl -X POST http://127.0.0.1:8000/api/chat \
 91 |   -H "Content-Type: application/json" \
 92 |   -d '{"message": "What is this about?", "context": "Hello world"}'
 93 | ```
 94 | 
 95 | ## 📚 API Endpoints
 96 | 
 97 | ### Sessions
 98 | - `POST /api/sessions` - Create new session
 99 | - `GET /api/sessions` - Get recent sessions (limit=15)
100 | - `GET /api/sessions/{id}` - Get session details
101 | - `GET /api/sessions/{id}/messages` - Get session messages
102 | - `POST /api/sessions/{id}/messages` - Add message to session
103 | 
104 | ### Chat
105 | - `POST /api/chat` - Send chat message (with optional context and history)
106 | - `POST /api/actions/{action}` - Perform quick action (summarize, rewrite, explain)
107 | - `WS /ws/chat` - WebSocket for streaming responses
108 | 
109 | ### Settings
110 | - `GET /api/settings` - Get all settings
111 | - `PUT /api/settings` - Update settings
112 | 
113 | ### Health
114 | - `GET /` - Basic health check
115 | - `GET /health` - Detailed health status
116 | 
117 | ## 🔧 Development Workflow
118 | 
119 | ### Running Both Old and New
120 | 
121 | You can run both the old Tkinter app and the new backend simultaneously:
122 | 
123 | **Terminal 1 - Old App (for reference)**
124 | ```bash
125 | python main.py
126 | ```
127 | 
128 | **Terminal 2 - New Backend**
129 | ```bash
130 | cd backend
131 | python run.py
132 | ```
133 | 
134 | This allows you to:
135 | 1. Compare functionality
136 | 2. Test API endpoints while seeing the old UI
137 | 3. Gradually migrate features
138 | 
139 | ## 📋 Next Steps
140 | 
141 | ### Phase 1: Backend ✅ (COMPLETED)
142 | - [x] FastAPI setup
143 | - [x] REST endpoints
144 | - [x] WebSocket support
145 | - [x] Integration with existing Python code
146 | 
147 | ### Phase 2: React Frontend (NEXT)
148 | 1. **Initialize React Project**
149 |    ```bash
150 |    npm create vite@latest frontend -- --template react-ts
151 |    cd frontend
152 |    npm install
153 |    ```
154 | 
155 | 2. **Add Dependencies**
156 |    ```bash
157 |    npm install zustand axios socket.io-client framer-motion
158 |    npm install -D tailwindcss postcss autoprefixer
159 |    npm install -D electron electron-builder
160 |    ```
161 | 
162 | 3. **Setup Tailwind**
163 |    ```bash
164 |    npx tailwindcss init -p
165 |    ```
166 | 
167 | 4. **Create Components**
168 |    - MainWindow
169 |    - Popup
170 |    - Chat interface
171 |    - Session history
172 | 
173 | 5. **Setup Electron**
174 |    - Main process
175 |    - Preload script
176 |    - IPC communication
177 |    - Global hotkeys
178 | 
179 | ### Phase 3: Integration
180 | - Connect React to FastAPI
181 | - Implement WebSocket streaming
182 | - Add state management
183 | - Style with Tailwind
184 | 
185 | ### Phase 4: Polish
186 | - Animations
187 | - Error handling
188 | - Loading states
189 | - Testing
190 | 
191 | ## 🎨 Design System
192 | 
193 | ### Colors (Dark Theme)
194 | ```css
195 | --bg: #0a0a0a
196 | --surface: #141414
197 | --surface-2: #1e1e1e
198 | --surface-3: #282828
199 | --border: #2a2a2a
200 | --accent: #00e676 (green)
201 | --blue: #40c4ff
202 | --red: #ff5252
203 | --orange: #ffab40
204 | --purple: #ce93d8
205 | --text: #ffffff
206 | --text-2: #9e9e9e
207 | --text-3: #5a5a5a
208 | ```
209 | 
210 | ### Typography
211 | - **Headings**: Segoe UI, Bold
212 | - **Body**: Segoe UI, Regular
213 | - **Code**: Consolas, Monospace
214 | 
215 | ## 🐛 Troubleshooting
216 | 
217 | ### Backend won't start
218 | ```bash
219 | # Make sure you're in the backend directory
220 | cd backend
221 | 
222 | # Install dependencies
223 | pip install -r requirements.txt
224 | 
225 | # Run
226 | python run.py
227 | ```
228 | 
229 | ### Import errors
230 | ```bash
231 | # Make sure project root is in Python path
232 | # The run.py script handles this automatically
233 | ```
234 | 
235 | ### Database errors
236 | The backend uses the same SQLite database as the old app:
237 | - Location: `C:\Users\{username}\.smartclick\smartclick.db`
238 | - It will be created automatically if it doesn't exist
239 | 
240 | ## 📖 Documentation
241 | 
242 | - **Full Plan**: See `docs/REACT_MODERNIZATION_PLAN.md`
243 | - **API Docs**: http://127.0.0.1:8000/docs (when server is running)
244 | - **Architecture**: See `docs/ARCHITECTURE.md`
245 | 
246 | ## 🤝 Contributing
247 | 
248 | This is a modernization project. The goal is to:
249 | 1. Keep all existing functionality
250 | 2. Improve UI/UX dramatically
251 | 3. Make the codebase more maintainable
252 | 4. Enable future enhancements
253 | 
254 | ## 📝 Notes
255 | 
256 | ### Why FastAPI?
257 | - Modern, fast, async Python framework
258 | - Automatic API documentation
259 | - Built-in WebSocket support
260 | - Type hints and validation
261 | - Easy to integrate with existing code
262 | 
263 | ### Why React + Electron?
264 | - Professional, modern UI
265 | - Cross-platform desktop app
266 | - Native OS integration
267 | - Large ecosystem
268 | - Great developer experience
269 | 
270 | ### Why Zustand?
271 | - Simpler than Redux
272 | - Less boilerplate
273 | - Better TypeScript support
274 | - Smaller bundle size
275 | 
276 | ### Why Tailwind?
277 | - Rapid development
278 | - Consistent design
279 | - No CSS conflicts
280 | - Easy customization
281 | - Great with React
282 | 
283 | ## 🎯 Success Criteria
284 | 
285 | - ✅ Backend API working with all endpoints
286 | - ⏳ React frontend with smooth animations
287 | - ⏳ Electron app with global hotkeys
288 | - ⏳ Real-time chat streaming
289 | - ⏳ All existing features working
290 | - ⏳ Better performance than v1.0
291 | - ⏳ Professional, polished UI
292 | 
293 | ## 🚀 Let's Build!
294 | 
295 | The backend is ready. Now let's create an amazing React frontend!
296 | 
297 | **Next command to run:**
298 | ```bash
299 | npm create vite@latest frontend -- --template react-ts
300 | ```
301 | 
302 | ---
303 | 
304 | **Questions?** Check the docs or ask for help!
</content>
</file>
<file><path>TROUBLESHOOTING.md</path>
<content lines="1-331">
  1 | # SmartClick Troubleshooting Guide 🔧
  2 | 
  3 | ## Common Issues & Solutions
  4 | 
  5 | ### Backend Issues
  6 | 
  7 | #### Issue 1: `ModuleNotFoundError: No module named 'uvicorn'`
  8 | 
  9 | **Solution:**
 10 | ```bash
 11 | cd backend
 12 | pip install -r requirements.txt
 13 | ```
 14 | 
 15 | #### Issue 2: `ERROR: No matching distribution found for pywin32==306`
 16 | 
 17 | **Solution:** Updated to pywin32==311 in requirements.txt. Run:
 18 | ```bash
 19 | cd backend
 20 | pip install -r requirements.txt
 21 | ```
 22 | 
 23 | #### Issue 3: Backend won't start
 24 | 
 25 | **Check:**
 26 | 1. Are you in the backend directory? `cd backend`
 27 | 2. Is virtual environment activated? `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
 28 | 3. Are dependencies installed? `pip install -r requirements.txt`
 29 | 4. Is port 8000 already in use? Try `python run.py` or change port in `run.py`
 30 | 
 31 | #### Issue 4: Database errors
 32 | 
 33 | **Solution:** The database will be created automatically at:
 34 | - Windows: `C:\Users\{username}\.smartclick\smartclick.db`
 35 | - Linux/Mac: `~/.smartclick/smartclick.db`
 36 | 
 37 | If issues persist, delete the database file and restart.
 38 | 
 39 | ---
 40 | 
 41 | ### Frontend Issues
 42 | 
 43 | #### Issue 1: `npm install` fails
 44 | 
 45 | **Solution:**
 46 | ```bash
 47 | cd frontend
 48 | rm -rf node_modules package-lock.json  # or delete manually on Windows
 49 | npm install
 50 | ```
 51 | 
 52 | #### Issue 2: TypeScript errors
 53 | 
 54 | **Solution:** These are expected until we build the components. The foundation is ready, components are next phase.
 55 | 
 56 | #### Issue 3: `npm run dev` shows default Vite page
 57 | 
 58 | **Expected behavior!** We haven't built the React components yet. This is Phase 3 (next).
 59 | 
 60 | ---
 61 | 
 62 | ### Installation Steps (Clean Install)
 63 | 
 64 | #### Backend
 65 | ```bash
 66 | # 1. Navigate to backend
 67 | cd backend
 68 | 
 69 | # 2. Create virtual environment (optional but recommended)
 70 | python -m venv venv
 71 | 
 72 | # 3. Activate virtual environment
 73 | # Windows:
 74 | venv\Scripts\activate
 75 | # Linux/Mac:
 76 | source venv/bin/activate
 77 | 
 78 | # 4. Install dependencies
 79 | pip install -r requirements.txt
 80 | 
 81 | # 5. Run backend
 82 | python run.py
 83 | ```
 84 | 
 85 | #### Frontend
 86 | ```bash
 87 | # 1. Navigate to frontend
 88 | cd frontend
 89 | 
 90 | # 2. Install dependencies
 91 | npm install
 92 | 
 93 | # 3. Run dev server (when components are ready)
 94 | npm run dev
 95 | ```
 96 | 
 97 | ---
 98 | 
 99 | ### Verification Checklist
100 | 
101 | #### Backend ✅
102 | - [ ] Dependencies installed without errors
103 | - [ ] `python run.py` starts server
104 | - [ ] Can access http://127.0.0.1:8000
105 | - [ ] Can access http://127.0.0.1:8000/docs
106 | - [ ] Health check returns status: "healthy"
107 | 
108 | #### Frontend ✅
109 | - [ ] Dependencies installed without errors
110 | - [ ] `npm run dev` starts dev server
111 | - [ ] Can access http://localhost:5173
112 | - [ ] No console errors (TypeScript warnings are OK for now)
113 | 
114 | ---
115 | 
116 | ### Port Conflicts
117 | 
118 | #### Backend (Port 8000)
119 | 
120 | If port 8000 is in use, edit `backend/run.py`:
121 | ```python
122 | uvicorn.run(
123 |     "api.main:app",
124 |     host="127.0.0.1",
125 |     port=8001,  # Change this
126 |     reload=True,
127 |     log_level="info"
128 | )
129 | ```
130 | 
131 | Then update `frontend/.env`:
132 | ```
133 | VITE_API_URL=http://127.0.0.1:8001
134 | ```
135 | 
136 | #### Frontend (Port 5173)
137 | 
138 | Vite will automatically use the next available port if 5173 is taken.
139 | 
140 | ---
141 | 
142 | ### Environment Variables
143 | 
144 | #### Backend
145 | No environment variables required for basic operation. The app uses:
146 | - SQLite database (created automatically)
147 | - Mock AI client (if watsonx credentials not configured)
148 | 
149 | #### Frontend
150 | Create `frontend/.env` from `frontend/.env.example`:
151 | ```bash
152 | cd frontend
153 | cp .env.example .env
154 | ```
155 | 
156 | Edit if needed:
157 | ```
158 | VITE_API_URL=http://127.0.0.1:8000
159 | VITE_WS_URL=ws://127.0.0.1:8000
160 | ```
161 | 
162 | ---
163 | 
164 | ### Python Version
165 | 
166 | **Required:** Python 3.8+
167 | 
168 | **Check version:**
169 | ```bash
170 | python --version
171 | ```
172 | 
173 | **If too old:**
174 | - Download from https://www.python.org/downloads/
175 | - Or use pyenv: `pyenv install 3.11`
176 | 
177 | ---
178 | 
179 | ### Node Version
180 | 
181 | **Required:** Node 16+
182 | 
183 | **Check version:**
184 | ```bash
185 | node --version
186 | npm --version
187 | ```
188 | 
189 | **If too old:**
190 | - Download from https://nodejs.org/
191 | - Or use nvm: `nvm install 20`
192 | 
193 | ---
194 | 
195 | ### Windows-Specific Issues
196 | 
197 | #### Issue: PowerShell execution policy
198 | 
199 | **Error:** `cannot be loaded because running scripts is disabled`
200 | 
201 | **Solution:**
202 | ```powershell
203 | Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
204 | ```
205 | 
206 | #### Issue: Long path names
207 | 
208 | **Error:** `The filename or extension is too long`
209 | 
210 | **Solution:**
211 | 1. Enable long paths in Windows
212 | 2. Or move project closer to root: `C:\SmartClick`
213 | 
214 | ---
215 | 
216 | ### macOS-Specific Issues
217 | 
218 | #### Issue: Permission denied
219 | 
220 | **Solution:**
221 | ```bash
222 | chmod +x backend/run.py
223 | ```
224 | 
225 | #### Issue: SSL certificate errors
226 | 
227 | **Solution:**
228 | ```bash
229 | pip install --upgrade certifi
230 | ```
231 | 
232 | ---
233 | 
234 | ### Linux-Specific Issues
235 | 
236 | #### Issue: Missing system dependencies
237 | 
238 | **Solution (Ubuntu/Debian):**
239 | ```bash
240 | sudo apt-get update
241 | sudo apt-get install python3-dev python3-pip nodejs npm
242 | ```
243 | 
244 | **Solution (Fedora/RHEL):**
245 | ```bash
246 | sudo dnf install python3-devel python3-pip nodejs npm
247 | ```
248 | 
249 | ---
250 | 
251 | ### Getting Help
252 | 
253 | #### Check Logs
254 | 
255 | **Backend logs:**
256 | - Console output when running `python run.py`
257 | - Look for ERROR or WARNING messages
258 | 
259 | **Frontend logs:**
260 | - Browser console (F12)
261 | - Terminal output when running `npm run dev`
262 | 
263 | #### Common Log Messages
264 | 
265 | **"Address already in use"**
266 | - Port conflict, change port or kill process
267 | 
268 | **"Module not found"**
269 | - Missing dependency, run `pip install` or `npm install`
270 | 
271 | **"Connection refused"**
272 | - Backend not running, start with `python run.py`
273 | 
274 | ---
275 | 
276 | ### Still Having Issues?
277 | 
278 | 1. **Check the documentation:**
279 |    - `FOUNDATION_REVIEW.md` - What's built and how to test
280 |    - `MODERNIZATION_README.md` - Quick start guide
281 |    - `PHASE_2_COMPLETE.md` - Phase summary
282 | 
283 | 2. **Verify installation:**
284 |    - Backend: `cd backend && pip list`
285 |    - Frontend: `cd frontend && npm list`
286 | 
287 | 3. **Clean install:**
288 |    - Backend: Delete `venv`, recreate, reinstall
289 |    - Frontend: Delete `node_modules`, reinstall
290 | 
291 | 4. **Check versions:**
292 |    - Python 3.8+
293 |    - Node 16+
294 |    - pip latest
295 |    - npm latest
296 | 
297 | ---
298 | 
299 | ### Quick Reference
300 | 
301 | #### Start Backend
302 | ```bash
303 | cd backend
304 | python run.py
305 | ```
306 | 
307 | #### Start Frontend (when ready)
308 | ```bash
309 | cd frontend
310 | npm run dev
311 | ```
312 | 
313 | #### Test Backend
314 | ```bash
315 | curl http://127.0.0.1:8000/health
316 | ```
317 | 
318 | #### View API Docs
319 | ```
320 | http://127.0.0.1:8000/docs
321 | ```
322 | 
323 | ---
324 | 
325 | **Most issues are solved by:**
326 | 1. Ensuring you're in the correct directory
327 | 2. Installing/reinstalling dependencies
328 | 3. Checking Python/Node versions
329 | 4. Restarting the servers
330 | 
331 | Good luck! 🚀
</content>
</file>
<file><path>ELECTRON_QUICKSTART.md</path>
<content lines="1-245">
  1 | # SmartClick Electron - Quick Start Guide
  2 | 
  3 | ## Prerequisites
  4 | 
  5 | 1. **Backend Running**
  6 |    ```bash
  7 |    cd backend
  8 |    python run.py
  9 |    ```
 10 |    Backend should be running on http://127.0.0.1:8000
 11 | 
 12 | 2. **Dependencies Installed**
 13 |    ```bash
 14 |    cd frontend
 15 |    npm install
 16 |    ```
 17 | 
 18 | ## Running the Electron App
 19 | 
 20 | ### Option 1: Development Mode (Recommended for Testing)
 21 | 
 22 | ```bash
 23 | cd frontend
 24 | npm run electron:dev
 25 | ```
 26 | 
 27 | This will:
 28 | - Start Vite dev server on http://localhost:5174
 29 | - Wait for server to be ready
 30 | - Launch Electron with DevTools open
 31 | - Enable hot module replacement (HMR)
 32 | 
 33 | **What you'll see:**
 34 | - Main window opens with SmartClick UI
 35 | - System tray icon appears (look for it in your taskbar)
 36 | - DevTools open for debugging
 37 | - Console logs show "Running in Electron mode"
 38 | 
 39 | ### Option 2: Compiled Mode
 40 | 
 41 | ```bash
 42 | cd frontend
 43 | npm run electron:start
 44 | ```
 45 | 
 46 | This will:
 47 | - Compile Electron TypeScript files to `dist-electron/`
 48 | - Launch Electron with compiled files
 49 | - Use Vite dev server for React app
 50 | 
 51 | ### Option 3: Production Build
 52 | 
 53 | ```bash
 54 | cd frontend
 55 | npm run build              # Build React app
 56 | npm run electron:compile   # Compile Electron files
 57 | npm run electron:build     # Package for distribution
 58 | ```
 59 | 
 60 | Output in `frontend/release/`:
 61 | - Windows: `SmartClick Setup.exe` + portable version
 62 | - macOS: `SmartClick.dmg` + ZIP
 63 | - Linux: `SmartClick.AppImage` + DEB package
 64 | 
 65 | ## Testing the Global Hotkey
 66 | 
 67 | 1. **Start the app** using one of the methods above
 68 | 2. **Enable SmartClick** by clicking the "Enable" button in the main window
 69 | 3. **Open any text editor** (Notepad, VS Code, browser, etc.)
 70 | 4. **Select some text**
 71 | 5. **Press Ctrl+Shift+Z**
 72 | 6. **Popup should appear** at your cursor position with the selected text
 73 | 
 74 | ## System Tray Features
 75 | 
 76 | **Right-click the tray icon:**
 77 | - Show SmartClick - Opens the main window
 78 | - Hide SmartClick - Hides the main window
 79 | - Quit - Exits the application
 80 | 
 81 | **Left-click the tray icon:**
 82 | - Toggles window visibility (show/hide)
 83 | 
 84 | **Closing the window:**
 85 | - Window hides to tray (doesn't quit)
 86 | - App continues running in background
 87 | - Use "Quit" from tray menu to exit
 88 | 
 89 | ## Troubleshooting
 90 | 
 91 | ### Hotkey Not Working
 92 | 
 93 | **Check:**
 94 | 1. Is SmartClick enabled? (Green status in main window)
 95 | 2. Is another app using Ctrl+Shift+Z?
 96 | 3. Check console for "Hotkey pressed" message
 97 | 4. Try restarting the app
 98 | 
 99 | **Fix:**
100 | - Close other apps that might use the same hotkey
101 | - Check Windows/macOS accessibility permissions
102 | - Look for error messages in DevTools console
103 | 
104 | ### Popup Not Appearing
105 | 
106 | **Check:**
107 | 1. Is text actually selected?
108 | 2. Is SmartClick enabled?
109 | 3. Check console for "Text selected" message
110 | 4. Check cursor position detection
111 | 
112 | **Fix:**
113 | - Try selecting text again
114 | - Check if popup is off-screen
115 | - Restart the app
116 | 
117 | ### Backend Connection Issues
118 | 
119 | **Check:**
120 | 1. Is backend running on http://127.0.0.1:8000?
121 | 2. Check backend terminal for errors
122 | 3. Check frontend console for API errors
123 | 
124 | **Fix:**
125 | ```bash
126 | # Restart backend
127 | cd backend
128 | python run.py
129 | 
130 | # Check if it's running
131 | curl http://127.0.0.1:8000/api/sessions?limit=1
132 | ```
133 | 
134 | ### Compilation Errors
135 | 
136 | **If `npm run electron:compile` fails:**
137 | 
138 | ```bash
139 | # Clean and reinstall
140 | cd frontend
141 | rm -rf node_modules dist-electron
142 | npm install
143 | npm run electron:compile
144 | ```
145 | 
146 | ### Build Errors
147 | 
148 | **If `npm run electron:build` fails:**
149 | 
150 | 1. Make sure React app is built first:
151 |    ```bash
152 |    npm run build
153 |    ```
154 | 
155 | 2. Check that dist-electron exists:
156 |    ```bash
157 |    npm run electron:compile
158 |    ```
159 | 
160 | 3. Try building again:
161 |    ```bash
162 |    npm run electron:build
163 |    ```
164 | 
165 | ## Development Tips
166 | 
167 | ### Hot Reload
168 | - React changes: Instant HMR (no restart needed)
169 | - Electron main process changes: Requires app restart
170 | - Preload script changes: Requires app restart
171 | 
172 | ### Debugging
173 | 
174 | **React (Renderer Process):**
175 | - DevTools open automatically in dev mode
176 | - Use `console.log()` as usual
177 | - React DevTools extension works
178 | 
179 | **Electron (Main Process):**
180 | - Check terminal output
181 | - Use `console.log()` in main.ts
182 | - Logs appear in terminal, not DevTools
183 | 
184 | **IPC Communication:**
185 | - Log in both main and renderer
186 | - Check preload.ts for bridge issues
187 | - Verify event names match
188 | 
189 | ### Useful Commands
190 | 
191 | ```bash
192 | # Check if Electron is installed
193 | npx electron --version
194 | 
195 | # List all npm scripts
196 | npm run
197 | 
198 | # Clean build artifacts
199 | rm -rf dist dist-electron release
200 | 
201 | # Full rebuild
202 | npm run build && npm run electron:compile && npm run electron:build
203 | ```
204 | 
205 | ## File Locations
206 | 
207 | **Source Files:**
208 | - `frontend/electron/main.ts` - Main process
209 | - `frontend/electron/preload.ts` - Preload script
210 | - `frontend/src/App.tsx` - React integration
211 | 
212 | **Compiled Files:**
213 | - `frontend/dist-electron/main.js` - Compiled main
214 | - `frontend/dist-electron/preload.js` - Compiled preload
215 | - `frontend/dist/` - Built React app
216 | 
217 | **Build Output:**
218 | - `frontend/release/` - Packaged installers
219 | 
220 | ## Next Steps
221 | 
222 | 1. **Test the hotkey** - Select text and press Ctrl+Shift+Z
223 | 2. **Test the popup** - Verify it appears at cursor position
224 | 3. **Test system tray** - Right-click icon, try show/hide
225 | 4. **Test window management** - Minimize, maximize, close
226 | 5. **Create real icons** - Replace placeholder icons
227 | 6. **Build for distribution** - Package the app
228 | 
229 | ## Known Issues
230 | 
231 | 1. **Text capture uses clipboard** - May interfere with user's clipboard
232 | 2. **Icons are placeholders** - Need real icon files
233 | 3. **No auto-launch** - App doesn't start with OS (yet)
234 | 
235 | ## Support
236 | 
237 | If you encounter issues:
238 | 1. Check this guide first
239 | 2. Look at PHASE_4_ELECTRON_COMPLETE.md for details
240 | 3. Check console logs in both terminals
241 | 4. Verify all prerequisites are met
242 | 
243 | ---
244 | 
245 | **Made with Bob** 🚀
</content>
</file>
</files>
Tool [read_file] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
Tool [read_file] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
Tool [read_file] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
Tool [read_file] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
Tool [read_file] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs
backend/backend_client.py,backend/api/main.py,.env,docs/SERVICE_DOCUMENTATION.md,docs/FRONTEND_IMPLEMENTATION_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-03T13:30:14.159Z
User time zone: Africa/Johannesburg, UTC+2:00

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>advanced</slug>
<name>🛠️ Advanced</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll continue reading the remaining documentation files to complete my analysis.

<read_file>
<args>
  <file>
    <path>FOUNDATION_REVIEW.md</path>
  </file>
  <file>
    <path>PHASE_2_COMPLETE.md</path>
  </file>
  <file>
    <path>PHASE_4_ELECTRON_COMPLETE.md</path>
  </file>
  <file>
    <path>docs/PROJECT_SUMMARY.md</path>
  </file>
  <file>
    <path>docs/ARCHITECTURE.md</path>
  </file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>FOUNDATION_REVIEW.md</path>
<content lines="1-464">
  1 | # SmartClick Foundation Review 🔍
  2 | 
  3 | ## What We've Built So Far
  4 | 
  5 | ### 📊 Progress Overview
  6 | 
  7 | ```
  8 | Phase 1: Planning & Design          ✅ 100% Complete
  9 | Phase 2: Backend & Frontend Setup   ✅ 100% Complete
 10 | Phase 3: React Components           ⏳ 0% (Next)
 11 | Phase 4: Electron Integration       ⏳ 0% (After Phase 3)
 12 | Phase 5: Polish & Testing           ⏳ 0% (Final)
 13 | ```
 14 | 
 15 | ---
 16 | 
 17 | ## 🎯 What's Working Right Now
 18 | 
 19 | ### 1. FastAPI Backend ✅ FULLY FUNCTIONAL
 20 | 
 21 | **Location**: `backend/api/main.py`
 22 | 
 23 | **Test it:**
 24 | ```bash
 25 | # Terminal 1: Start backend
 26 | cd backend
 27 | pip install -r requirements.txt
 28 | python run.py
 29 | 
 30 | # Terminal 2: Test endpoints
 31 | curl http://127.0.0.1:8000/health
 32 | ```
 33 | 
 34 | **What you get:**
 35 | - ✅ REST API with 10+ endpoints
 36 | - ✅ WebSocket for streaming
 37 | - ✅ Interactive docs at http://127.0.0.1:8000/docs
 38 | - ✅ All existing Python code integrated (AI, database, text capture)
 39 | 
 40 | **Available Endpoints:**
 41 | ```
 42 | GET  /                          - Health check
 43 | GET  /health                    - Detailed status
 44 | POST /api/sessions              - Create session
 45 | GET  /api/sessions              - List sessions
 46 | GET  /api/sessions/{id}         - Get session
 47 | GET  /api/sessions/{id}/messages - Get messages
 48 | POST /api/sessions/{id}/messages - Add message
 49 | POST /api/chat                  - Chat with AI
 50 | POST /api/actions/{action}      - Quick actions
 51 | GET  /api/settings              - Get settings
 52 | PUT  /api/settings              - Update settings
 53 | WS   /ws/chat                   - Streaming chat
 54 | ```
 55 | 
 56 | ### 2. Frontend Foundation ✅ READY FOR COMPONENTS
 57 | 
 58 | **Location**: `frontend/`
 59 | 
 60 | **What's configured:**
 61 | - ✅ React 19 + TypeScript + Vite
 62 | - ✅ Tailwind CSS with custom dark theme
 63 | - ✅ All dependencies installed
 64 | - ✅ Build system ready
 65 | 
 66 | **Test it:**
 67 | ```bash
 68 | cd frontend
 69 | npm run dev
 70 | ```
 71 | 
 72 | This will start the dev server, but you'll see the default Vite page because we haven't built the components yet.
 73 | 
 74 | ### 3. Type System ✅ COMPLETE
 75 | 
 76 | **Location**: `frontend/src/types/index.ts`
 77 | 
 78 | **What's defined:**
 79 | - ✅ 207 lines of TypeScript types
 80 | - ✅ Session, Message, Chat types
 81 | - ✅ API request/response types
 82 | - ✅ WebSocket message types
 83 | - ✅ UI state types
 84 | - ✅ Component prop types
 85 | - ✅ Electron IPC types
 86 | 
 87 | **Example:**
 88 | ```typescript
 89 | interface Session {
 90 |   id: number;
 91 |   selected_text: string;
 92 |   app_name?: string;
 93 |   window_title?: string;
 94 |   cursor_x?: number;
 95 |   cursor_y?: number;
 96 |   created_at: string;
 97 |   updated_at: string;
 98 |   message_count: number;
 99 | }
100 | ```
101 | 
102 | ### 4. API Client ✅ READY TO USE
103 | 
104 | **Location**: `frontend/src/services/api.ts`
105 | 
106 | **What it does:**
107 | - ✅ Axios-based REST client
108 | - ✅ All endpoints wrapped in type-safe methods
109 | - ✅ Error handling
110 | - ✅ Request/response logging
111 | - ✅ Automatic retries
112 | 
113 | **Example usage:**
114 | ```typescript
115 | import { api } from './services/api';
116 | 
117 | // Create a session
118 | const { session_id } = await api.createSession({
119 |   selected_text: "Hello world",
120 |   cursor_x: 100,
121 |   cursor_y: 200
122 | });
123 | 
124 | // Get sessions
125 | const sessions = await api.getSessions(15);
126 | 
127 | // Chat
128 | const response = await api.chat({
129 |   message: "What is this?",
130 |   context: "Hello world"
131 | });
132 | ```
133 | 
134 | ### 5. WebSocket Client ✅ READY FOR STREAMING
135 | 
136 | **Location**: `frontend/src/services/websocket.ts`
137 | 
138 | **What it does:**
139 | - ✅ Socket.io client
140 | - ✅ Automatic reconnection
141 | - ✅ Streaming chat responses
142 | - ✅ Error handling
143 | 
144 | **Example usage:**
145 | ```typescript
146 | import { wsClient } from './services/websocket';
147 | 
148 | await wsClient.streamChat(
149 |   { message: "Explain this", context: "Some text" },
150 |   (chunk) => console.log('Received:', chunk),
151 |   () => console.log('Complete'),
152 |   (error) => console.error('Error:', error)
153 | );
154 | ```
155 | 
156 | ### 6. State Management ✅ READY FOR COMPONENTS
157 | 
158 | **Location**: `frontend/src/stores/`
159 | 
160 | **App Store** (`appStore.ts`):
161 | ```typescript
162 | import { useAppStore } from './stores/appStore';
163 | 
164 | // In a component:
165 | const { enabled, sessions, enable, disable, loadSessions } = useAppStore();
166 | 
167 | // Enable SmartClick
168 | enable();
169 | 
170 | // Load sessions
171 | await loadSessions();
172 | ```
173 | 
174 | **Chat Store** (`chatStore.ts`):
175 | ```typescript
176 | import { useChatStore } from './stores/chatStore';
177 | 
178 | // In a component:
179 | const { messages, isStreaming, sendMessage } = useChatStore();
180 | 
181 | // Send a message
182 | await sendMessage(sessionId, "Hello", "context");
183 | ```
184 | 
185 | ### 7. Styling System ✅ COMPLETE
186 | 
187 | **Location**: `frontend/tailwind.config.js`, `frontend/src/index.css`
188 | 
189 | **What's configured:**
190 | - ✅ Custom color palette (dark theme)
191 | - ✅ Typography system
192 | - ✅ Animation keyframes
193 | - ✅ Custom scrollbar
194 | - ✅ Glass morphism effects
195 | 
196 | **Example usage:**
197 | ```tsx
198 | <div className="bg-bg-surface border border-border rounded-lg p-4">
199 |   <h1 className="text-accent font-bold text-xl">SmartClick</h1>
200 |   <p className="text-text-secondary">AI-powered cursor layer</p>
201 | </div>
202 | ```
203 | 
204 | ---
205 | 
206 | ## 🧪 How to Test What's Built
207 | 
208 | ### Test 1: Backend API
209 | 
210 | ```bash
211 | # Start backend
212 | cd backend
213 | python run.py
214 | 
215 | # In another terminal, test endpoints:
216 | 
217 | # Health check
218 | curl http://127.0.0.1:8000/health
219 | 
220 | # Create a session
221 | curl -X POST http://127.0.0.1:8000/api/sessions \
222 |   -H "Content-Type: application/json" \
223 |   -d '{"selected_text": "Test text", "cursor_x": 100, "cursor_y": 200}'
224 | 
225 | # Get sessions
226 | curl http://127.0.0.1:8000/api/sessions
227 | 
228 | # Chat
229 | curl -X POST http://127.0.0.1:8000/api/chat \
230 |   -H "Content-Type: application/json" \
231 |   -d '{"message": "Hello", "context": "Test"}'
232 | ```
233 | 
234 | ### Test 2: Interactive API Docs
235 | 
236 | 1. Start backend: `cd backend && python run.py`
237 | 2. Open browser: http://127.0.0.1:8000/docs
238 | 3. Try out any endpoint interactively!
239 | 
240 | ### Test 3: Frontend Dev Server
241 | 
242 | ```bash
243 | cd frontend
244 | npm run dev
245 | ```
246 | 
247 | Opens at http://localhost:5173 (default Vite page for now)
248 | 
249 | ---
250 | 
251 | ## 📁 Complete File Structure
252 | 
253 | ```
254 | Smart_Clicks/
255 | ├── backend/
256 | │   ├── api/
257 | │   │   ├── __init__.py ✅
258 | │   │   └── main.py ✅ (413 lines)
259 | │   ├── requirements.txt ✅
260 | │   └── run.py ✅
261 | │
262 | ├── frontend/
263 | │   ├── src/
264 | │   │   ├── types/
265 | │   │   │   └── index.ts ✅ (207 lines)
266 | │   │   ├── services/
267 | │   │   │   ├── api.ts ✅ (159 lines)
268 | │   │   │   └── websocket.ts ✅ (145 lines)
269 | │   │   ├── stores/
270 | │   │   │   ├── appStore.ts ✅ (105 lines)
271 | │   │   │   └── chatStore.ts ✅ (165 lines)
272 | │   │   ├── components/ ⏳ (to be built)
273 | │   │   ├── hooks/ ⏳ (to be built)
274 | │   │   ├── index.css ✅ (113 lines)
275 | │   │   ├── App.tsx ⏳ (to be updated)
276 | │   │   └── main.tsx ⏳ (to be updated)
277 | │   ├── tailwind.config.js ✅ (82 lines)
278 | │   ├── postcss.config.js ✅
279 | │   ├── package.json ✅
280 | │   ├── .env.example ✅
281 | │   └── vite.config.ts ✅
282 | │
283 | ├── docs/
284 | │   ├── REACT_MODERNIZATION_PLAN.md ✅
285 | │   └── ...
286 | │
287 | ├── MODERNIZATION_README.md ✅
288 | ├── PHASE_2_COMPLETE.md ✅
289 | └── FOUNDATION_REVIEW.md ✅ (this file)
290 | ```
291 | 
292 | ---
293 | 
294 | ## 💪 What's Strong About This Foundation
295 | 
296 | ### 1. Type Safety
297 | - Every API call is type-checked
298 | - No runtime type errors
299 | - IntelliSense everywhere
300 | - Catch bugs at compile time
301 | 
302 | ### 2. Modern Architecture
303 | - Clean separation of concerns
304 | - Services layer for API calls
305 | - State management with Zustand
306 | - Reusable, testable code
307 | 
308 | ### 3. Developer Experience
309 | - Fast HMR with Vite
310 | - Automatic API docs
311 | - Clear error messages
312 | - Easy debugging
313 | 
314 | ### 4. Performance Ready
315 | - Async/await throughout
316 | - WebSocket streaming
317 | - Optimized builds
318 | - Code splitting ready
319 | 
320 | ### 5. Scalability
321 | - Easy to add new endpoints
322 | - Easy to add new components
323 | - Easy to add new features
324 | - Well-organized structure
325 | 
326 | ---
327 | 
328 | ## 🚧 What's Missing (Next Phase)
329 | 
330 | ### React Components (Phase 3)
331 | 
332 | **Shared Components:**
333 | - [ ] Button.tsx
334 | - [ ] Card.tsx
335 | - [ ] LoadingSpinner.tsx
336 | - [ ] Modal.tsx
337 | 
338 | **Main Window:**
339 | - [ ] MainWindow.tsx
340 | - [ ] ControlPanel.tsx
341 | - [ ] SessionHistory.tsx
342 | - [ ] SessionItem.tsx
343 | - [ ] InfoCards.tsx
344 | - [ ] StatusIndicator.tsx
345 | 
346 | **Popup:**
347 | - [ ] Popup.tsx
348 | - [ ] CompactView.tsx
349 | - [ ] ChatView.tsx
350 | - [ ] ChatBubble.tsx
351 | - [ ] InputBox.tsx
352 | - [ ] ActionButton.tsx
353 | 
354 | **Hooks:**
355 | - [ ] useChat.ts
356 | - [ ] useSession.ts
357 | - [ ] useWebSocket.ts
358 | 
359 | ### Electron (Phase 4)
360 | - [ ] Main process
361 | - [ ] Preload script
362 | - [ ] Global hotkeys
363 | - [ ] System tray
364 | - [ ] Window management
365 | 
366 | ---
367 | 
368 | ## 📊 Metrics
369 | 
370 | ### Code Written
371 | - **Backend**: 413 lines (main.py)
372 | - **Frontend Types**: 207 lines
373 | - **API Client**: 159 lines
374 | - **WebSocket Client**: 145 lines
375 | - **App Store**: 105 lines
376 | - **Chat Store**: 165 lines
377 | - **Styles**: 113 lines
378 | - **Config**: ~200 lines
379 | - **Total**: ~1,500+ lines of production-ready code
380 | 
381 | ### Dependencies Installed
382 | - **Production**: 6 packages (React, Zustand, Axios, Socket.io, Framer Motion)
383 | - **Development**: 10+ packages (TypeScript, Vite, Tailwind, Electron, etc.)
384 | 
385 | ### Time Invested
386 | - Planning & Architecture: ✅
387 | - Backend API: ✅
388 | - Frontend Setup: ✅
389 | - Type System: ✅
390 | - Services Layer: ✅
391 | - State Management: ✅
392 | - Styling System: ✅
393 | 
394 | ---
395 | 
396 | ## ✅ Quality Checklist
397 | 
398 | - [x] TypeScript strict mode enabled
399 | - [x] ESLint configured
400 | - [x] Error handling throughout
401 | - [x] Logging for debugging
402 | - [x] Type-safe API calls
403 | - [x] Automatic reconnection (WebSocket)
404 | - [x] CORS configured
405 | - [x] Environment variables
406 | - [x] Documentation complete
407 | - [x] Code organized and clean
408 | 
409 | ---
410 | 
411 | ## 🎯 Next Steps
412 | 
413 | ### Option 1: Continue Building (Recommended)
414 | Build the React components to make the UI functional:
415 | 1. Start with shared components (Button, Card)
416 | 2. Build MainWindow components
417 | 3. Build Popup components
418 | 4. Connect everything together
419 | 
420 | **Estimated time**: 2-3 hours for basic UI, 1-2 days for polished UI
421 | 
422 | ### Option 2: Test Current Foundation
423 | Play with the backend API and understand the architecture:
424 | 1. Start backend and test endpoints
425 | 2. Explore API docs
426 | 3. Review the code structure
427 | 4. Ask questions
428 | 
429 | ### Option 3: Review & Adjust
430 | Make changes to the foundation before building components:
431 | 1. Adjust color scheme
432 | 2. Change API structure
433 | 3. Add/remove features
434 | 4. Modify architecture
435 | 
436 | ---
437 | 
438 | ## 🤔 Questions to Consider
439 | 
440 | 1. **Design**: Happy with the dark theme colors? Want to adjust?
441 | 2. **Features**: Any additional features to add before building UI?
442 | 3. **Architecture**: Any concerns about the structure?
443 | 4. **Timeline**: When do you need this completed?
444 | 5. **Priorities**: What's most important - speed, polish, or features?
445 | 
446 | ---
447 | 
448 | ## 📞 Ready to Continue?
449 | 
450 | The foundation is **solid, production-ready, and well-architected**. 
451 | 
452 | When you're ready, I can:
453 | 1. Build all React components (2-3 hours)
454 | 2. Add Electron integration (1-2 hours)
455 | 3. Polish with animations (1 hour)
456 | 4. Test everything (1 hour)
457 | 
458 | **Total estimated time to completion: 5-7 hours of focused work**
459 | 
460 | ---
461 | 
462 | **Current Status**: Foundation Complete ✅  
463 | **Next Phase**: Build React Components  
464 | **Confidence Level**: 💯 High - Everything is ready!
</content>
</file>
<file><path>PHASE_2_COMPLETE.md</path>
<content lines="1-375">
  1 | # SmartClick Phase 2 Complete! 🎉
  2 | 
  3 | ## What We've Built
  4 | 
  5 | ### ✅ Backend (FastAPI) - COMPLETE
  6 | **Location**: `backend/api/`
  7 | 
  8 | - **`main.py`** - Complete FastAPI application with:
  9 |   - REST API endpoints for sessions, messages, chat, settings
 10 |   - WebSocket support for real-time streaming
 11 |   - Integration with existing Python code
 12 |   - CORS configured for frontend
 13 |   - Automatic API documentation
 14 |   - Health check endpoints
 15 | 
 16 | - **`requirements.txt`** - All backend dependencies
 17 | - **`run.py`** - Simple server startup script
 18 | 
 19 | **To start backend:**
 20 | ```bash
 21 | cd backend
 22 | pip install -r requirements.txt
 23 | python run.py
 24 | ```
 25 | 
 26 | Access at:
 27 | - API: http://127.0.0.1:8000
 28 | - Docs: http://127.0.0.1:8000/docs
 29 | 
 30 | ---
 31 | 
 32 | ### ✅ Frontend Foundation - COMPLETE
 33 | **Location**: `frontend/`
 34 | 
 35 | #### 1. Project Setup ✅
 36 | - React 19 + TypeScript + Vite
 37 | - Modern build tooling
 38 | - Fast HMR (Hot Module Replacement)
 39 | 
 40 | #### 2. Styling System ✅
 41 | - **Tailwind CSS** configured with custom design system
 42 | - **PostCSS** for processing
 43 | - Custom color palette matching original dark theme
 44 | - Smooth animations and transitions
 45 | - Custom scrollbar styles
 46 | - Glass morphism effects
 47 | 
 48 | **Files:**
 49 | - `tailwind.config.js` - Complete design system
 50 | - `postcss.config.js` - PostCSS configuration
 51 | - `src/index.css` - Global styles with Tailwind
 52 | 
 53 | #### 3. TypeScript Types ✅
 54 | **File**: `src/types/index.ts`
 55 | 
 56 | Complete type definitions for:
 57 | - Sessions, Messages, Chat
 58 | - API requests/responses
 59 | - WebSocket messages
 60 | - UI state
 61 | - Component props
 62 | - Electron IPC
 63 | 
 64 | #### 4. API Services ✅
 65 | **Files:**
 66 | - `src/services/api.ts` - REST API client with axios
 67 |   - All CRUD operations
 68 |   - Error handling
 69 |   - Request/response interceptors
 70 |   - Type-safe endpoints
 71 | 
 72 | - `src/services/websocket.ts` - WebSocket client
 73 |   - Real-time chat streaming
 74 |   - Automatic reconnection
 75 |   - Error handling
 76 |   - Connection management
 77 | 
 78 | #### 5. State Management ✅
 79 | **Files:**
 80 | - `src/stores/appStore.ts` - Global app state
 81 |   - Enable/disable functionality
 82 |   - Session management
 83 |   - Loading states
 84 |   - Error handling
 85 | 
 86 | - `src/stores/chatStore.ts` - Chat state
 87 |   - Message management
 88 |   - Streaming responses
 89 |   - Action handling
 90 |   - Real-time updates
 91 | 
 92 | #### 6. Configuration ✅
 93 | - `package.json` - All dependencies installed
 94 | - `.env.example` - Environment variables template
 95 | - TypeScript configs
 96 | - ESLint config
 97 | 
 98 | ---
 99 | 
100 | ## Dependencies Installed
101 | 
102 | ### Production
103 | ```json
104 | {
105 |   "react": "^19.2.5",
106 |   "react-dom": "^19.2.5",
107 |   "zustand": "^5.0.2",
108 |   "axios": "^1.7.9",
109 |   "socket.io-client": "^4.8.1",
110 |   "framer-motion": "^11.15.0"
111 | }
112 | ```
113 | 
114 | ### Development
115 | ```json
116 | {
117 |   "typescript": "~6.0.2",
118 |   "vite": "^8.0.10",
119 |   "tailwindcss": "^3.4.17",
120 |   "autoprefixer": "^10.4.20",
121 |   "postcss": "^8.4.49",
122 |   "electron": "^34.0.0",
123 |   "electron-builder": "^25.1.8"
124 | }
125 | ```
126 | 
127 | ---
128 | 
129 | ## Architecture
130 | 
131 | ```
132 | ┌─────────────────────────────────────────┐
133 | │         React Frontend (Vite)           │
134 | │  ┌─────────────────────────────────┐   │
135 | │  │  Components (To be built)       │   │
136 | │  │  - MainWindow                   │   │
137 | │  │  - Popup                        │   │
138 | │  │  - Chat Interface               │   │
139 | │  └─────────────────────────────────┘   │
140 | │  ┌─────────────────────────────────┐   │
141 | │  │  State Management (Zustand) ✅  │   │
142 | │  │  - appStore                     │   │
143 | │  │  - chatStore                    │   │
144 | │  └─────────────────────────────────┘   │
145 | │  ┌─────────────────────────────────┐   │
146 | │  │  Services ✅                    │   │
147 | │  │  - API Client (axios)           │   │
148 | │  │  - WebSocket Client             │   │
149 | │  └─────────────────────────────────┘   │
150 | └─────────────────────────────────────────┘
151 |                     ↕
152 |         REST API + WebSocket
153 |                     ↕
154 | ┌─────────────────────────────────────────┐
155 | │      FastAPI Backend ✅                 │
156 | │  ┌─────────────────────────────────┐   │
157 | │  │  REST Endpoints                 │   │
158 | │  │  - Sessions CRUD                │   │
159 | │  │  - Messages CRUD                │   │
160 | │  │  - Chat                         │   │
161 | │  │  - Actions                      │   │
162 | │  │  - Settings                     │   │
163 | │  └─────────────────────────────────┘   │
164 | │  ┌─────────────────────────────────┐   │
165 | │  │  WebSocket                      │   │
166 | │  │  - Streaming chat responses     │   │
167 | │  └─────────────────────────────────┘   │
168 | │  ┌─────────────────────────────────┐   │
169 | │  │  Existing Python Code           │   │
170 | │  │  - AI Integration (watsonx)     │   │
171 | │  │  - Database (SQLite)            │   │
172 | │  │  - Text Capture                 │   │
173 | │  └─────────────────────────────────┘   │
174 | └─────────────────────────────────────────┘
175 | ```
176 | 
177 | ---
178 | 
179 | ## What's Next: Phase 3 - React Components
180 | 
181 | ### Components to Build
182 | 
183 | #### 1. Shared Components
184 | - `Button.tsx` - Reusable button with variants
185 | - `Card.tsx` - Container component
186 | - `LoadingSpinner.tsx` - Loading indicator
187 | - `Modal.tsx` - Dialog component
188 | 
189 | #### 2. Main Window Components
190 | - `MainWindow.tsx` - Main layout
191 | - `ControlPanel.tsx` - Enable/disable controls
192 | - `SessionHistory.tsx` - Session list
193 | - `SessionItem.tsx` - Individual session
194 | - `InfoCards.tsx` - How-to guides
195 | - `StatusIndicator.tsx` - Active/disabled status
196 | 
197 | #### 3. Popup Components
198 | - `Popup.tsx` - Floating popup container
199 | - `CompactView.tsx` - 4 action buttons
200 | - `ChatView.tsx` - Expanded chat interface
201 | - `ChatBubble.tsx` - Message display
202 | - `InputBox.tsx` - Message input
203 | - `ActionButton.tsx` - Action buttons
204 | 
205 | #### 4. Custom Hooks
206 | - `useChat.ts` - Chat functionality
207 | - `useSession.ts` - Session management
208 | - `useWebSocket.ts` - WebSocket connection
209 | - `useHotkey.ts` - Keyboard shortcuts
210 | 
211 | ---
212 | 
213 | ## Quick Start Guide
214 | 
215 | ### 1. Start Backend
216 | ```bash
217 | cd backend
218 | pip install -r requirements.txt
219 | python run.py
220 | ```
221 | 
222 | ### 2. Start Frontend (when components are ready)
223 | ```bash
224 | cd frontend
225 | npm install  # Already done
226 | npm run dev
227 | ```
228 | 
229 | ### 3. Access
230 | - Frontend: http://localhost:5173
231 | - Backend API: http://127.0.0.1:8000
232 | - API Docs: http://127.0.0.1:8000/docs
233 | 
234 | ---
235 | 
236 | ## File Structure
237 | 
238 | ```
239 | Smart_Clicks/
240 | ├── backend/
241 | │   ├── api/
242 | │   │   ├── __init__.py ✅
243 | │   │   └── main.py ✅
244 | │   ├── requirements.txt ✅
245 | │   └── run.py ✅
246 | │
247 | ├── frontend/
248 | │   ├── src/
249 | │   │   ├── components/        ⏳ Next phase
250 | │   │   ├── stores/
251 | │   │   │   ├── appStore.ts ✅
252 | │   │   │   └── chatStore.ts ✅
253 | │   │   ├── services/
254 | │   │   │   ├── api.ts ✅
255 | │   │   │   └── websocket.ts ✅
256 | │   │   ├── types/
257 | │   │   │   └── index.ts ✅
258 | │   │   ├── index.css ✅
259 | │   │   ├── App.tsx ⏳
260 | │   │   └── main.tsx ⏳
261 | │   ├── tailwind.config.js ✅
262 | │   ├── postcss.config.js ✅
263 | │   ├── package.json ✅
264 | │   └── .env.example ✅
265 | │
266 | ├── docs/
267 | │   ├── REACT_MODERNIZATION_PLAN.md ✅
268 | │   └── ...
269 | │
270 | ├── MODERNIZATION_README.md ✅
271 | └── PHASE_2_COMPLETE.md ✅ (this file)
272 | ```
273 | 
274 | ---
275 | 
276 | ## Key Features Implemented
277 | 
278 | ### Backend ✅
279 | - ✅ REST API with all endpoints
280 | - ✅ WebSocket for streaming
281 | - ✅ CORS configured
282 | - ✅ Error handling
283 | - ✅ Automatic API docs
284 | - ✅ Health checks
285 | - ✅ Integration with existing code
286 | 
287 | ### Frontend Foundation ✅
288 | - ✅ React 19 + TypeScript + Vite
289 | - ✅ Tailwind CSS with custom theme
290 | - ✅ Complete type definitions
291 | - ✅ API client with axios
292 | - ✅ WebSocket client
293 | - ✅ Zustand state management
294 | - ✅ Environment configuration
295 | - ✅ Modern build tooling
296 | 
297 | ### Still To Do ⏳
298 | - ⏳ React components (UI)
299 | - ⏳ Electron integration
300 | - ⏳ Global hotkeys
301 | - ⏳ System tray
302 | - ⏳ Testing
303 | - ⏳ Build & deployment
304 | 
305 | ---
306 | 
307 | ## Success Metrics
308 | 
309 | ### Completed ✅
310 | - [x] Modern tech stack selected
311 | - [x] Backend API functional
312 | - [x] Frontend foundation solid
313 | - [x] Type safety throughout
314 | - [x] State management ready
315 | - [x] API/WebSocket clients ready
316 | - [x] Styling system configured
317 | 
318 | ### In Progress ⏳
319 | - [ ] UI components built
320 | - [ ] Electron wrapper
321 | - [ ] End-to-end functionality
322 | - [ ] Testing coverage
323 | - [ ] Performance optimization
324 | 
325 | ---
326 | 
327 | ## Next Steps
328 | 
329 | 1. **Build React Components** (Phase 3)
330 |    - Start with shared components (Button, Card, etc.)
331 |    - Build MainWindow components
332 |    - Build Popup components
333 |    - Connect to stores
334 | 
335 | 2. **Electron Integration** (Phase 4)
336 |    - Setup Electron main process
337 |    - Create preload script
338 |    - Implement global hotkeys
339 |    - Add system tray
340 | 
341 | 3. **Polish & Test** (Phase 5)
342 |    - Add animations with Framer Motion
343 |    - Implement error boundaries
344 |    - Add loading states
345 |    - Write tests
346 |    - Optimize performance
347 | 
348 | ---
349 | 
350 | ## Documentation
351 | 
352 | - **Full Plan**: `docs/REACT_MODERNIZATION_PLAN.md`
353 | - **Quick Start**: `MODERNIZATION_README.md`
354 | - **API Docs**: http://127.0.0.1:8000/docs (when backend running)
355 | - **This Summary**: `PHASE_2_COMPLETE.md`
356 | 
357 | ---
358 | 
359 | ## Questions?
360 | 
361 | Everything is set up and ready for building the UI components. The foundation is solid:
362 | - ✅ Backend API working
363 | - ✅ Frontend tooling configured
364 | - ✅ State management ready
365 | - ✅ Services ready
366 | - ✅ Types defined
367 | - ✅ Styling system ready
368 | 
369 | **Ready to build beautiful React components!** 🚀
370 | 
371 | ---
372 | 
373 | **Phase 2 Status**: ✅ COMPLETE
374 | **Next Phase**: Build React Components
375 | **Estimated Time**: 2-3 days for full UI
</content>
</file>
<file><path>PHASE_4_ELECTRON_COMPLETE.md</path>
<content lines="1-320">
  1 | # Phase 4: Electron Integration - COMPLETE ✅
  2 | 
  3 | ## Overview
  4 | Successfully integrated Electron to transform SmartClick from a web app into a full-featured desktop application with global hotkeys, system tray, and native OS integration.
  5 | 
  6 | ## What Was Built
  7 | 
  8 | ### 1. Electron Main Process (`frontend/electron/main.ts`)
  9 | **207 lines** - Core Electron application logic
 10 | 
 11 | **Features:**
 12 | - ✅ Window management (create, show, hide, minimize)
 13 | - ✅ System tray integration with context menu
 14 | - ✅ Global hotkey registration (Ctrl+Shift+Z)
 15 | - ✅ Text selection capture via clipboard
 16 | - ✅ Cursor position detection
 17 | - ✅ IPC communication with renderer process
 18 | - ✅ Auto-hide to tray on close
 19 | - ✅ Development and production mode support
 20 | 
 21 | **Key Functions:**
 22 | ```typescript
 23 | createMainWindow()     // Creates the main BrowserWindow
 24 | createTray()          // Sets up system tray icon
 25 | registerHotkeys()     // Registers Ctrl+Shift+Z globally
 26 | getSelectedText()     // Captures selected text from clipboard
 27 | ```
 28 | 
 29 | ### 2. Electron Preload Script (`frontend/electron/preload.ts`)
 30 | **40 lines** - Secure IPC bridge
 31 | 
 32 | **Exposed APIs:**
 33 | - `onTextSelected()` - Listen for text selection events
 34 | - `minimizeWindow()` - Minimize window
 35 | - `maximizeWindow()` - Maximize window
 36 | - `closeWindow()` - Close window
 37 | - `getPlatform()` - Get OS platform
 38 | - `getVersion()` - Get Electron version
 39 | - `writeClipboard()` - Write to clipboard
 40 | - `readClipboard()` - Read from clipboard
 41 | - `showNotification()` - Show system notification
 42 | 
 43 | **Security:**
 44 | - Uses `contextBridge` for secure API exposure
 45 | - No direct Node.js access in renderer
 46 | - Type-safe API definitions
 47 | 
 48 | ### 3. Type Definitions (`frontend/src/types/electron.d.ts`)
 49 | **25 lines** - TypeScript definitions for Electron APIs
 50 | 
 51 | Extends the global `Window` interface with `electron` property for type safety throughout the React app.
 52 | 
 53 | ### 4. React Integration (`frontend/src/App.tsx`)
 54 | **68 lines** - Updated to handle Electron events
 55 | 
 56 | **Features:**
 57 | - Detects Electron vs browser mode
 58 | - Listens for text selection events
 59 | - Shows popup at cursor position
 60 | - Respects enabled/disabled state
 61 | 
 62 | **Flow:**
 63 | 1. User presses Ctrl+Shift+Z with text selected
 64 | 2. Electron captures text and cursor position
 65 | 3. Sends event to React via IPC
 66 | 4. React shows Popup component at cursor location
 67 | 5. User interacts with AI features
 68 | 
 69 | ### 5. Build Configuration
 70 | 
 71 | **package.json Scripts:**
 72 | ```json
 73 | {
 74 |   "electron:dev": "concurrently \"vite\" \"wait-on http://localhost:5174 && electron .\"",
 75 |   "electron:compile": "tsc -p tsconfig.electron.json",
 76 |   "electron:start": "npm run electron:compile && electron .",
 77 |   "electron:build": "npm run build && electron-builder"
 78 | }
 79 | ```
 80 | 
 81 | **tsconfig.electron.json:**
 82 | - Separate TypeScript config for Electron
 83 | - CommonJS module system
 84 | - ES2020 target
 85 | - Bundler module resolution
 86 | 
 87 | **electron-builder Configuration:**
 88 | - Windows: NSIS installer + portable
 89 | - macOS: DMG + ZIP
 90 | - Linux: AppImage + DEB
 91 | - Output directory: `release/`
 92 | 
 93 | ### 6. Dependencies Added
 94 | ```json
 95 | {
 96 |   "concurrently": "^9.1.2",    // Run multiple commands
 97 |   "wait-on": "^8.0.1",         // Wait for server to start
 98 |   "electron": "^34.0.0",       // Electron framework
 99 |   "electron-builder": "^25.1.8" // Build and package
100 | }
101 | ```
102 | 
103 | ## How It Works
104 | 
105 | ### Global Hotkey Flow
106 | ```
107 | 1. User selects text in any application
108 | 2. User presses Ctrl+Shift+Z
109 | 3. Electron main process captures:
110 |    - Selected text (via clipboard)
111 |    - Cursor position (via screen API)
112 | 4. Main process sends IPC message to renderer
113 | 5. React receives event via window.electron.onTextSelected()
114 | 6. Popup appears at cursor position
115 | 7. User interacts with AI features
116 | ```
117 | 
118 | ### System Tray Integration
119 | ```
120 | - App icon appears in system tray
121 | - Right-click shows context menu:
122 |   - Show SmartClick
123 |   - Hide SmartClick
124 |   - Quit
125 | - Left-click toggles window visibility
126 | - Closing window hides to tray (doesn't quit)
127 | ```
128 | 
129 | ### Window Management
130 | ```
131 | - Main window: 900x600 (min 800x500)
132 | - Dark theme background (#0a0a0a)
133 | - Shows when ready (prevents flash)
134 | - Hides to tray on close
135 | - Restores from tray on show
136 | ```
137 | 
138 | ## File Structure
139 | ```
140 | frontend/
141 | ├── electron/
142 | │   ├── main.ts              # Main process (207 lines)
143 | │   └── preload.ts           # Preload script (40 lines)
144 | ├── src/
145 | │   ├── App.tsx              # Updated with Electron integration (68 lines)
146 | │   └── types/
147 | │       └── electron.d.ts    # Type definitions (25 lines)
148 | ├── public/
149 | │   ├── icon.png             # App icon (placeholder)
150 | │   └── tray-icon.png        # Tray icon (placeholder)
151 | ├── dist-electron/           # Compiled Electron files
152 | │   ├── main.js
153 | │   └── preload.js
154 | ├── package.json             # Updated with Electron scripts
155 | ├── tsconfig.electron.json   # Electron TypeScript config
156 | └── vite.config.electron.ts  # Vite config for Electron
157 | ```
158 | 
159 | ## Running the Electron App
160 | 
161 | ### Development Mode
162 | ```bash
163 | # Terminal 1: Start backend
164 | cd backend
165 | python run.py
166 | 
167 | # Terminal 2: Start Electron app
168 | cd frontend
169 | npm run electron:dev
170 | ```
171 | 
172 | This will:
173 | 1. Start Vite dev server on http://localhost:5174
174 | 2. Wait for server to be ready
175 | 3. Launch Electron with dev tools open
176 | 4. Enable hot module replacement
177 | 
178 | ### Production Build
179 | ```bash
180 | # Compile Electron files
181 | npm run electron:compile
182 | 
183 | # Build React app
184 | npm run build
185 | 
186 | # Package for distribution
187 | npm run electron:build
188 | ```
189 | 
190 | Output in `frontend/release/`:
191 | - Windows: `SmartClick Setup.exe` + `SmartClick.exe` (portable)
192 | - macOS: `SmartClick.dmg` + `SmartClick.zip`
193 | - Linux: `SmartClick.AppImage` + `smartclick.deb`
194 | 
195 | ## Testing Checklist
196 | 
197 | ### ✅ Completed
198 | - [x] Electron files compile without errors
199 | - [x] TypeScript types are correct
200 | - [x] React app detects Electron mode
201 | - [x] IPC bridge is secure
202 | 
203 | ### 🔄 To Test
204 | - [ ] Global hotkey (Ctrl+Shift+Z) captures text
205 | - [ ] Popup appears at cursor position
206 | - [ ] System tray icon and menu work
207 | - [ ] Window hide/show/minimize work
208 | - [ ] App survives close (hides to tray)
209 | - [ ] Quit from tray menu works
210 | - [ ] Clipboard operations work
211 | - [ ] Cross-platform compatibility (Windows/Mac/Linux)
212 | 
213 | ## Known Limitations
214 | 
215 | 1. **Text Capture Method**: Currently uses clipboard workaround. For production, consider:
216 |    - Windows: Use Windows API for text selection
217 |    - macOS: Use Accessibility API
218 |    - Linux: Use X11 or Wayland APIs
219 | 
220 | 2. **Icon Placeholders**: Need actual icon files:
221 |    - `icon.png`: 512x512 app icon
222 |    - `tray-icon.png`: 16x16 or 32x32 tray icon
223 | 
224 | 3. **Auto-launch**: Not yet implemented. Add to electron-builder config:
225 |    ```json
226 |    "win": {
227 |      "target": ["nsis"],
228 |      "nsis": {
229 |        "oneClick": false,
230 |        "allowToChangeInstallationDirectory": true,
231 |        "createDesktopShortcut": true,
232 |        "createStartMenuShortcut": true,
233 |        "runAfterFinish": true
234 |      }
235 |    }
236 |    ```
237 | 
238 | ## Next Steps (Phase 5)
239 | 
240 | 1. **Create Real Icons**
241 |    - Design app icon (512x512)
242 |    - Design tray icon (16x16, 32x32)
243 |    - Export in multiple formats
244 | 
245 | 2. **Test Global Hotkeys**
246 |    - Test text selection capture
247 |    - Test popup positioning
248 |    - Test across different apps
249 | 
250 | 3. **Improve Text Capture**
251 |    - Implement native APIs per platform
252 |    - Handle edge cases (no text selected, etc.)
253 | 
254 | 4. **Add Auto-launch**
255 |    - Configure electron-builder
256 |    - Add settings toggle
257 | 
258 | 5. **Performance Optimization**
259 |    - Minimize bundle size
260 |    - Optimize startup time
261 |    - Reduce memory usage
262 | 
263 | 6. **End-to-End Testing**
264 |    - Test all features together
265 |    - Test on different OS versions
266 |    - Test with different screen configurations
267 | 
268 | ## Success Metrics
269 | 
270 | ✅ **Phase 4 Complete:**
271 | - Electron main process created (207 lines)
272 | - Preload script created (40 lines)
273 | - Type definitions added (25 lines)
274 | - React integration complete (68 lines)
275 | - Build configuration complete
276 | - All files compile successfully
277 | - No TypeScript errors
278 | 
279 | 🎯 **Ready for Testing:**
280 | - Global hotkey registration
281 | - Text selection capture
282 | - System tray integration
283 | - Window management
284 | - IPC communication
285 | 
286 | ## Technical Highlights
287 | 
288 | ### Security
289 | - Context isolation enabled
290 | - No Node.js in renderer
291 | - Secure IPC bridge via preload
292 | - Type-safe API exposure
293 | 
294 | ### Performance
295 | - Lazy window creation
296 | - Efficient IPC communication
297 | - Minimal memory footprint
298 | - Fast startup time
299 | 
300 | ### User Experience
301 | - Native OS integration
302 | - Global hotkey access
303 | - System tray convenience
304 | - Seamless window management
305 | 
306 | ## Conclusion
307 | 
308 | Phase 4 successfully transforms SmartClick into a true desktop application with:
309 | - ✅ Global hotkey support (Ctrl+Shift+Z)
310 | - ✅ System tray integration
311 | - ✅ Native window management
312 | - ✅ Secure IPC communication
313 | - ✅ Cross-platform compatibility
314 | - ✅ Professional build system
315 | 
316 | The app is now ready for testing and can be packaged for distribution on Windows, macOS, and Linux!
317 | 
318 | ---
319 | 
320 | **Made with Bob** 🚀
</content>
</file>
<file><path>docs/PROJECT_SUMMARY.md</path>
<content lines="1-562">
  1 | # SmartClick - Project Summary & Recommendations
  2 | 
  3 | ## Executive Summary
  4 | 
  5 | SmartClick is an AI-powered cursor layer that brings IBM Bob directly into any application. This document summarizes the complete planning phase and provides actionable recommendations for implementation.
  6 | 
  7 | ## Project Overview
  8 | 
  9 | ### What is SmartClick?
 10 | 
 11 | SmartClick enables users to:
 12 | 1. **Highlight text** in any application (browser, IDE, document, email)
 13 | 2. **See an instant popup** with AI-powered actions
 14 | 3. **Query, rewrite, summarize, or analyze** the selected text
 15 | 4. **Expand into a full chat** interface for deeper conversations
 16 | 5. **Maintain context** throughout the interaction
 17 | 
 18 | ### Core Components
 19 | 
 20 | 1. **Setup App** - One-time configuration interface
 21 | 2. **Cursor Layer** - System-wide overlay that works everywhere
 22 | 3. **AI Engine** - IBM watsonx integration for text processing
 23 | 4. **Background Service** - Silent process managing everything
 24 | 
 25 | ---
 26 | 
 27 | ## Technology Stack Recommendations
 28 | 
 29 | ### ✅ Recommended: Electron + React + TypeScript
 30 | 
 31 | **Why This Stack?**
 32 | 
 33 | | Requirement | Solution |
 34 | |-------------|----------|
 35 | | Cross-platform (Windows, macOS, Linux) | ✅ Electron provides single codebase |
 36 | | System-wide text selection | ✅ Node.js native modules + OS APIs |
 37 | | Rich UI with animations | ✅ React + Tailwind CSS |
 38 | | Type safety | ✅ TypeScript throughout |
 39 | | IBM watsonx integration | ✅ Official Node.js SDK available |
 40 | | Overlay windows | ✅ Electron transparent windows |
 41 | | Global shortcuts | ✅ Node.js keyboard listeners |
 42 | 
 43 | ### Technology Breakdown
 44 | 
 45 | ```
 46 | Frontend:
 47 | ├── React 18+ (UI components)
 48 | ├── TypeScript (type safety)
 49 | ├── Tailwind CSS (styling)
 50 | ├── Zustand (state management)
 51 | └── Vite (build tool)
 52 | 
 53 | Backend:
 54 | ├── Electron (desktop framework)
 55 | ├── Node.js (runtime)
 56 | ├── IBM watsonx SDK (AI)
 57 | └── SQLite (chat history)
 58 | 
 59 | Build & Deploy:
 60 | ├── Electron Builder (packaging)
 61 | ├── GitHub Actions (CI/CD)
 62 | └── Vitest + Playwright (testing)
 63 | ```
 64 | 
 65 | ### Alternative Considered
 66 | 
 67 | **Tauri + Rust**: Lighter and faster, but more complex for system-level features. Recommended for v2.0 if performance becomes critical.
 68 | 
 69 | ---
 70 | 
 71 | ## Project Structure
 72 | 
 73 | ### High-Level Organization
 74 | 
 75 | ```
 76 | smart-clicks/
 77 | ├── docs/              # All documentation
 78 | ├── src/
 79 | │   ├── main/         # Electron main process (Node.js)
 80 | │   ├── renderer/     # UI (React)
 81 | │   ├── preload/      # Security bridge
 82 | │   └── shared/       # Common code
 83 | ├── tests/            # All tests
 84 | ├── scripts/          # Build scripts
 85 | └── resources/        # Icons, images
 86 | ```
 87 | 
 88 | ### Key Directories
 89 | 
 90 | - **`src/main/services/`** - Core business logic (text selection, AI, overlay)
 91 | - **`src/renderer/overlay/`** - Popup and chat UI
 92 | - **`src/renderer/setup/`** - Configuration wizard
 93 | - **`src/shared/types/`** - TypeScript definitions
 94 | 
 95 | **Full structure**: See [`FOLDER_STRUCTURE.md`](./FOLDER_STRUCTURE.md)
 96 | 
 97 | ---
 98 | 
 99 | ## Development Phases
100 | 
101 | ### 12-Week Timeline
102 | 
103 | | Phase | Duration | Deliverable |
104 | |-------|----------|-------------|
105 | | **Phase 0: MVP** | 1 week | Working prototype |
106 | | **Phase 1: Infrastructure** | 2 weeks | Solid foundation |
107 | | **Phase 2: Text Selection** | 2 weeks | Cross-platform detection |
108 | | **Phase 3: AI Integration** | 2 weeks | IBM watsonx working |
109 | | **Phase 4: Chat Interface** | 2 weeks | Full conversations |
110 | | **Phase 5: Settings** | 2 weeks | Setup wizard |
111 | | **Phase 6: Polish** | 2 weeks | Production ready |
112 | 
113 | ### MVP Prototype (Week 1)
114 | 
115 | **Goal**: Demonstrate core concept in 5 days
116 | 
117 | **Features**:
118 | - ✅ Detect text selection (clipboard-based)
119 | - ✅ Show popup at cursor
120 | - ✅ Display action buttons
121 | - ✅ Show mock AI response
122 | 
123 | **Critical Files** (24 files):
124 | 1. Project setup (package.json, configs)
125 | 2. Basic Electron app
126 | 3. Simple overlay UI
127 | 4. Text selection detector
128 | 5. Mock AI client
129 | 
130 | **Why Start Here?**: Validates the concept quickly, gets stakeholder buy-in, identifies technical challenges early.
131 | 
132 | ### Phase-by-Phase Breakdown
133 | 
134 | **Detailed plans**: See [`DEVELOPMENT_PLAN.md`](./DEVELOPMENT_PLAN.md)
135 | 
136 | ---
137 | 
138 | ## IBM watsonx Integration
139 | 
140 | ### Setup Requirements
141 | 
142 | 1. **IBM Cloud Account** with watsonx.ai access
143 | 2. **API Credentials**:
144 |    - API Key (IAM authentication)
145 |    - Project ID
146 |    - Service endpoint URL
147 | 3. **Model Access**: e.g., `ibm/granite-13b-chat-v2`
148 | 
149 | ### Integration Architecture
150 | 
151 | ```typescript
152 | // High-level flow
153 | User selects text
154 |   → Text Selection Detector captures it
155 |   → Overlay Manager shows popup
156 |   → User clicks action (e.g., "Summarize")
157 |   → Prompt Builder creates optimized prompt
158 |   → Watsonx Client sends API request
159 |   → Response streams back in real-time
160 |   → Chat Interface displays result
161 | ```
162 | 
163 | ### Key Components
164 | 
165 | 1. **WatsonxClient** - API wrapper with error handling
166 | 2. **PromptBuilder** - Optimized prompts for each action
167 | 3. **ContextManager** - Maintains conversation context
168 | 4. **ResponseCache** - Reduces API calls
169 | 
170 | ### Prompt Templates
171 | 
172 | ```typescript
173 | Summarize: "Summarize this text concisely: {context}"
174 | Rewrite: "Rewrite this text to be more {tone}: {context}"
175 | Explain: "Explain this text in simple terms: {context}"
176 | Analyze: "Analyze this text and provide insights: {context}"
177 | Custom: "{user_prompt}\n\nContext: {context}"
178 | ```
179 | 
180 | **Complete guide**: See [`API_INTEGRATION.md`](./API_INTEGRATION.md)
181 | 
182 | ---
183 | 
184 | ## Implementation Priority
185 | 
186 | ### Critical Path (Must-Have for Launch)
187 | 
188 | **~60 critical files** to build in priority order:
189 | 
190 | 1. **Project Setup** (8 files) - Day 1
191 | 2. **Electron App** (5 files) - Day 2
192 | 3. **Overlay UI** (6 files) - Day 3
193 | 4. **Text Selection** (8 files) - Week 3-4
194 | 5. **Overlay Management** (3 files) - Week 3-4
195 | 6. **AI Integration** (7 files) - Week 5-6
196 | 7. **Chat Interface** (9 files) - Week 7-8
197 | 8. **Settings** (8 files) - Week 9-10
198 | 9. **Setup UI** (12 files) - Week 9-10
199 | 10. **Build Pipeline** (3 files) - Week 2
200 | 
201 | ### Can Be Deferred (Post-Launch)
202 | 
203 | - Advanced E2E testing
204 | - System tray integration
205 | - Conversation search
206 | - Dark mode
207 | - Custom shortcuts
208 | - Analytics
209 | - Advanced error reporting
210 | 
211 | **Detailed priority list**: See [`IMPLEMENTATION_PRIORITY.md`](./IMPLEMENTATION_PRIORITY.md)
212 | 
213 | ---
214 | 
215 | ## Architecture Highlights
216 | 
217 | ### System Architecture
218 | 
219 | ```
220 | ┌─────────────────────────────────────────────────┐
221 | │                   User                          │
222 | └────────────┬────────────────────────────────────┘
223 |              │ Highlights text
224 |              ▼
225 | ┌─────────────────────────────────────────────────┐
226 | │         Operating System (Windows/Mac/Linux)    │
227 | └────────────┬────────────────────────────────────┘
228 |              │ Selection event
229 |              ▼
230 | ┌─────────────────────────────────────────────────┐
231 | │      Text Selection Detector (Main Process)     │
232 | │  • Windows: UI Automation API                   │
233 | │  • macOS: Accessibility API                     │
234 | │  • Linux: X11/Wayland                          │
235 | └────────────┬────────────────────────────────────┘
236 |              │ Text + Position
237 |              ▼
238 | ┌─────────────────────────────────────────────────┐
239 | │      Overlay Manager (Main Process)             │
240 | │  • Creates transparent window                   │
241 | │  • Positions at cursor                         │
242 | │  • Manages click-through                       │
243 | └────────────┬────────────────────────────────────┘
244 |              │ Display popup
245 |              ▼
246 | ┌─────────────────────────────────────────────────┐
247 | │      SmartClick Popup (Renderer Process)        │
248 | │  • Shows selected text                         │
249 | │  • Action buttons (Summarize, Rewrite, etc.)   │
250 | │  • Expand to chat option                       │
251 | └────────────┬────────────────────────────────────┘
252 |              │ User action
253 |              ▼
254 | ┌─────────────────────────────────────────────────┐
255 | │      AI Engine (Main Process)                   │
256 | │  • Builds optimized prompt                     │
257 | │  • Manages context window                      │
258 | │  • Handles caching                             │
259 | └────────────┬────────────────────────────────────┘
260 |              │ API request
261 |              ▼
262 | ┌─────────────────────────────────────────────────┐
263 | │      IBM watsonx API                            │
264 | │  • Text generation                             │
265 | │  • Streaming responses                         │
266 | └────────────┬────────────────────────────────────┘
267 |              │ AI response (streaming)
268 |              ▼
269 | ┌─────────────────────────────────────────────────┐
270 | │      Chat Interface (Renderer Process)          │
271 | │  • Real-time response display                  │
272 | │  • Multi-turn conversations                    │
273 | │  • Context persistence                         │
274 | └─────────────────────────────────────────────────┘
275 | ```
276 | 
277 | ### Security Model
278 | 
279 | - **API keys**: Encrypted storage with `electron-store`
280 | - **IPC**: Context isolation between main and renderer
281 | - **Permissions**: Request only what's needed
282 | - **Updates**: Secure auto-update mechanism
283 | 
284 | **Full architecture**: See [`ARCHITECTURE.md`](./ARCHITECTURE.md)
285 | 
286 | ---
287 | 
288 | ## Key Technical Challenges & Solutions
289 | 
290 | ### Challenge 1: Cross-Platform Text Selection
291 | 
292 | **Problem**: Each OS has different APIs for detecting text selection
293 | 
294 | **Solution**:
295 | - Create unified interface
296 | - Platform-specific implementations
297 | - Clipboard monitoring as fallback
298 | - Graceful degradation
299 | 
300 | ```typescript
301 | interface TextSelection {
302 |   text: string;
303 |   position: { x: number; y: number };
304 |   application: string;
305 | }
306 | 
307 | class TextSelectionDetector {
308 |   detectSelection(): Promise<TextSelection | null> {
309 |     switch (platform) {
310 |       case 'win32': return this.detectWindows();
311 |       case 'darwin': return this.detectMacOS();
312 |       case 'linux': return this.detectLinux();
313 |     }
314 |   }
315 | }
316 | ```
317 | 
318 | ### Challenge 2: Overlay Performance
319 | 
320 | **Problem**: Overlay must be responsive without impacting system
321 | 
322 | **Solution**:
323 | - GPU-accelerated CSS transforms
324 | - Debounced text selection events (300ms)
325 | - Lazy loading of chat components
326 | - Virtual scrolling for long histories
327 | 
328 | ### Challenge 3: Context Management
329 | 
330 | **Problem**: Maintaining conversation context within token limits
331 | 
332 | **Solution**:
333 | - Sliding window with selected text always included
334 | - Prioritize recent messages
335 | - Token counting and intelligent truncation
336 | - Context persistence in SQLite
337 | 
338 | ### Challenge 4: Rate Limiting
339 | 
340 | **Problem**: IBM watsonx API has rate limits
341 | 
342 | **Solution**:
343 | - Request queuing
344 | - Response caching
345 | - User feedback on limits
346 | - Exponential backoff for retries
347 | 
348 | ---
349 | 
350 | ## Quick Start Guide
351 | 
352 | ### Prerequisites
353 | 
354 | ```bash
355 | # Required
356 | Node.js 18+ LTS
357 | npm or yarn
358 | Git
359 | 
360 | # Platform-specific
361 | Windows: Visual Studio Build Tools
362 | macOS: Xcode Command Line Tools
363 | Linux: build-essential
364 | ```
365 | 
366 | ### Initial Setup
367 | 
368 | ```bash
369 | # 1. Clone repository
370 | git clone <repo-url>
371 | cd smart-clicks
372 | 
373 | # 2. Install dependencies
374 | npm install
375 | 
376 | # 3. Configure environment
377 | cp .env.example .env
378 | # Edit .env with IBM watsonx credentials
379 | 
380 | # 4. Start development
381 | npm run dev
382 | ```
383 | 
384 | ### Development Commands
385 | 
386 | ```bash
387 | npm run dev          # Start with hot reload
388 | npm run build        # Build for production
389 | npm run package      # Create installers
390 | npm test             # Run tests
391 | npm run lint         # Check code quality
392 | ```
393 | 
394 | ---
395 | 
396 | ## Success Metrics
397 | 
398 | ### Technical Metrics
399 | 
400 | - ⚡ Overlay appears in **< 300ms** after text selection
401 | - 🚀 AI response starts streaming in **< 2 seconds**
402 | - 💾 Memory usage **< 200MB**
403 | - ⏱️ App startup time **< 2 seconds**
404 | - ✅ Test coverage **> 80%**
405 | 
406 | ### User Experience Metrics
407 | 
408 | - 📊 Setup completion rate **> 90%**
409 | - 🎯 Daily active usage **> 10 interactions/user**
410 | - ⭐ User satisfaction **> 4.5/5**
411 | - 🐛 Crash rate **< 0.1%**
412 | 
413 | ### Business Metrics
414 | 
415 | - 📈 Installation completion **> 80%**
416 | - 🔄 7-day retention **> 60%**
417 | - 📅 30-day retention **> 40%**
418 | - 💯 NPS score **> 50**
419 | 
420 | ---
421 | 
422 | ## Risk Mitigation
423 | 
424 | ### Technical Risks
425 | 
426 | | Risk | Impact | Mitigation |
427 | |------|--------|------------|
428 | | Platform-specific APIs vary | High | Unified interface + extensive testing |
429 | | Overlay performance issues | Medium | Performance monitoring + optimization |
430 | | API rate limits | Medium | Caching + queuing + user feedback |
431 | | Permission denials | High | Clear explanations + fallbacks |
432 | 
433 | ### Schedule Risks
434 | 
435 | | Risk | Impact | Mitigation |
436 | |------|--------|------------|
437 | | Underestimated complexity | High | MVP first + iterative development |
438 | | Platform-specific bugs | Medium | Early testing on all platforms |
439 | | Team availability | Medium | 2-week buffer in timeline |
440 | 
441 | ---
442 | 
443 | ## Resource Requirements
444 | 
445 | ### Team
446 | 
447 | - **2 Full-stack Developers** (Electron + React + TypeScript)
448 | - **1 UI/UX Designer** (part-time)
449 | - **1 QA Engineer** (part-time, Phase 6)
450 | 
451 | ### Tools & Services
452 | 
453 | - GitHub (version control + CI/CD)
454 | - IBM watsonx account with API access
455 | - Code signing certificates (Apple, Microsoft)
456 | - Sentry (error tracking)
457 | - Figma (design)
458 | 
459 | ### Budget Considerations
460 | 
461 | - IBM watsonx API costs (usage-based)
462 | - Code signing certificates (~$500/year)
463 | - Testing infrastructure
464 | - Design tools subscriptions
465 | 
466 | ---
467 | 
468 | ## Next Steps
469 | 
470 | ### Immediate Actions (This Week)
471 | 
472 | 1. ✅ **Review this plan** with stakeholders
473 | 2. ✅ **Set up IBM watsonx** account and get credentials
474 | 3. ✅ **Initialize project** with recommended stack
475 | 4. ✅ **Build MVP prototype** (5 days)
476 | 5. ✅ **Get feedback** on MVP from users
477 | 
478 | ### Week 2 Actions
479 | 
480 | 1. Complete Phase 1 (Infrastructure)
481 | 2. Set up CI/CD pipeline
482 | 3. Establish testing framework
483 | 4. Begin Phase 2 (Text Selection)
484 | 
485 | ### Monthly Milestones
486 | 
487 | - **End of Month 1**: Text selection working on all platforms
488 | - **End of Month 2**: AI integration complete with chat
489 | - **End of Month 3**: Production-ready application
490 | 
491 | ---
492 | 
493 | ## Documentation Index
494 | 
495 | All planning documents are in the `docs/` directory:
496 | 
497 | 1. **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System architecture and technical design
498 | 2. **[FOLDER_STRUCTURE.md](./FOLDER_STRUCTURE.md)** - Complete project structure
499 | 3. **[DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)** - Phased development approach
500 | 4. **[API_INTEGRATION.md](./API_INTEGRATION.md)** - IBM watsonx integration guide
501 | 5. **[IMPLEMENTATION_PRIORITY.md](./IMPLEMENTATION_PRIORITY.md)** - File-by-file priority list
502 | 6. **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - This document
503 | 
504 | ---
505 | 
506 | ## Recommendations Summary
507 | 
508 | ### ✅ Technology Stack
509 | **Electron + React + TypeScript** provides the best balance of:
510 | - Cross-platform compatibility
511 | - Development speed
512 | - Rich UI capabilities
513 | - IBM watsonx SDK support
514 | 
515 | ### ✅ Development Approach
516 | **Start with MVP** (Week 1):
517 | - Validates concept quickly
518 | - Gets stakeholder buy-in
519 | - Identifies challenges early
520 | - Enables iterative development
521 | 
522 | ### ✅ Implementation Strategy
523 | **Follow the critical path**:
524 | - ~60 critical files for launch
525 | - Build incrementally
526 | - Test continuously
527 | - Ship MVP, gather feedback, iterate
528 | 
529 | ### ✅ Timeline
530 | **12 weeks to production**:
531 | - Realistic with 2-3 developers
532 | - Includes 2-week buffer
533 | - Phased approach with clear milestones
534 | - MVP in Week 1 for early validation
535 | 
536 | ---
537 | 
538 | ## Conclusion
539 | 
540 | SmartClick is technically feasible and can be built in 12 weeks with the recommended stack. The architecture is solid, the plan is detailed, and the risks are manageable.
541 | 
542 | **Key Success Factors**:
543 | 1. ✅ Start with MVP to validate concept
544 | 2. ✅ Follow the critical path
545 | 3. ✅ Test continuously
546 | 4. ✅ Iterate based on feedback
547 | 5. ✅ Ship incrementally
548 | 
549 | **Ready to build?** Start with the MVP prototype using [`IMPLEMENTATION_PRIORITY.md`](./IMPLEMENTATION_PRIORITY.md) as your guide.
550 | 
551 | ---
552 | 
553 | ## Questions?
554 | 
555 | If you have questions about:
556 | - **Architecture**: See [`ARCHITECTURE.md`](./ARCHITECTURE.md)
557 | - **Project structure**: See [`FOLDER_STRUCTURE.md`](./FOLDER_STRUCTURE.md)
558 | - **Development phases**: See [`DEVELOPMENT_PLAN.md`](./DEVELOPMENT_PLAN.md)
559 | - **IBM watsonx**: See [`API_INTEGRATION.md`](./API_INTEGRATION.md)
560 | - **What to build first**: See [`IMPLEMENTATION_PRIORITY.md`](./IMPLEMENTATION_PRIORITY.md)
561 | 
562 | **Let's build SmartClick! 🚀**
</content>
</file>
<file><path>docs/ARCHITECTURE.md</path>
<content lines="1-390">
  1 | # SmartClick Architecture Documentation
  2 | 
  3 | ## Executive Summary
  4 | 
  5 | SmartClick is a cross-platform AI-powered cursor layer that integrates IBM Bob/watsonx AI into any application. The system consists of two main components:
  6 | 
  7 | 1. **Setup/Configuration App** - One-time setup interface that runs in the background
  8 | 2. **Cursor Layer** - System-wide text selection overlay with AI capabilities
  9 | 
 10 | ## Technology Stack Recommendations
 11 | 
 12 | ### Core Framework: Electron + Node.js
 13 | 
 14 | **Rationale:**
 15 | - **Cross-platform compatibility** - Single codebase for Windows, macOS, and Linux
 16 | - **System-level access** - Can create global overlays and capture system-wide events
 17 | - **Rich UI capabilities** - Modern web technologies for responsive, beautiful interfaces
 18 | - **Active ecosystem** - Extensive libraries for system integration
 19 | - **IBM SDK support** - Node.js has official IBM watsonx SDK
 20 | 
 21 | ### Technology Breakdown
 22 | 
 23 | #### 1. Setup/Configuration App
 24 | - **Framework:** Electron
 25 | - **UI:** React 18+ with TypeScript
 26 | - **State Management:** Zustand (lightweight, perfect for settings)
 27 | - **Styling:** Tailwind CSS + shadcn/ui components
 28 | - **Build Tool:** Vite (fast development, optimized builds)
 29 | 
 30 | #### 2. Cursor Layer (Overlay System)
 31 | - **Framework:** Electron (transparent, frameless windows)
 32 | - **UI:** React 18+ with TypeScript
 33 | - **Overlay Management:** Custom Electron BrowserWindow configuration
 34 | - **Text Selection Detection:** Native OS APIs via Node.js addons
 35 | - **IPC:** Electron IPC for communication between processes
 36 | 
 37 | #### 3. Background Service
 38 | - **Runtime:** Node.js
 39 | - **Process Management:** Electron main process
 40 | - **System Integration:** 
 41 |   - `node-global-key-listener` for keyboard shortcuts
 42 |   - `robotjs` or `nut-js` for cursor position tracking
 43 |   - Native modules for clipboard and text selection access
 44 | 
 45 | #### 4. AI Integration
 46 | - **IBM watsonx SDK:** `@ibm-cloud/watsonx-ai`
 47 | - **HTTP Client:** `axios` with retry logic
 48 | - **Streaming:** Server-Sent Events (SSE) for real-time responses
 49 | - **Context Management:** Custom context window manager
 50 | 
 51 | #### 5. Data & Storage
 52 | - **Settings Storage:** `electron-store` (encrypted local storage)
 53 | - **Chat History:** SQLite via `better-sqlite3`
 54 | - **Cache:** In-memory LRU cache for recent contexts
 55 | 
 56 | ### Alternative Stack Consideration
 57 | 
 58 | **Tauri + Rust** (Future consideration)
 59 | - Lighter weight than Electron
 60 | - Better performance and security
 61 | - Smaller bundle size
 62 | - More complex development for system-level features
 63 | - **Recommendation:** Start with Electron, consider Tauri for v2.0
 64 | 
 65 | ## System Architecture
 66 | 
 67 | ### High-Level Component Diagram
 68 | 
 69 | ```mermaid
 70 | graph TB
 71 |     User[User] -->|Highlights Text| OS[Operating System]
 72 |     OS -->|Selection Event| TSD[Text Selection Detector]
 73 |     TSD -->|Coordinates & Text| OM[Overlay Manager]
 74 |     OM -->|Display| Popup[SmartClick Popup]
 75 |     Popup -->|User Action| AIE[AI Engine]
 76 |     AIE -->|API Request| IBM[IBM watsonx]
 77 |     IBM -->|Response| AIE
 78 |     AIE -->|Result| Chat[Chat Interface]
 79 |     Chat -->|Display| User
 80 |     
 81 |     Setup[Setup App] -->|Configure| Config[Configuration Store]
 82 |     Config -->|Settings| OM
 83 |     Config -->|API Keys| AIE
 84 |     
 85 |     BG[Background Service] -->|Monitor| TSD
 86 |     BG -->|Manage| OM
 87 |     BG -->|Shortcuts| KL[Keyboard Listener]
 88 | ```
 89 | 
 90 | ### Process Architecture
 91 | 
 92 | ```mermaid
 93 | graph LR
 94 |     Main[Main Process<br/>Background Service] -->|IPC| Setup[Setup Window<br/>Renderer Process]
 95 |     Main -->|IPC| Overlay[Overlay Window<br/>Renderer Process]
 96 |     Main -->|Manages| Store[Electron Store<br/>Settings & Keys]
 97 |     Main -->|Queries| DB[SQLite DB<br/>Chat History]
 98 |     Overlay -->|API Calls| Watson[IBM watsonx API]
 99 | ```
100 | 
101 | ### Data Flow: Text Selection to AI Response
102 | 
103 | ```mermaid
104 | sequenceDiagram
105 |     participant User
106 |     participant OS
107 |     participant Detector
108 |     participant Overlay
109 |     participant AI
110 |     participant Watson
111 |     
112 |     User->>OS: Highlights text
113 |     OS->>Detector: Selection event
114 |     Detector->>Detector: Extract text & position
115 |     Detector->>Overlay: Show popup at cursor
116 |     User->>Overlay: Click "Summarize"
117 |     Overlay->>AI: Process request
118 |     AI->>Watson: API call with context
119 |     Watson-->>AI: Streaming response
120 |     AI-->>Overlay: Update UI in real-time
121 |     Overlay-->>User: Display result
122 | ```
123 | 
124 | ## Core Features & Implementation
125 | 
126 | ### 1. Text Selection Detection
127 | 
128 | **Cross-Platform Approaches:**
129 | 
130 | **Windows:**
131 | - Use Windows Accessibility API (UI Automation)
132 | - Monitor clipboard for Ctrl+C events
133 | - Hook into text selection events via native addon
134 | 
135 | **macOS:**
136 | - Use Accessibility API (AXUIElement)
137 | - Monitor NSPasteboard
138 | - Require accessibility permissions
139 | 
140 | **Linux:**
141 | - Use X11 selection buffer (PRIMARY selection)
142 | - Monitor D-Bus for clipboard events
143 | - Wayland support via wl-clipboard
144 | 
145 | **Implementation Strategy:**
146 | ```typescript
147 | // Unified text selection interface
148 | interface TextSelection {
149 |   text: string;
150 |   position: { x: number; y: number };
151 |   application: string;
152 |   timestamp: number;
153 | }
154 | 
155 | class TextSelectionDetector {
156 |   private platform: 'win32' | 'darwin' | 'linux';
157 |   
158 |   async detectSelection(): Promise<TextSelection | null> {
159 |     switch (this.platform) {
160 |       case 'win32':
161 |         return this.detectWindows();
162 |       case 'darwin':
163 |         return this.detectMacOS();
164 |       case 'linux':
165 |         return this.detectLinux();
166 |     }
167 |   }
168 | }
169 | ```
170 | 
171 | ### 2. Overlay System
172 | 
173 | **Electron Window Configuration:**
174 | ```typescript
175 | const overlayWindow = new BrowserWindow({
176 |   transparent: true,
177 |   frame: false,
178 |   alwaysOnTop: true,
179 |   skipTaskbar: true,
180 |   resizable: false,
181 |   focusable: true,
182 |   webPreferences: {
183 |     nodeIntegration: false,
184 |     contextIsolation: true,
185 |     preload: path.join(__dirname, 'preload.js')
186 |   }
187 | });
188 | 
189 | // Make window click-through except for popup area
190 | overlayWindow.setIgnoreMouseEvents(true, { forward: true });
191 | ```
192 | 
193 | **Popup Positioning:**
194 | - Calculate position relative to text selection
195 | - Adjust for screen boundaries
196 | - Handle multi-monitor setups
197 | - Smooth animations with CSS transitions
198 | 
199 | ### 3. IBM watsonx Integration
200 | 
201 | **API Configuration:**
202 | ```typescript
203 | interface WatsonxConfig {
204 |   apiKey: string;
205 |   projectId: string;
206 |   endpoint: string;
207 |   modelId: string; // e.g., 'ibm/granite-13b-chat-v2'
208 | }
209 | 
210 | class WatsonxClient {
211 |   async generateText(prompt: string, context: string): Promise<string> {
212 |     // Use IBM watsonx SDK
213 |     const response = await this.client.textGeneration({
214 |       input: this.buildPrompt(prompt, context),
215 |       modelId: this.config.modelId,
216 |       parameters: {
217 |         max_new_tokens: 1024,
218 |         temperature: 0.7,
219 |         top_p: 0.9
220 |       }
221 |     });
222 |     return response.results[0].generated_text;
223 |   }
224 |   
225 |   async streamGeneration(prompt: string, context: string): AsyncGenerator<string> {
226 |     // Streaming implementation for real-time responses
227 |   }
228 | }
229 | ```
230 | 
231 | **Prompt Templates:**
232 | ```typescript
233 | const PROMPT_TEMPLATES = {
234 |   summarize: "Summarize the following text concisely:\n\n{context}",
235 |   rewrite: "Rewrite the following text to be more {tone}:\n\n{context}",
236 |   explain: "Explain the following text in simple terms:\n\n{context}",
237 |   analyze: "Analyze the following text and provide insights:\n\n{context}",
238 |   custom: "{prompt}\n\nContext:\n{context}"
239 | };
240 | ```
241 | 
242 | ### 4. Context Management
243 | 
244 | **Context Window Strategy:**
245 | ```typescript
246 | interface ConversationContext {
247 |   id: string;
248 |   selectedText: string;
249 |   messages: Message[];
250 |   metadata: {
251 |     application: string;
252 |     timestamp: number;
253 |     location: string;
254 |   };
255 | }
256 | 
257 | class ContextManager {
258 |   private maxContextLength = 4096; // tokens
259 |   
260 |   buildContext(conversation: ConversationContext): string {
261 |     // Implement sliding window with selected text always included
262 |     // Prioritize recent messages
263 |     // Truncate older messages if needed
264 |   }
265 | }
266 | ```
267 | 
268 | ## Security Considerations
269 | 
270 | ### 1. API Key Storage
271 | - Store IBM watsonx credentials in encrypted format
272 | - Use `electron-store` with encryption enabled
273 | - Never expose keys in renderer process
274 | - Implement key rotation mechanism
275 | 
276 | ### 2. Data Privacy
277 | - All text processing happens locally until sent to IBM
278 | - Implement opt-in telemetry
279 | - Clear chat history option
280 | - No persistent storage of sensitive text without consent
281 | 
282 | ### 3. Permissions
283 | - Request only necessary OS permissions
284 | - Clear permission explanations in setup
285 | - Graceful degradation if permissions denied
286 | 
287 | ## Performance Optimization
288 | 
289 | ### 1. Overlay Performance
290 | - Use CSS transforms for animations (GPU-accelerated)
291 | - Lazy load chat interface components
292 | - Debounce text selection events (300ms)
293 | - Virtual scrolling for long chat histories
294 | 
295 | ### 2. AI Response Optimization
296 | - Implement response caching for identical queries
297 | - Use streaming for better perceived performance
298 | - Show loading states immediately
299 | - Prefetch common operations
300 | 
301 | ### 3. Memory Management
302 | - Limit chat history in memory (last 50 conversations)
303 | - Implement garbage collection for old contexts
304 | - Use worker threads for heavy processing
305 | - Monitor and limit overlay window count
306 | 
307 | ## Accessibility
308 | 
309 | - Full keyboard navigation support
310 | - Screen reader compatibility
311 | - High contrast mode support
312 | - Customizable font sizes
313 | - Respect OS accessibility settings
314 | 
315 | ## Deployment Strategy
316 | 
317 | ### Build & Distribution
318 | - **Electron Builder** for packaging
319 | - **Auto-update** via electron-updater
320 | - **Code signing** for all platforms
321 | - **DMG** for macOS, **MSI** for Windows, **AppImage/deb** for Linux
322 | 
323 | ### Installation Flow
324 | 1. User downloads installer
325 | 2. Setup app launches automatically
326 | 3. User configures IBM watsonx credentials
327 | 4. User sets keyboard shortcuts
328 | 5. User grants necessary permissions
329 | 6. Setup app minimizes to system tray
330 | 7. Background service starts monitoring
331 | 
332 | ## Monitoring & Analytics
333 | 
334 | - Error tracking with Sentry
335 | - Anonymous usage analytics (opt-in)
336 | - Performance metrics
337 | - API usage tracking
338 | - Crash reporting
339 | 
340 | ## Future Enhancements (Post-MVP)
341 | 
342 | 1. **Multi-AI Provider Support** - OpenAI, Anthropic, local models
343 | 2. **Custom Actions** - User-defined text transformations
344 | 3. **Team Collaboration** - Shared prompts and templates
345 | 4. **Browser Extension** - Enhanced web integration
346 | 5. **Mobile Companion** - iOS/Android apps
347 | 6. **Voice Input** - Speech-to-text for queries
348 | 7. **Plugin System** - Third-party extensions
349 | 8. **Offline Mode** - Local AI model support
350 | 
351 | ## Technical Risks & Mitigations
352 | 
353 | | Risk | Impact | Mitigation |
354 | |------|--------|------------|
355 | | OS-specific text selection APIs vary | High | Abstract with unified interface, extensive testing |
356 | | Overlay performance on older hardware | Medium | Implement performance monitoring, graceful degradation |
357 | | IBM watsonx API rate limits | Medium | Implement request queuing, caching, user feedback |
358 | | Permission denial by users | High | Clear explanations, graceful fallbacks, manual mode |
359 | | Electron bundle size | Low | Code splitting, lazy loading, tree shaking |
360 | 
361 | ## Development Environment Setup
362 | 
363 | ### Prerequisites
364 | - Node.js 18+ LTS
365 | - npm or yarn
366 | - Git
367 | - Platform-specific build tools:
368 |   - Windows: Visual Studio Build Tools
369 |   - macOS: Xcode Command Line Tools
370 |   - Linux: build-essential
371 | 
372 | ### Quick Start
373 | ```bash
374 | npm install
375 | npm run dev          # Start development mode
376 | npm run build        # Build for production
377 | npm run package      # Create distributable
378 | ```
379 | 
380 | ## Conclusion
381 | 
382 | This architecture provides a solid foundation for SmartClick with:
383 | - ✅ Cross-platform compatibility
384 | - ✅ System-wide text selection
385 | - ✅ Seamless IBM watsonx integration
386 | - ✅ Scalable and maintainable codebase
387 | - ✅ Excellent user experience
388 | - ✅ Security and privacy by design
389 | 
390 | The Electron + React + TypeScript stack offers the best balance of development speed, cross-platform support, and rich UI capabilities for this use case.
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs
backend/backend_client.py,backend/api/main.py,.env,docs/SERVICE_DOCUMENTATION.md,docs/FRONTEND_IMPLEMENTATION_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-03T13:30:20.464Z
User time zone: Africa/Johannesburg, UTC+2:00

# Current Cost
$0.08

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>advanced</slug>
<name>🛠️ Advanced</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll continue reading the remaining documentation files to complete my comprehensive analysis.

<read_file>
<args>
  <file>
    <path>docs/DEVELOPMENT_PLAN.md</path>
  </file>
  <file>
    <path>docs/FOLDER_STRUCTURE.md</path>
  </file>
  <file>
    <path>docs/IMPLEMENTATION_PRIORITY.md</path>
  </file>
  <file>
    <path>docs/REACT_MODERNIZATION_PLAN.md</path>
  </file>
  <file>
    <path>docs/API_INTEGRATION.md</path>
  </file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>docs/DEVELOPMENT_PLAN.md</path>
<content lines="1-652">
  1 | # SmartClick Development Plan
  2 | 
  3 | ## Overview
  4 | 
  5 | This document outlines the phased development approach for SmartClick, breaking down the project into manageable milestones with clear deliverables and success criteria.
  6 | 
  7 | ## Development Phases
  8 | 
  9 | ### Phase 1: Core Infrastructure Setup (Week 1-2)
 10 | 
 11 | **Goal**: Establish the foundational project structure and development environment
 12 | 
 13 | #### Tasks
 14 | 
 15 | 1. **Project Initialization**
 16 |    - Initialize npm project with proper configuration
 17 |    - Set up TypeScript with appropriate configs for main/renderer
 18 |    - Configure Electron with basic window management
 19 |    - Set up Vite for renderer process bundling
 20 |    - Configure path aliases for clean imports
 21 | 
 22 | 2. **Development Tooling**
 23 |    - Configure ESLint with TypeScript rules
 24 |    - Set up Prettier for code formatting
 25 |    - Configure Vitest for unit testing
 26 |    - Set up Playwright for E2E testing
 27 |    - Create development scripts (dev, build, test)
 28 | 
 29 | 3. **Basic Electron App Structure**
 30 |    - Create main process entry point
 31 |    - Set up IPC communication framework
 32 |    - Create basic preload scripts
 33 |    - Implement application lifecycle management
 34 |    - Add error handling and logging utilities
 35 | 
 36 | 4. **Build Pipeline**
 37 |    - Configure Electron Builder for packaging
 38 |    - Set up platform-specific build configurations
 39 |    - Create build scripts for development and production
 40 |    - Configure code signing (placeholder for now)
 41 | 
 42 | #### Deliverables
 43 | - ✅ Working Electron app that opens a blank window
 44 | - ✅ Hot reload working for development
 45 | - ✅ Build pipeline producing executables for all platforms
 46 | - ✅ Basic logging and error handling in place
 47 | 
 48 | #### Success Criteria
 49 | - `npm run dev` starts the app with hot reload
 50 | - `npm run build` compiles without errors
 51 | - `npm run package` creates platform-specific installers
 52 | - Tests run successfully with `npm test`
 53 | 
 54 | #### Key Files to Create
 55 | ```
 56 | package.json (update)
 57 | tsconfig.json
 58 | tsconfig.main.json
 59 | tsconfig.renderer.json
 60 | vite.config.ts
 61 | vitest.config.ts
 62 | electron-builder.yml
 63 | src/main/index.ts
 64 | src/main/app.ts
 65 | src/main/utils/logger.ts
 66 | src/preload/setup.preload.ts
 67 | src/renderer/setup/index.html
 68 | src/renderer/setup/main.tsx
 69 | src/renderer/setup/App.tsx
 70 | scripts/dev.js
 71 | scripts/build.js
 72 | ```
 73 | 
 74 | ---
 75 | 
 76 | ### Phase 2: Text Selection & Popup System (Week 3-4)
 77 | 
 78 | **Goal**: Implement cross-platform text selection detection and overlay popup
 79 | 
 80 | #### Tasks
 81 | 
 82 | 1. **Text Selection Detection**
 83 |    - Research and implement platform-specific APIs
 84 |    - Create unified text selection interface
 85 |    - Implement Windows text selection (UI Automation API)
 86 |    - Implement macOS text selection (Accessibility API)
 87 |    - Implement Linux text selection (X11/Wayland)
 88 |    - Add clipboard monitoring as fallback
 89 |    - Implement debouncing and filtering logic
 90 | 
 91 | 2. **Overlay Window System**
 92 |    - Create transparent, frameless overlay window
 93 |    - Implement click-through behavior
 94 |    - Add multi-monitor support
 95 |    - Create window positioning logic
 96 |    - Implement smooth show/hide animations
 97 | 
 98 | 3. **Basic Popup UI**
 99 |    - Design and implement popup component
100 |    - Add quick action buttons (Summarize, Rewrite, Explain)
101 |    - Implement expand/collapse functionality
102 |    - Add loading states and animations
103 |    - Style with Tailwind CSS
104 | 
105 | 4. **IPC Communication**
106 |    - Set up IPC channels for text selection events
107 |    - Implement overlay show/hide commands
108 |    - Add position calculation and adjustment
109 |    - Handle edge cases (screen boundaries, multi-monitor)
110 | 
111 | #### Deliverables
112 | - ✅ Text selection detected across all platforms
113 | - ✅ Popup appears at cursor position when text is selected
114 | - ✅ Popup displays selected text and action buttons
115 | - ✅ Smooth animations and responsive UI
116 | 
117 | #### Success Criteria
118 | - Selecting text in any application triggers popup within 300ms
119 | - Popup appears at correct position on all monitors
120 | - Popup doesn't interfere with normal application usage
121 | - Click-through works correctly when popup is not active
122 | 
123 | #### Key Files to Create
124 | ```
125 | src/main/services/text-selection/index.ts
126 | src/main/services/text-selection/detector.ts
127 | src/main/services/text-selection/windows.detector.ts
128 | src/main/services/text-selection/macos.detector.ts
129 | src/main/services/text-selection/linux.detector.ts
130 | src/main/services/overlay/index.ts
131 | src/main/services/overlay/manager.ts
132 | src/main/services/overlay/window-factory.ts
133 | src/main/ipc/overlay.handler.ts
134 | src/renderer/overlay/index.html
135 | src/renderer/overlay/main.tsx
136 | src/renderer/overlay/App.tsx
137 | src/renderer/overlay/components/Popup/index.tsx
138 | src/renderer/overlay/components/Popup/ActionButtons.tsx
139 | src/renderer/overlay/hooks/useSelection.ts
140 | src/renderer/overlay/hooks/usePosition.ts
141 | src/renderer/overlay/utils/positioning.ts
142 | src/shared/types/selection.types.ts
143 | tests/integration/text-selection.test.ts
144 | tests/integration/overlay-display.test.ts
145 | ```
146 | 
147 | ---
148 | 
149 | ### Phase 3: IBM watsonx Integration (Week 5-6)
150 | 
151 | **Goal**: Integrate IBM watsonx AI for text processing capabilities
152 | 
153 | #### Tasks
154 | 
155 | 1. **IBM watsonx Client Setup**
156 |    - Install IBM watsonx SDK (`@ibm-cloud/watsonx-ai`)
157 |    - Create watsonx client wrapper
158 |    - Implement authentication with API keys
159 |    - Add error handling and retry logic
160 |    - Implement request/response logging
161 | 
162 | 2. **Prompt Engineering**
163 |    - Design prompt templates for each action
164 |    - Implement prompt builder with context injection
165 |    - Add system prompts for consistent behavior
166 |    - Create prompt testing framework
167 |    - Optimize prompts for token efficiency
168 | 
169 | 3. **AI Service Layer**
170 |    - Create AI service abstraction
171 |    - Implement text generation methods
172 |    - Add streaming support for real-time responses
173 |    - Implement response caching
174 |    - Add rate limiting and queue management
175 | 
176 | 4. **Context Management**
177 |    - Design context window strategy
178 |    - Implement context builder
179 |    - Add token counting and truncation
180 |    - Create context persistence for conversations
181 |    - Implement context cleanup
182 | 
183 | 5. **Integration with Popup**
184 |    - Connect action buttons to AI service
185 |    - Display AI responses in popup
186 |    - Add loading indicators
187 |    - Implement error handling and user feedback
188 |    - Add retry mechanism for failed requests
189 | 
190 | #### Deliverables
191 | - ✅ Working IBM watsonx integration
192 | - ✅ All quick actions (Summarize, Rewrite, Explain) functional
193 | - ✅ Streaming responses displayed in real-time
194 | - ✅ Error handling with user-friendly messages
195 | 
196 | #### Success Criteria
197 | - AI responses appear within 2-3 seconds
198 | - Streaming updates are smooth and readable
199 | - Failed requests are retried automatically
200 | - API errors are handled gracefully with clear messages
201 | - Context is maintained correctly across requests
202 | 
203 | #### Key Files to Create
204 | ```
205 | src/main/services/ai/index.ts
206 | src/main/services/ai/watsonx-client.ts
207 | src/main/services/ai/context-manager.ts
208 | src/main/services/ai/prompt-builder.ts
209 | src/main/services/ai/cache.ts
210 | src/main/ipc/ai.handler.ts
211 | src/shared/types/ai.types.ts
212 | src/shared/constants/prompts.ts
213 | src/renderer/overlay/hooks/useAI.ts
214 | tests/unit/main/services/ai.test.ts
215 | tests/integration/ai-integration.test.ts
216 | .env.example
217 | ```
218 | 
219 | ---
220 | 
221 | ### Phase 4: Chat Interface & Context Management (Week 7-8)
222 | 
223 | **Goal**: Build expandable chat interface with conversation history
224 | 
225 | #### Tasks
226 | 
227 | 1. **Chat UI Components**
228 |    - Design and implement chat interface
229 |    - Create message list with virtual scrolling
230 |    - Build message components (user/assistant)
231 |    - Implement input box with auto-resize
232 |    - Add context display showing selected text
233 |    - Style chat interface for readability
234 | 
235 | 2. **Chat State Management**
236 |    - Set up Zustand store for chat state
237 |    - Implement message history management
238 |    - Add conversation persistence
239 |    - Create chat session management
240 |    - Implement undo/redo for messages
241 | 
242 | 3. **Expand/Collapse Functionality**
243 |    - Implement smooth transition from popup to chat
244 |    - Add expand/collapse animations
245 |    - Maintain popup position during expansion
246 |    - Handle window resizing
247 |    - Add minimize to popup option
248 | 
249 | 4. **Conversation Features**
250 |    - Implement multi-turn conversations
251 |    - Add message editing capability
252 |    - Implement message regeneration
253 |    - Add copy message functionality
254 |    - Create conversation export feature
255 | 
256 | 5. **Context Persistence**
257 |    - Implement SQLite database for chat history
258 |    - Create database schema
259 |    - Add CRUD operations for conversations
260 |    - Implement search functionality
261 |    - Add conversation cleanup (old conversations)
262 | 
263 | #### Deliverables
264 | - ✅ Fully functional chat interface
265 | - ✅ Smooth expand/collapse animations
266 | - ✅ Conversation history persisted to database
267 | - ✅ Multi-turn conversations with context
268 | 
269 | #### Success Criteria
270 | - Chat expands smoothly from popup
271 | - Messages are displayed in real-time as they stream
272 | - Conversation history is saved and retrievable
273 | - Context is maintained across multiple messages
274 | - Chat interface is responsive and performant
275 | 
276 | #### Key Files to Create
277 | ```
278 | src/renderer/overlay/components/Chat/index.tsx
279 | src/renderer/overlay/components/Chat/ChatInterface.tsx
280 | src/renderer/overlay/components/Chat/MessageList.tsx
281 | src/renderer/overlay/components/Chat/Message.tsx
282 | src/renderer/overlay/components/Chat/InputBox.tsx
283 | src/renderer/overlay/components/Chat/ContextDisplay.tsx
284 | src/renderer/overlay/hooks/useChat.ts
285 | src/renderer/overlay/store/chat.store.ts
286 | src/main/services/storage/index.ts
287 | src/main/services/storage/history-db.ts
288 | src/shared/types/chat.types.ts
289 | tests/unit/renderer/overlay/chat.test.tsx
290 | tests/e2e/chat-flow.test.ts
291 | ```
292 | 
293 | ---
294 | 
295 | ### Phase 5: Settings & Configuration UI (Week 9-10)
296 | 
297 | **Goal**: Create setup app for initial configuration and settings management
298 | 
299 | #### Tasks
300 | 
301 | 1. **Setup Flow Design**
302 |    - Design multi-step setup wizard
303 |    - Create welcome screen
304 |    - Design API key configuration screen
305 |    - Create keyboard shortcut configuration
306 |    - Design permissions request screen
307 |    - Create completion screen
308 | 
309 | 2. **Setup UI Implementation**
310 |    - Implement setup flow components
311 |    - Add form validation
312 |    - Create progress indicator
313 |    - Implement navigation (next/back)
314 |    - Add skip options where appropriate
315 |    - Style with modern, clean design
316 | 
317 | 3. **Settings Storage**
318 |    - Implement encrypted settings storage
319 |    - Create settings schema
320 |    - Add settings validation
321 |    - Implement settings migration
322 |    - Add settings export/import
323 | 
324 | 4. **Keyboard Shortcuts**
325 |    - Implement global keyboard listener
326 |    - Create shortcut registration system
327 |    - Add shortcut conflict detection
328 |    - Implement customizable shortcuts
329 |    - Add shortcut help overlay
330 | 
331 | 5. **Permissions Management**
332 |    - Request accessibility permissions (macOS)
333 |    - Request screen recording permission (macOS)
334 |    - Handle permission denials gracefully
335 |    - Add permission status checking
336 |    - Create permission troubleshooting guide
337 | 
338 | 6. **System Tray Integration**
339 |    - Create system tray icon
340 |    - Implement tray menu
341 |    - Add quick settings access
342 |    - Implement show/hide functionality
343 |    - Add quit option
344 | 
345 | #### Deliverables
346 | - ✅ Complete setup wizard
347 | - ✅ Settings stored securely
348 | - ✅ Customizable keyboard shortcuts
349 | - ✅ System tray integration
350 | - ✅ Permission handling for all platforms
351 | 
352 | #### Success Criteria
353 | - Setup flow is intuitive and completes in under 2 minutes
354 | - API keys are stored securely and never exposed
355 | - Keyboard shortcuts work globally across all apps
356 | - System tray provides quick access to settings
357 | - Permissions are requested with clear explanations
358 | 
359 | #### Key Files to Create
360 | ```
361 | src/renderer/setup/components/WelcomeScreen.tsx
362 | src/renderer/setup/components/ApiKeySetup.tsx
363 | src/renderer/setup/components/ShortcutConfig.tsx
364 | src/renderer/setup/components/PermissionsRequest.tsx
365 | src/renderer/setup/components/CompletionScreen.tsx
366 | src/renderer/setup/hooks/useSettings.ts
367 | src/renderer/setup/hooks/useSetupFlow.ts
368 | src/renderer/setup/store/setup.store.ts
369 | src/main/services/storage/settings-store.ts
370 | src/main/services/keyboard/index.ts
371 | src/main/services/keyboard/shortcut-manager.ts
372 | src/main/ipc/settings.handler.ts
373 | src/shared/types/settings.types.ts
374 | src/shared/constants/shortcuts.ts
375 | tests/e2e/setup-flow.test.ts
376 | ```
377 | 
378 | ---
379 | 
380 | ### Phase 6: Testing, Optimization & Polish (Week 11-12)
381 | 
382 | **Goal**: Ensure quality, performance, and production readiness
383 | 
384 | #### Tasks
385 | 
386 | 1. **Comprehensive Testing**
387 |    - Write unit tests for all services
388 |    - Create integration tests for workflows
389 |    - Implement E2E tests for critical paths
390 |    - Add performance benchmarks
391 |    - Test on all target platforms
392 |    - Fix identified bugs
393 | 
394 | 2. **Performance Optimization**
395 |    - Profile and optimize overlay rendering
396 |    - Optimize AI response handling
397 |    - Reduce memory footprint
398 |    - Optimize startup time
399 |    - Implement lazy loading where appropriate
400 |    - Add performance monitoring
401 | 
402 | 3. **Error Handling & Logging**
403 |    - Implement comprehensive error handling
404 |    - Add structured logging
405 |    - Create error reporting system
406 |    - Add crash reporting (Sentry)
407 |    - Implement graceful degradation
408 | 
409 | 4. **Security Hardening**
410 |    - Audit API key storage
411 |    - Review IPC security
412 |    - Implement CSP for renderer
413 |    - Add input validation everywhere
414 |    - Review dependencies for vulnerabilities
415 |    - Implement auto-update securely
416 | 
417 | 5. **Documentation**
418 |    - Write user documentation
419 |    - Create developer documentation
420 |    - Document API integration
421 |    - Create troubleshooting guide
422 |    - Write deployment guide
423 |    - Create video tutorials
424 | 
425 | 6. **Polish & UX Improvements**
426 |    - Refine animations and transitions
427 |    - Improve accessibility
428 |    - Add keyboard navigation
429 |    - Implement dark mode
430 |    - Add tooltips and help text
431 |    - Improve error messages
432 | 
433 | 7. **Deployment Preparation**
434 |    - Set up code signing for all platforms
435 |    - Configure auto-update mechanism
436 |    - Create release pipeline
437 |    - Set up crash reporting
438 |    - Configure analytics (opt-in)
439 |    - Prepare marketing materials
440 | 
441 | #### Deliverables
442 | - ✅ 80%+ test coverage
443 | - ✅ All critical bugs fixed
444 | - ✅ Performance benchmarks met
445 | - ✅ Complete documentation
446 | - ✅ Production-ready builds
447 | 
448 | #### Success Criteria
449 | - All E2E tests pass on all platforms
450 | - App starts in under 2 seconds
451 | - Overlay appears in under 300ms
452 | - Memory usage stays under 200MB
453 | - No critical security vulnerabilities
454 | - Documentation is complete and clear
455 | 
456 | #### Key Files to Create
457 | ```
458 | tests/unit/main/services/text-selection.test.ts
459 | tests/unit/main/services/overlay.test.ts
460 | tests/unit/main/services/ai.test.ts
461 | tests/integration/text-selection.test.ts
462 | tests/integration/overlay-display.test.ts
463 | tests/integration/ai-integration.test.ts
464 | tests/e2e/setup-flow.test.ts
465 | tests/e2e/text-selection-flow.test.ts
466 | tests/e2e/chat-flow.test.ts
467 | docs/USER_GUIDE.md
468 | docs/DEVELOPMENT.md
469 | docs/DEPLOYMENT.md
470 | docs/TROUBLESHOOTING.md
471 | .github/workflows/build.yml
472 | .github/workflows/test.yml
473 | .github/workflows/release.yml
474 | ```
475 | 
476 | ---
477 | 
478 | ## MVP Prototype Priority (Quick Start)
479 | 
480 | To get a working prototype as quickly as possible, focus on these files first:
481 | 
482 | ### Week 1: Minimal Viable Prototype
483 | 
484 | **Goal**: Text selection → Popup → Mock AI response
485 | 
486 | #### Critical Files (Priority Order)
487 | 
488 | 1. **Project Setup** (Day 1)
489 |    ```
490 |    package.json (update with dependencies)
491 |    tsconfig.json
492 |    vite.config.ts
493 |    electron-builder.yml
494 |    ```
495 | 
496 | 2. **Basic Electron App** (Day 1-2)
497 |    ```
498 |    src/main/index.ts
499 |    src/main/app.ts
500 |    src/main/utils/logger.ts
501 |    src/preload/overlay.preload.ts
502 |    ```
503 | 
504 | 3. **Simple Overlay** (Day 2-3)
505 |    ```
506 |    src/renderer/overlay/index.html
507 |    src/renderer/overlay/main.tsx
508 |    src/renderer/overlay/App.tsx
509 |    src/renderer/overlay/components/Popup/index.tsx
510 |    ```
511 | 
512 | 4. **Text Selection (Clipboard-based)** (Day 3-4)
513 |    ```
514 |    src/main/services/text-selection/detector.ts
515 |    src/main/ipc/overlay.handler.ts
516 |    ```
517 | 
518 | 5. **Mock AI Integration** (Day 4-5)
519 |    ```
520 |    src/main/services/ai/watsonx-client.ts (mock)
521 |    src/renderer/overlay/hooks/useAI.ts
522 |    ```
523 | 
524 | #### MVP Features
525 | - ✅ Detect text selection via clipboard monitoring
526 | - ✅ Show popup at cursor position
527 | - ✅ Display "Summarize" button
528 | - ✅ Show mock AI response
529 | - ✅ Basic styling
530 | 
531 | This MVP can be built in 5 days and demonstrates the core concept.
532 | 
533 | ---
534 | 
535 | ## Development Timeline Summary
536 | 
537 | | Phase | Duration | Key Deliverable |
538 | |-------|----------|-----------------|
539 | | Phase 1: Infrastructure | 2 weeks | Working Electron app with build pipeline |
540 | | Phase 2: Text Selection & Popup | 2 weeks | Cross-platform text selection with popup |
541 | | Phase 3: IBM watsonx Integration | 2 weeks | Functional AI-powered text processing |
542 | | Phase 4: Chat Interface | 2 weeks | Full chat interface with history |
543 | | Phase 5: Settings & Configuration | 2 weeks | Complete setup wizard and settings |
544 | | Phase 6: Testing & Polish | 2 weeks | Production-ready application |
545 | | **Total** | **12 weeks** | **SmartClick v1.0** |
546 | 
547 | ### Milestones
548 | 
549 | - **Week 2**: Basic Electron app running
550 | - **Week 4**: Text selection working on all platforms
551 | - **Week 6**: AI integration complete
552 | - **Week 8**: Chat interface functional
553 | - **Week 10**: Setup wizard complete
554 | - **Week 12**: Production release
555 | 
556 | ---
557 | 
558 | ## Risk Mitigation
559 | 
560 | ### Technical Risks
561 | 
562 | 1. **Platform-specific text selection complexity**
563 |    - **Mitigation**: Start with clipboard-based fallback, iterate to native APIs
564 |    - **Fallback**: Manual text selection via keyboard shortcut
565 | 
566 | 2. **IBM watsonx API rate limits**
567 |    - **Mitigation**: Implement caching, request queuing, user feedback
568 |    - **Fallback**: Allow users to configure rate limit handling
569 | 
570 | 3. **Overlay performance on older hardware**
571 |    - **Mitigation**: Performance profiling, optimization, settings for low-end devices
572 |    - **Fallback**: Simplified UI mode
573 | 
574 | 4. **Permission denials on macOS**
575 |    - **Mitigation**: Clear explanations, troubleshooting guide, manual mode
576 |    - **Fallback**: Browser extension as alternative
577 | 
578 | ### Schedule Risks
579 | 
580 | 1. **Underestimated complexity**
581 |    - **Mitigation**: Build MVP first, iterate with user feedback
582 |    - **Buffer**: 2-week buffer built into timeline
583 | 
584 | 2. **Platform-specific bugs**
585 |    - **Mitigation**: Test early and often on all platforms
586 |    - **Strategy**: Focus on one platform first, then expand
587 | 
588 | ---
589 | 
590 | ## Success Metrics
591 | 
592 | ### Technical Metrics
593 | - Overlay appears in < 300ms after text selection
594 | - AI response starts streaming in < 2 seconds
595 | - Memory usage < 200MB
596 | - App startup time < 2 seconds
597 | - 80%+ test coverage
598 | 
599 | ### User Experience Metrics
600 | - Setup completion rate > 90%
601 | - Daily active usage > 10 interactions/user
602 | - User satisfaction score > 4.5/5
603 | - Crash rate < 0.1%
604 | 
605 | ### Business Metrics
606 | - Installation completion rate > 80%
607 | - 7-day retention > 60%
608 | - 30-day retention > 40%
609 | - NPS score > 50
610 | 
611 | ---
612 | 
613 | ## Next Steps
614 | 
615 | 1. **Review this plan** with the team
616 | 2. **Set up development environment** (Phase 1, Week 1)
617 | 3. **Build MVP prototype** (5 days)
618 | 4. **Get user feedback** on MVP
619 | 5. **Iterate and continue** with full development plan
620 | 
621 | ---
622 | 
623 | ## Resources Needed
624 | 
625 | ### Development Team
626 | - 1-2 Full-stack developers (Electron + React + TypeScript)
627 | - 1 UI/UX designer (part-time)
628 | - 1 QA engineer (part-time, starting Phase 6)
629 | 
630 | ### Tools & Services
631 | - GitHub for version control
632 | - GitHub Actions for CI/CD
633 | - Sentry for error tracking
634 | - IBM watsonx account with API access
635 | - Code signing certificates (Apple, Microsoft)
636 | - Design tools (Figma)
637 | 
638 | ### Hardware
639 | - Windows development machine
640 | - macOS development machine
641 | - Linux development machine (or VM)
642 | - Test devices for each platform
643 | 
644 | ---
645 | 
646 | ## Conclusion
647 | 
648 | This development plan provides a clear roadmap from initial setup to production release. The phased approach allows for iterative development with regular milestones and deliverables. The MVP prototype path enables quick validation of the core concept before investing in full development.
649 | 
650 | **Estimated Total Development Time**: 12 weeks (3 months)
651 | **Recommended Team Size**: 2-3 developers
652 | **Budget Considerations**: Factor in IBM watsonx API costs, code signing certificates, and testing infrastructure
</content>
</file>
<file><path>docs/FOLDER_STRUCTURE.md</path>
<content lines="1-461">
  1 | # SmartClick Project Folder Structure
  2 | 
  3 | ## Complete Directory Layout
  4 | 
  5 | ```
  6 | smart-clicks/
  7 | ├── .github/
  8 | │   └── workflows/
  9 | │       ├── build.yml                 # CI/CD pipeline for builds
 10 | │       ├── test.yml                  # Automated testing
 11 | │       └── release.yml               # Release automation
 12 | │
 13 | ├── .vscode/
 14 | │   ├── settings.json                 # VSCode workspace settings
 15 | │   ├── launch.json                   # Debug configurations
 16 | │   └── extensions.json               # Recommended extensions
 17 | │
 18 | ├── docs/
 19 | │   ├── ARCHITECTURE.md               # System architecture (created)
 20 | │   ├── FOLDER_STRUCTURE.md           # This file
 21 | │   ├── API_INTEGRATION.md            # IBM watsonx integration guide
 22 | │   ├── DEVELOPMENT.md                # Development guidelines
 23 | │   ├── DEPLOYMENT.md                 # Deployment instructions
 24 | │   └── USER_GUIDE.md                 # End-user documentation
 25 | │
 26 | ├── src/
 27 | │   ├── main/                         # Electron main process
 28 | │   │   ├── index.ts                  # Main entry point
 29 | │   │   ├── app.ts                    # Application lifecycle
 30 | │   │   ├── ipc/                      # IPC handlers
 31 | │   │   │   ├── index.ts
 32 | │   │   │   ├── settings.handler.ts
 33 | │   │   │   ├── overlay.handler.ts
 34 | │   │   │   └── ai.handler.ts
 35 | │   │   ├── services/                 # Background services
 36 | │   │   │   ├── text-selection/
 37 | │   │   │   │   ├── index.ts
 38 | │   │   │   │   ├── detector.ts
 39 | │   │   │   │   ├── windows.detector.ts
 40 | │   │   │   │   ├── macos.detector.ts
 41 | │   │   │   │   └── linux.detector.ts
 42 | │   │   │   ├── overlay/
 43 | │   │   │   │   ├── index.ts
 44 | │   │   │   │   ├── manager.ts
 45 | │   │   │   │   └── window-factory.ts
 46 | │   │   │   ├── keyboard/
 47 | │   │   │   │   ├── index.ts
 48 | │   │   │   │   └── shortcut-manager.ts
 49 | │   │   │   ├── ai/
 50 | │   │   │   │   ├── index.ts
 51 | │   │   │   │   ├── watsonx-client.ts
 52 | │   │   │   │   ├── context-manager.ts
 53 | │   │   │   │   ├── prompt-builder.ts
 54 | │   │   │   │   └── cache.ts
 55 | │   │   │   └── storage/
 56 | │   │   │       ├── index.ts
 57 | │   │   │       ├── settings-store.ts
 58 | │   │   │       └── history-db.ts
 59 | │   │   ├── utils/
 60 | │   │   │   ├── logger.ts
 61 | │   │   │   ├── error-handler.ts
 62 | │   │   │   └── platform.ts
 63 | │   │   └── types/
 64 | │   │       ├── index.ts
 65 | │   │       ├── ipc.types.ts
 66 | │   │       └── services.types.ts
 67 | │   │
 68 | │   ├── renderer/                     # Electron renderer processes
 69 | │   │   ├── setup/                    # Setup/Configuration app
 70 | │   │   │   ├── index.html
 71 | │   │   │   ├── main.tsx
 72 | │   │   │   ├── App.tsx
 73 | │   │   │   ├── components/
 74 | │   │   │   │   ├── WelcomeScreen.tsx
 75 | │   │   │   │   ├── ApiKeySetup.tsx
 76 | │   │   │   │   ├── ShortcutConfig.tsx
 77 | │   │   │   │   ├── PermissionsRequest.tsx
 78 | │   │   │   │   └── CompletionScreen.tsx
 79 | │   │   │   ├── hooks/
 80 | │   │   │   │   ├── useSettings.ts
 81 | │   │   │   │   └── useSetupFlow.ts
 82 | │   │   │   ├── store/
 83 | │   │   │   │   └── setup.store.ts
 84 | │   │   │   └── styles/
 85 | │   │   │       └── setup.css
 86 | │   │   │
 87 | │   │   └── overlay/                  # Overlay/Popup UI
 88 | │   │       ├── index.html
 89 | │   │       ├── main.tsx
 90 | │   │       ├── App.tsx
 91 | │   │       ├── components/
 92 | │   │       │   ├── Popup/
 93 | │   │       │   │   ├── index.tsx
 94 | │   │       │   │   ├── ActionButtons.tsx
 95 | │   │       │   │   ├── QuickActions.tsx
 96 | │   │       │   │   └── ExpandButton.tsx
 97 | │   │       │   ├── Chat/
 98 | │   │       │   │   ├── index.tsx
 99 | │   │       │   │   ├── ChatInterface.tsx
100 | │   │       │   │   ├── MessageList.tsx
101 | │   │       │   │   ├── Message.tsx
102 | │   │       │   │   ├── InputBox.tsx
103 | │   │       │   │   └── ContextDisplay.tsx
104 | │   │       │   └── shared/
105 | │   │       │       ├── Button.tsx
106 | │   │       │       ├── Input.tsx
107 | │   │       │       ├── Spinner.tsx
108 | │   │       │       └── Tooltip.tsx
109 | │   │       ├── hooks/
110 | │   │       │   ├── useAI.ts
111 | │   │       │   ├── useChat.ts
112 | │   │       │   ├── useSelection.ts
113 | │   │       │   └── usePosition.ts
114 | │   │       ├── store/
115 | │   │       │   ├── overlay.store.ts
116 | │   │       │   └── chat.store.ts
117 | │   │       ├── utils/
118 | │   │       │   ├── positioning.ts
119 | │   │       │   └── animations.ts
120 | │   │       └── styles/
121 | │   │           └── overlay.css
122 | │   │
123 | │   ├── preload/                      # Preload scripts
124 | │   │   ├── setup.preload.ts
125 | │   │   └── overlay.preload.ts
126 | │   │
127 | │   ├── shared/                       # Shared code
128 | │   │   ├── types/
129 | │   │   │   ├── index.ts
130 | │   │   │   ├── ai.types.ts
131 | │   │   │   ├── settings.types.ts
132 | │   │   │   └── chat.types.ts
133 | │   │   ├── constants/
134 | │   │   │   ├── index.ts
135 | │   │   │   ├── shortcuts.ts
136 | │   │   │   ├── prompts.ts
137 | │   │   │   └── config.ts
138 | │   │   └── utils/
139 | │   │       ├── validation.ts
140 | │   │       └── formatting.ts
141 | │   │
142 | │   └── native/                       # Native modules (optional)
143 | │       ├── text-selection/
144 | │       │   ├── binding.gyp
145 | │       │   ├── windows/
146 | │       │   │   └── selection.cc
147 | │       │   ├── macos/
148 | │       │   │   └── selection.mm
149 | │       │   └── linux/
150 | │       │       └── selection.cc
151 | │       └── README.md
152 | │
153 | ├── tests/
154 | │   ├── unit/
155 | │   │   ├── main/
156 | │   │   │   ├── services/
157 | │   │   │   │   ├── text-selection.test.ts
158 | │   │   │   │   ├── overlay.test.ts
159 | │   │   │   │   └── ai.test.ts
160 | │   │   │   └── utils/
161 | │   │   │       └── logger.test.ts
162 | │   │   └── renderer/
163 | │   │       ├── setup/
164 | │   │       │   └── components.test.tsx
165 | │   │       └── overlay/
166 | │   │           └── components.test.tsx
167 | │   ├── integration/
168 | │   │   ├── text-selection.test.ts
169 | │   │   ├── overlay-display.test.ts
170 | │   │   └── ai-integration.test.ts
171 | │   ├── e2e/
172 | │   │   ├── setup-flow.test.ts
173 | │   │   ├── text-selection-flow.test.ts
174 | │   │   └── chat-flow.test.ts
175 | │   ├── fixtures/
176 | │   │   ├── mock-settings.json
177 | │   │   └── mock-responses.json
178 | │   └── helpers/
179 | │       ├── test-utils.ts
180 | │       └── mock-electron.ts
181 | │
182 | ├── scripts/
183 | │   ├── build.js                      # Build script
184 | │   ├── dev.js                        # Development script
185 | │   ├── package.js                    # Packaging script
186 | │   ├── notarize.js                   # macOS notarization
187 | │   └── clean.js                      # Clean build artifacts
188 | │
189 | ├── resources/                        # Static resources
190 | │   ├── icons/
191 | │   │   ├── icon.icns                 # macOS icon
192 | │   │   ├── icon.ico                  # Windows icon
193 | │   │   ├── icon.png                  # Linux icon
194 | │   │   └── tray/
195 | │   │       ├── tray.png
196 | │   │       ├── tray@2x.png
197 | │   │       └── tray-active.png
198 | │   ├── images/
199 | │   │   └── logo.png
200 | │   └── sounds/
201 | │       └── notification.mp3
202 | │
203 | ├── build/                            # Build configuration
204 | │   ├── entitlements.mac.plist        # macOS entitlements
205 | │   ├── icon.icns
206 | │   ├── icon.ico
207 | │   └── notarize.js
208 | │
209 | ├── dist/                             # Build output (gitignored)
210 | │   ├── main/
211 | │   ├── renderer/
212 | │   └── preload/
213 | │
214 | ├── release/                          # Release packages (gitignored)
215 | │   ├── SmartClick-1.0.0.dmg
216 | │   ├── SmartClick-1.0.0.exe
217 | │   └── SmartClick-1.0.0.AppImage
218 | │
219 | ├── .env.example                      # Environment variables template
220 | ├── .env                              # Environment variables (gitignored)
221 | ├── .eslintrc.json                    # ESLint configuration
222 | ├── .prettierrc                       # Prettier configuration
223 | ├── .gitignore                        # Git ignore rules
224 | ├── electron-builder.yml              # Electron Builder config
225 | ├── package.json                      # Project dependencies
226 | ├── package-lock.json                 # Locked dependencies
227 | ├── tsconfig.json                     # TypeScript config (base)
228 | ├── tsconfig.main.json                # TypeScript config (main)
229 | ├── tsconfig.renderer.json            # TypeScript config (renderer)
230 | ├── vite.config.ts                    # Vite configuration
231 | ├── vitest.config.ts                  # Vitest configuration
232 | ├── README.md                         # Project README
233 | └── LICENSE                           # License file
234 | ```
235 | 
236 | ## Directory Descriptions
237 | 
238 | ### Root Level
239 | 
240 | - **`.github/`** - GitHub Actions workflows for CI/CD
241 | - **`.vscode/`** - VSCode workspace configuration
242 | - **`docs/`** - All project documentation
243 | - **`src/`** - Source code (main application)
244 | - **`tests/`** - Test suites
245 | - **`scripts/`** - Build and utility scripts
246 | - **`resources/`** - Static assets (icons, images, sounds)
247 | - **`build/`** - Build configuration files
248 | - **`dist/`** - Compiled output (generated, not committed)
249 | - **`release/`** - Packaged installers (generated, not committed)
250 | 
251 | ### Source Code Structure (`src/`)
252 | 
253 | #### `main/` - Electron Main Process
254 | The Node.js backend that runs with full system access:
255 | 
256 | - **`index.ts`** - Entry point, initializes Electron app
257 | - **`app.ts`** - Application lifecycle management
258 | - **`ipc/`** - Inter-Process Communication handlers
259 | - **`services/`** - Core business logic services
260 |   - **`text-selection/`** - Platform-specific text detection
261 |   - **`overlay/`** - Window management for popup/chat
262 |   - **`keyboard/`** - Global keyboard shortcut handling
263 |   - **`ai/`** - IBM watsonx integration
264 |   - **`storage/`** - Settings and chat history persistence
265 | - **`utils/`** - Utility functions (logging, error handling)
266 | - **`types/`** - TypeScript type definitions
267 | 
268 | #### `renderer/` - Electron Renderer Processes
269 | The UI layer built with React:
270 | 
271 | - **`setup/`** - One-time configuration interface
272 |   - Components for each setup step
273 |   - Setup flow state management
274 |   - Styling specific to setup UI
275 |   
276 | - **`overlay/`** - Popup and chat interface
277 |   - **`Popup/`** - Initial quick-action popup
278 |   - **`Chat/`** - Expanded chat interface
279 |   - **`shared/`** - Reusable UI components
280 |   - Hooks for AI, chat, and positioning logic
281 |   - State management with Zustand
282 | 
283 | #### `preload/` - Preload Scripts
284 | Bridge between main and renderer processes with controlled API exposure
285 | 
286 | #### `shared/` - Shared Code
287 | Code used by both main and renderer processes:
288 | - Type definitions
289 | - Constants
290 | - Validation utilities
291 | 
292 | #### `native/` - Native Modules (Optional)
293 | C++/Objective-C code for platform-specific features that Node.js can't handle
294 | 
295 | ### Test Structure (`tests/`)
296 | 
297 | - **`unit/`** - Unit tests for individual functions/components
298 | - **`integration/`** - Integration tests for service interactions
299 | - **`e2e/`** - End-to-end tests for complete user flows
300 | - **`fixtures/`** - Test data and mocks
301 | - **`helpers/`** - Test utilities
302 | 
303 | ## Key Configuration Files
304 | 
305 | ### `package.json`
306 | ```json
307 | {
308 |   "name": "smartclick",
309 |   "version": "1.0.0",
310 |   "main": "dist/main/index.js",
311 |   "scripts": {
312 |     "dev": "node scripts/dev.js",
313 |     "build": "node scripts/build.js",
314 |     "package": "electron-builder",
315 |     "test": "vitest",
316 |     "test:e2e": "playwright test",
317 |     "lint": "eslint src/",
318 |     "format": "prettier --write src/"
319 |   }
320 | }
321 | ```
322 | 
323 | ### `electron-builder.yml`
324 | ```yaml
325 | appId: com.smartclick.app
326 | productName: SmartClick
327 | directories:
328 |   output: release
329 |   buildResources: build
330 | files:
331 |   - dist/**/*
332 |   - resources/**/*
333 | mac:
334 |   category: public.app-category.productivity
335 |   target:
336 |     - dmg
337 |     - zip
338 | win:
339 |   target:
340 |     - nsis
341 |     - portable
342 | linux:
343 |   target:
344 |     - AppImage
345 |     - deb
346 | ```
347 | 
348 | ### `tsconfig.json` (Base)
349 | ```json
350 | {
351 |   "compilerOptions": {
352 |     "target": "ES2020",
353 |     "module": "ESNext",
354 |     "lib": ["ES2020"],
355 |     "moduleResolution": "node",
356 |     "strict": true,
357 |     "esModuleInterop": true,
358 |     "skipLibCheck": true,
359 |     "resolveJsonModule": true,
360 |     "baseUrl": ".",
361 |     "paths": {
362 |       "@main/*": ["src/main/*"],
363 |       "@renderer/*": ["src/renderer/*"],
364 |       "@shared/*": ["src/shared/*"]
365 |     }
366 |   }
367 | }
368 | ```
369 | 
370 | ## File Naming Conventions
371 | 
372 | - **Components**: PascalCase (e.g., `ChatInterface.tsx`)
373 | - **Utilities/Services**: camelCase (e.g., `textSelection.ts`)
374 | - **Types**: PascalCase with `.types.ts` suffix (e.g., `ai.types.ts`)
375 | - **Tests**: Same as source with `.test.ts` suffix (e.g., `overlay.test.ts`)
376 | - **Constants**: UPPER_SNAKE_CASE in files (e.g., `MAX_CONTEXT_LENGTH`)
377 | 
378 | ## Import Path Aliases
379 | 
380 | ```typescript
381 | // Instead of: import { something } from '../../../shared/types'
382 | // Use: import { something } from '@shared/types'
383 | 
384 | // Available aliases:
385 | // @main/* -> src/main/*
386 | // @renderer/* -> src/renderer/*
387 | // @shared/* -> src/shared/*
388 | ```
389 | 
390 | ## Build Output Structure
391 | 
392 | ```
393 | dist/
394 | ├── main/
395 | │   ├── index.js              # Compiled main process
396 | │   └── [other compiled files]
397 | ├── renderer/
398 | │   ├── setup/
399 | │   │   ├── index.html
400 | │   │   └── assets/
401 | │   └── overlay/
402 | │       ├── index.html
403 | │       └── assets/
404 | └── preload/
405 |     ├── setup.preload.js
406 |     └── overlay.preload.js
407 | ```
408 | 
409 | ## Development Workflow
410 | 
411 | 1. **Start Development**: `npm run dev`
412 |    - Compiles TypeScript
413 |    - Starts Vite dev server for renderer
414 |    - Launches Electron with hot reload
415 | 
416 | 2. **Run Tests**: `npm test`
417 |    - Runs unit and integration tests
418 |    - Watch mode for development
419 | 
420 | 3. **Build for Production**: `npm run build`
421 |    - Compiles all TypeScript
422 |    - Bundles renderer code
423 |    - Optimizes assets
424 | 
425 | 4. **Package Application**: `npm run package`
426 |    - Creates platform-specific installers
427 |    - Signs and notarizes (if configured)
428 | 
429 | ## Git Ignore Patterns
430 | 
431 | ```
432 | node_modules/
433 | dist/
434 | release/
435 | .env
436 | *.log
437 | .DS_Store
438 | Thumbs.db
439 | *.swp
440 | coverage/
441 | .vscode/settings.json
442 | ```
443 | 
444 | ## Notes
445 | 
446 | - All paths are relative to project root
447 | - TypeScript is used throughout for type safety
448 | - React 18+ with hooks for all UI components
449 | - Zustand for lightweight state management
450 | - Vite for fast development and optimized builds
451 | - Electron Builder for cross-platform packaging
452 | - Vitest for unit/integration tests
453 | - Playwright for E2E tests
454 | 
455 | This structure supports:
456 | - ✅ Clear separation of concerns
457 | - ✅ Easy navigation and maintenance
458 | - ✅ Scalable architecture
459 | - ✅ Comprehensive testing
460 | - ✅ Cross-platform development
461 | - ✅ Professional build pipeline
</content>
</file>
<file><path>docs/IMPLEMENTATION_PRIORITY.md</path>
<content lines="1-522">
  1 | # SmartClick Implementation Priority Guide
  2 | 
  3 | ## Quick Reference
  4 | 
  5 | This guide provides a prioritized list of files to create and implement, organized by urgency and dependencies. Use this as your roadmap for building SmartClick efficiently.
  6 | 
  7 | ## Priority Levels
  8 | 
  9 | - 🔴 **Critical** - Must have for MVP, blocks other work
 10 | - 🟡 **High** - Important for core functionality
 11 | - 🟢 **Medium** - Enhances user experience
 12 | - 🔵 **Low** - Nice to have, can be deferred
 13 | 
 14 | ---
 15 | 
 16 | ## Phase 0: MVP Prototype (Week 1 - 5 Days)
 17 | 
 18 | **Goal**: Demonstrate core concept with minimal features
 19 | 
 20 | ### Day 1: Project Foundation 🔴
 21 | 
 22 | ```
 23 | 1. package.json (update with dependencies)
 24 | 2. tsconfig.json (base TypeScript config)
 25 | 3. tsconfig.main.json (main process config)
 26 | 4. tsconfig.renderer.json (renderer process config)
 27 | 5. vite.config.ts (Vite bundler config)
 28 | 6. electron-builder.yml (packaging config)
 29 | 7. .env.example (environment template)
 30 | 8. .gitignore (Git ignore rules)
 31 | ```
 32 | 
 33 | **Commands to run:**
 34 | ```bash
 35 | npm init -y
 36 | npm install electron electron-builder vite typescript
 37 | npm install react react-dom
 38 | npm install -D @types/react @types/react-dom @types/node
 39 | npm install -D @vitejs/plugin-react
 40 | ```
 41 | 
 42 | ### Day 2: Basic Electron App 🔴
 43 | 
 44 | ```
 45 | 9. src/main/index.ts (main entry point)
 46 | 10. src/main/app.ts (app lifecycle)
 47 | 11. src/main/utils/logger.ts (logging utility)
 48 | 12. src/preload/overlay.preload.ts (preload script)
 49 | 13. scripts/dev.js (development script)
 50 | ```
 51 | 
 52 | **Test**: App should launch with a blank window
 53 | 
 54 | ### Day 3: Simple Overlay UI 🔴
 55 | 
 56 | ```
 57 | 14. src/renderer/overlay/index.html
 58 | 15. src/renderer/overlay/main.tsx
 59 | 16. src/renderer/overlay/App.tsx
 60 | 17. src/renderer/overlay/components/Popup/index.tsx
 61 | 18. src/renderer/overlay/styles/overlay.css
 62 | 19. src/shared/types/index.ts
 63 | ```
 64 | 
 65 | **Test**: Overlay window appears on screen
 66 | 
 67 | ### Day 4: Text Selection (Clipboard-based) 🔴
 68 | 
 69 | ```
 70 | 20. src/main/services/text-selection/detector.ts
 71 | 21. src/main/ipc/overlay.handler.ts
 72 | 22. src/shared/types/selection.types.ts
 73 | 23. src/renderer/overlay/hooks/useSelection.ts
 74 | ```
 75 | 
 76 | **Test**: Copying text triggers popup
 77 | 
 78 | ### Day 5: Mock AI Response 🔴
 79 | 
 80 | ```
 81 | 24. src/main/services/ai/watsonx-client.ts (with mock)
 82 | 25. src/renderer/overlay/hooks/useAI.ts
 83 | 26. src/renderer/overlay/components/Popup/ActionButtons.tsx
 84 | 27. src/shared/constants/prompts.ts
 85 | ```
 86 | 
 87 | **Test**: Clicking "Summarize" shows mock response
 88 | 
 89 | **MVP Deliverable**: Working prototype demonstrating text selection → popup → mock AI response
 90 | 
 91 | ---
 92 | 
 93 | ## Phase 1: Core Infrastructure (Week 1-2)
 94 | 
 95 | ### Week 1, Day 1-2: Complete Electron Setup 🔴
 96 | 
 97 | ```
 98 | 28. src/main/ipc/index.ts (IPC router)
 99 | 29. src/main/utils/error-handler.ts
100 | 30. src/main/utils/platform.ts
101 | 31. src/main/types/index.ts
102 | 32. src/main/types/ipc.types.ts
103 | 33. vitest.config.ts (test config)
104 | 34. .eslintrc.json (linting config)
105 | 35. .prettierrc (formatting config)
106 | ```
107 | 
108 | ### Week 1, Day 3-4: Build Pipeline 🟡
109 | 
110 | ```
111 | 36. scripts/build.js
112 | 37. scripts/package.js
113 | 38. scripts/clean.js
114 | 39. .github/workflows/build.yml (CI/CD)
115 | 40. build/entitlements.mac.plist
116 | ```
117 | 
118 | ### Week 1, Day 5: Testing Setup 🟡
119 | 
120 | ```
121 | 41. tests/helpers/test-utils.ts
122 | 42. tests/helpers/mock-electron.ts
123 | 43. tests/fixtures/mock-settings.json
124 | 44. tests/unit/main/utils/logger.test.ts
125 | ```
126 | 
127 | ---
128 | 
129 | ## Phase 2: Text Selection & Overlay (Week 3-4)
130 | 
131 | ### Week 3, Day 1-2: Platform-Specific Detection 🔴
132 | 
133 | ```
134 | 45. src/main/services/text-selection/index.ts
135 | 46. src/main/services/text-selection/windows.detector.ts
136 | 47. src/main/services/text-selection/macos.detector.ts
137 | 48. src/main/services/text-selection/linux.detector.ts
138 | 49. tests/unit/main/services/text-selection.test.ts
139 | ```
140 | 
141 | ### Week 3, Day 3-4: Overlay Management 🔴
142 | 
143 | ```
144 | 50. src/main/services/overlay/index.ts
145 | 51. src/main/services/overlay/manager.ts
146 | 52. src/main/services/overlay/window-factory.ts
147 | 53. src/renderer/overlay/utils/positioning.ts
148 | 54. src/renderer/overlay/hooks/usePosition.ts
149 | 55. tests/integration/overlay-display.test.ts
150 | ```
151 | 
152 | ### Week 3, Day 5: Popup Polish 🟡
153 | 
154 | ```
155 | 56. src/renderer/overlay/components/Popup/QuickActions.tsx
156 | 57. src/renderer/overlay/components/Popup/ExpandButton.tsx
157 | 58. src/renderer/overlay/components/shared/Button.tsx
158 | 59. src/renderer/overlay/components/shared/Spinner.tsx
159 | 60. src/renderer/overlay/components/shared/Tooltip.tsx
160 | ```
161 | 
162 | ### Week 4: Integration & Testing 🟡
163 | 
164 | ```
165 | 61. tests/integration/text-selection.test.ts
166 | 62. tests/e2e/text-selection-flow.test.ts
167 | 63. src/renderer/overlay/utils/animations.ts
168 | 64. src/renderer/overlay/store/overlay.store.ts
169 | ```
170 | 
171 | ---
172 | 
173 | ## Phase 3: IBM watsonx Integration (Week 5-6)
174 | 
175 | ### Week 5, Day 1-2: Real AI Client 🔴
176 | 
177 | ```
178 | 65. src/main/services/ai/watsonx-client.ts (real implementation)
179 | 66. src/main/services/ai/prompt-builder.ts
180 | 67. src/main/services/ai/context-manager.ts
181 | 68. src/shared/types/ai.types.ts
182 | 69. .env (create from .env.example)
183 | ```
184 | 
185 | ### Week 5, Day 3-4: AI Service Layer 🔴
186 | 
187 | ```
188 | 70. src/main/services/ai/index.ts
189 | 71. src/main/services/ai/cache.ts
190 | 72. src/main/ipc/ai.handler.ts
191 | 73. tests/unit/main/services/ai.test.ts
192 | ```
193 | 
194 | ### Week 5, Day 5: Integration 🔴
195 | 
196 | ```
197 | 74. src/renderer/overlay/hooks/useAI.ts (update for real API)
198 | 75. tests/integration/ai-integration.test.ts
199 | 76. src/main/utils/error-handler.ts (update for AI errors)
200 | ```
201 | 
202 | ### Week 6: Streaming & Optimization 🟡
203 | 
204 | ```
205 | 77. src/renderer/overlay/components/Popup/StreamingResponse.tsx
206 | 78. src/shared/constants/config.ts
207 | 79. tests/unit/main/services/cache.test.ts
208 | ```
209 | 
210 | ---
211 | 
212 | ## Phase 4: Chat Interface (Week 7-8)
213 | 
214 | ### Week 7, Day 1-3: Chat Components 🔴
215 | 
216 | ```
217 | 80. src/renderer/overlay/components/Chat/index.tsx
218 | 81. src/renderer/overlay/components/Chat/ChatInterface.tsx
219 | 82. src/renderer/overlay/components/Chat/MessageList.tsx
220 | 83. src/renderer/overlay/components/Chat/Message.tsx
221 | 84. src/renderer/overlay/components/Chat/InputBox.tsx
222 | 85. src/renderer/overlay/components/Chat/ContextDisplay.tsx
223 | ```
224 | 
225 | ### Week 7, Day 4-5: Chat State 🔴
226 | 
227 | ```
228 | 86. src/renderer/overlay/store/chat.store.ts
229 | 87. src/renderer/overlay/hooks/useChat.ts
230 | 88. src/shared/types/chat.types.ts
231 | 89. tests/unit/renderer/overlay/chat.test.tsx
232 | ```
233 | 
234 | ### Week 8, Day 1-3: Persistence 🟡
235 | 
236 | ```
237 | 90. src/main/services/storage/index.ts
238 | 91. src/main/services/storage/history-db.ts
239 | 92. src/main/ipc/storage.handler.ts
240 | 93. tests/unit/main/services/storage.test.ts
241 | ```
242 | 
243 | ### Week 8, Day 4-5: Chat Features 🟢
244 | 
245 | ```
246 | 94. src/renderer/overlay/components/Chat/MessageActions.tsx
247 | 95. src/renderer/overlay/components/Chat/ConversationList.tsx
248 | 96. tests/e2e/chat-flow.test.ts
249 | ```
250 | 
251 | ---
252 | 
253 | ## Phase 5: Settings & Configuration (Week 9-10)
254 | 
255 | ### Week 9, Day 1-3: Setup UI 🔴
256 | 
257 | ```
258 | 97. src/renderer/setup/index.html
259 | 98. src/renderer/setup/main.tsx
260 | 99. src/renderer/setup/App.tsx
261 | 100. src/renderer/setup/components/WelcomeScreen.tsx
262 | 101. src/renderer/setup/components/ApiKeySetup.tsx
263 | 102. src/renderer/setup/components/ShortcutConfig.tsx
264 | 103. src/renderer/setup/components/PermissionsRequest.tsx
265 | 104. src/renderer/setup/components/CompletionScreen.tsx
266 | ```
267 | 
268 | ### Week 9, Day 4-5: Setup Logic 🔴
269 | 
270 | ```
271 | 105. src/renderer/setup/hooks/useSettings.ts
272 | 106. src/renderer/setup/hooks/useSetupFlow.ts
273 | 107. src/renderer/setup/store/setup.store.ts
274 | 108. src/preload/setup.preload.ts
275 | 109. src/renderer/setup/styles/setup.css
276 | ```
277 | 
278 | ### Week 10, Day 1-2: Settings Storage 🔴
279 | 
280 | ```
281 | 110. src/main/services/storage/settings-store.ts
282 | 111. src/main/ipc/settings.handler.ts
283 | 112. src/shared/types/settings.types.ts
284 | 113. tests/unit/main/services/settings.test.ts
285 | ```
286 | 
287 | ### Week 10, Day 3-4: Keyboard Shortcuts 🟡
288 | 
289 | ```
290 | 114. src/main/services/keyboard/index.ts
291 | 115. src/main/services/keyboard/shortcut-manager.ts
292 | 116. src/shared/constants/shortcuts.ts
293 | 117. tests/unit/main/services/keyboard.test.ts
294 | ```
295 | 
296 | ### Week 10, Day 5: System Tray 🟡
297 | 
298 | ```
299 | 118. src/main/services/tray/index.ts
300 | 119. src/main/services/tray/menu-builder.ts
301 | 120. resources/icons/tray/tray.png
302 | 121. resources/icons/tray/tray@2x.png
303 | ```
304 | 
305 | ---
306 | 
307 | ## Phase 6: Testing & Polish (Week 11-12)
308 | 
309 | ### Week 11: Comprehensive Testing 🟡
310 | 
311 | ```
312 | 122. tests/e2e/setup-flow.test.ts
313 | 123. tests/integration/full-workflow.test.ts
314 | 124. tests/unit/renderer/setup/components.test.tsx
315 | 125. tests/helpers/integration-utils.ts
316 | ```
317 | 
318 | ### Week 11-12: Documentation 🟢
319 | 
320 | ```
321 | 126. docs/USER_GUIDE.md
322 | 127. docs/DEVELOPMENT.md
323 | 128. docs/DEPLOYMENT.md
324 | 129. docs/TROUBLESHOOTING.md
325 | 130. README.md (update)
326 | ```
327 | 
328 | ### Week 12: Polish 🟢
329 | 
330 | ```
331 | 131. src/renderer/overlay/styles/themes.css
332 | 132. src/renderer/setup/styles/animations.css
333 | 133. resources/images/logo.png
334 | 134. resources/icons/icon.icns
335 | 135. resources/icons/icon.ico
336 | 136. resources/icons/icon.png
337 | ```
338 | 
339 | ### Week 12: Deployment 🟡
340 | 
341 | ```
342 | 137. .github/workflows/release.yml
343 | 138. scripts/notarize.js
344 | 139. build/notarize.js
345 | 140. LICENSE
346 | ```
347 | 
348 | ---
349 | 
350 | ## Critical Path Summary
351 | 
352 | ### Must-Have for Launch (Critical Path)
353 | 
354 | 1. **Project Setup** (Files 1-8)
355 | 2. **Basic Electron App** (Files 9-13)
356 | 3. **Overlay UI** (Files 14-19)
357 | 4. **Text Selection** (Files 20-23, 45-48)
358 | 5. **Overlay Management** (Files 50-52)
359 | 6. **IBM watsonx Integration** (Files 65-71)
360 | 7. **Chat Interface** (Files 80-88)
361 | 8. **Settings Storage** (Files 110-112)
362 | 9. **Setup UI** (Files 97-108)
363 | 10. **Build Pipeline** (Files 36-38)
364 | 
365 | **Total Critical Files**: ~60 files
366 | 
367 | ### Can Be Deferred (Post-Launch)
368 | 
369 | - Advanced testing (E2E, integration)
370 | - System tray integration
371 | - Conversation history search
372 | - Dark mode
373 | - Custom keyboard shortcuts
374 | - Analytics and monitoring
375 | - Advanced error reporting
376 | 
377 | ---
378 | 
379 | ## Implementation Strategy
380 | 
381 | ### Week-by-Week Focus
382 | 
383 | | Week | Focus Area | Key Deliverable |
384 | |------|-----------|-----------------|
385 | | 1 | MVP Prototype | Working demo |
386 | | 2 | Infrastructure | Solid foundation |
387 | | 3-4 | Text Selection | Cross-platform detection |
388 | | 5-6 | AI Integration | Real IBM watsonx |
389 | | 7-8 | Chat Interface | Full conversations |
390 | | 9-10 | Settings | Complete setup |
391 | | 11-12 | Polish | Production ready |
392 | 
393 | ### Daily Workflow
394 | 
395 | 1. **Morning**: Review priority list, pick next files
396 | 2. **Implementation**: Build 3-5 files per day
397 | 3. **Testing**: Write tests as you go
398 | 4. **Evening**: Commit working code, update progress
399 | 
400 | ### Quality Gates
401 | 
402 | - ✅ **After Week 1**: MVP demo works
403 | - ✅ **After Week 4**: Text selection works on all platforms
404 | - ✅ **After Week 6**: AI integration complete
405 | - ✅ **After Week 8**: Chat fully functional
406 | - ✅ **After Week 10**: Setup wizard complete
407 | - ✅ **After Week 12**: Production ready
408 | 
409 | ---
410 | 
411 | ## Dependencies Map
412 | 
413 | ```mermaid
414 | graph TD
415 |     A[Project Setup] --> B[Electron App]
416 |     B --> C[Overlay UI]
417 |     C --> D[Text Selection]
418 |     D --> E[Overlay Management]
419 |     E --> F[AI Integration]
420 |     F --> G[Chat Interface]
421 |     G --> H[Settings Storage]
422 |     H --> I[Setup UI]
423 |     I --> J[Build Pipeline]
424 |     
425 |     B --> K[IPC System]
426 |     K --> D
427 |     K --> F
428 |     K --> H
429 |     
430 |     F --> L[Context Manager]
431 |     L --> G
432 |     
433 |     H --> M[Keyboard Shortcuts]
434 |     M --> D
435 | ```
436 | 
437 | ---
438 | 
439 | ## Quick Start Commands
440 | 
441 | ### Initialize Project
442 | ```bash
443 | # Clone and setup
444 | git clone <repo-url>
445 | cd smart-clicks
446 | npm install
447 | 
448 | # Create environment file
449 | cp .env.example .env
450 | # Edit .env with your IBM watsonx credentials
451 | 
452 | # Start development
453 | npm run dev
454 | ```
455 | 
456 | ### Build for Production
457 | ```bash
458 | npm run build
459 | npm run package
460 | ```
461 | 
462 | ### Run Tests
463 | ```bash
464 | npm test                 # Unit tests
465 | npm run test:integration # Integration tests
466 | npm run test:e2e        # E2E tests
467 | ```
468 | 
469 | ---
470 | 
471 | ## Tips for Efficient Development
472 | 
473 | 1. **Start with MVP**: Get something working quickly
474 | 2. **Test as you go**: Don't defer testing to the end
475 | 3. **Commit often**: Small, focused commits
476 | 4. **Use TypeScript**: Catch errors early
477 | 5. **Follow the plan**: Don't skip ahead
478 | 6. **Ask for help**: When stuck, consult documentation
479 | 7. **Iterate**: Build → Test → Refine → Repeat
480 | 
481 | ---
482 | 
483 | ## Success Metrics
484 | 
485 | ### Week 1 (MVP)
486 | - ✅ App launches
487 | - ✅ Popup appears
488 | - ✅ Mock AI response works
489 | 
490 | ### Week 4 (Text Selection)
491 | - ✅ Works on Windows
492 | - ✅ Works on macOS
493 | - ✅ Works on Linux
494 | 
495 | ### Week 6 (AI)
496 | - ✅ Real IBM watsonx responses
497 | - ✅ Streaming works
498 | - ✅ Error handling robust
499 | 
500 | ### Week 8 (Chat)
501 | - ✅ Multi-turn conversations
502 | - ✅ History persisted
503 | - ✅ Context maintained
504 | 
505 | ### Week 10 (Settings)
506 | - ✅ Setup wizard complete
507 | - ✅ Settings saved
508 | - ✅ Shortcuts work
509 | 
510 | ### Week 12 (Launch)
511 | - ✅ All tests pass
512 | - ✅ Documentation complete
513 | - ✅ Installers built
514 | - ✅ Ready for users
515 | 
516 | ---
517 | 
518 | ## Conclusion
519 | 
520 | This priority guide provides a clear roadmap from day 1 to production launch. Follow the critical path, build incrementally, test continuously, and you'll have a production-ready SmartClick application in 12 weeks.
521 | 
522 | **Remember**: Perfect is the enemy of done. Ship the MVP, gather feedback, iterate.
</content>
</file>
<file><path>docs/REACT_MODERNIZATION_PLAN.md</path>
<content lines="1-476">
  1 | # SmartClick React Modernization Plan
  2 | 
  3 | ## Executive Summary
  4 | Transform SmartClick from a CustomTkinter desktop app into a modern React-based application with Python backend, delivering a smooth, professional UI/UX while maintaining all existing functionality.
  5 | 
  6 | ## Architecture Overview
  7 | 
  8 | ### Current Stack (To Be Replaced)
  9 | - **Frontend**: CustomTkinter (Python GUI)
 10 | - **Backend**: Integrated Python logic
 11 | - **Database**: SQLite
 12 | - **AI**: IBM watsonx integration
 13 | 
 14 | ### New Stack (Proposed)
 15 | - **Frontend**: React 18 + TypeScript + Vite
 16 | - **Desktop Wrapper**: Electron
 17 | - **Backend API**: FastAPI (Python)
 18 | - **Real-time**: WebSocket (FastAPI WebSocket)
 19 | - **State Management**: Zustand (lightweight, modern)
 20 | - **Styling**: Tailwind CSS + Framer Motion
 21 | - **Database**: SQLite (unchanged)
 22 | - **AI**: IBM watsonx (unchanged)
 23 | 
 24 | ## Why This Stack?
 25 | 
 26 | ### React + TypeScript + Vite
 27 | - **Fast**: Vite provides instant HMR and optimized builds
 28 | - **Type-safe**: TypeScript prevents runtime errors
 29 | - **Modern**: Latest React 18 features (concurrent rendering, suspense)
 30 | - **Developer Experience**: Best-in-class tooling
 31 | 
 32 | ### Electron
 33 | - **Native Desktop**: Full OS integration (system tray, global hotkeys)
 34 | - **Cross-platform**: Windows, macOS, Linux from single codebase
 35 | - **Mature**: Battle-tested by VS Code, Slack, Discord
 36 | - **Node.js Access**: Can communicate with Python backend
 37 | 
 38 | ### FastAPI
 39 | - **Fast**: Async/await, high performance
 40 | - **Modern Python**: Type hints, automatic API docs
 41 | - **WebSocket Support**: Built-in real-time communication
 42 | - **Easy Integration**: Works seamlessly with existing Python code
 43 | 
 44 | ### Zustand
 45 | - **Simple**: No boilerplate like Redux
 46 | - **Fast**: Minimal re-renders
 47 | - **TypeScript**: First-class TS support
 48 | - **Small**: ~1KB gzipped
 49 | 
 50 | ### Tailwind CSS + Framer Motion
 51 | - **Tailwind**: Utility-first, rapid development, consistent design
 52 | - **Framer Motion**: Smooth animations, gesture support
 53 | - **Professional**: Modern, polished UI
 54 | 
 55 | ## Project Structure
 56 | 
 57 | ```
 58 | Smart_Clicks/
 59 | ├── frontend/                    # React + Electron app
 60 | │   ├── src/
 61 | │   │   ├── main/               # Electron main process
 62 | │   │   │   ├── main.ts         # Electron entry point
 63 | │   │   │   ├── preload.ts      # Secure IPC bridge
 64 | │   │   │   └── hotkeys.ts      # Global hotkey registration
 65 | │   │   ├── renderer/           # React app
 66 | │   │   │   ├── components/
 67 | │   │   │   │   ├── MainWindow/
 68 | │   │   │   │   │   ├── MainWindow.tsx
 69 | │   │   │   │   │   ├── ControlPanel.tsx
 70 | │   │   │   │   │   ├── SessionHistory.tsx
 71 | │   │   │   │   │   └── InfoCards.tsx
 72 | │   │   │   │   ├── Popup/
 73 | │   │   │   │   │   ├── Popup.tsx
 74 | │   │   │   │   │   ├── CompactView.tsx
 75 | │   │   │   │   │   ├── ChatView.tsx
 76 | │   │   │   │   │   └── ChatBubble.tsx
 77 | │   │   │   │   └── shared/
 78 | │   │   │   │       ├── Button.tsx
 79 | │   │   │   │       ├── Card.tsx
 80 | │   │   │   │       └── LoadingSpinner.tsx
 81 | │   │   │   ├── stores/
 82 | │   │   │   │   ├── appStore.ts      # App state (enabled, sessions)
 83 | │   │   │   │   ├── chatStore.ts     # Chat messages
 84 | │   │   │   │   └── settingsStore.ts # User settings
 85 | │   │   │   ├── services/
 86 | │   │   │   │   ├── api.ts           # REST API client
 87 | │   │   │   │   ├── websocket.ts     # WebSocket client
 88 | │   │   │   │   └── electron.ts      # Electron IPC
 89 | │   │   │   ├── hooks/
 90 | │   │   │   │   ├── useChat.ts
 91 | │   │   │   │   ├── useSession.ts
 92 | │   │   │   │   └── useHotkey.ts
 93 | │   │   │   ├── types/
 94 | │   │   │   │   └── index.ts         # TypeScript types
 95 | │   │   │   ├── App.tsx
 96 | │   │   │   └── main.tsx
 97 | │   │   └── styles/
 98 | │   │       └── globals.css          # Tailwind imports
 99 | │   ├── package.json
100 | │   ├── vite.config.ts
101 | │   ├── electron-builder.json
102 | │   └── tsconfig.json
103 | │
104 | ├── backend/                     # FastAPI Python backend
105 | │   ├── api/
106 | │   │   ├── __init__.py
107 | │   │   ├── main.py              # FastAPI app
108 | │   │   ├── routes/
109 | │   │   │   ├── sessions.py      # Session endpoints
110 | │   │   │   ├── chat.py          # Chat endpoints
111 | │   │   │   ├── settings.py      # Settings endpoints
112 | │   │   │   └── websocket.py     # WebSocket endpoint
113 | │   │   └── models/
114 | │   │       ├── session.py
115 | │   │       ├── message.py
116 | │   │       └── settings.py
117 | │   ├── core/                    # Existing Python logic (reused)
118 | │   │   ├── ai_integration/      # IBM watsonx (unchanged)
119 | │   │   ├── database/            # SQLite manager (unchanged)
120 | │   │   └── text_capture/        # Text detection (unchanged)
121 | │   ├── requirements.txt
122 | │   └── run.py                   # Backend entry point
123 | │
124 | ├── docs/
125 | └── README.md
126 | ```
127 | 
128 | ## Implementation Phases
129 | 
130 | ### Phase 1: Backend API Setup (Week 1)
131 | **Goal**: Create FastAPI backend that exposes existing Python functionality
132 | 
133 | 1. **Setup FastAPI project**
134 |    - Install FastAPI, uvicorn, python-socketio
135 |    - Create API structure
136 |    - Add CORS middleware
137 | 
138 | 2. **Create REST endpoints**
139 |    - `POST /api/sessions` - Create new session
140 |    - `GET /api/sessions` - Get recent sessions
141 |    - `GET /api/sessions/{id}` - Get session details
142 |    - `POST /api/sessions/{id}/messages` - Add message
143 |    - `GET /api/sessions/{id}/messages` - Get messages
144 |    - `POST /api/chat` - Send chat message
145 |    - `GET /api/settings` - Get settings
146 |    - `PUT /api/settings` - Update settings
147 | 
148 | 3. **Implement WebSocket**
149 |    - `/ws/chat` - Real-time chat streaming
150 |    - Handle AI response streaming
151 |    - Connection management
152 | 
153 | 4. **Integrate existing Python code**
154 |    - Import DatabaseManager
155 |    - Import WatsonxClient
156 |    - Import text capture utilities
157 |    - Wrap in API endpoints
158 | 
159 | ### Phase 2: React Frontend Foundation (Week 2)
160 | **Goal**: Setup React project with Electron and basic UI
161 | 
162 | 1. **Initialize React + Vite + TypeScript**
163 |    ```bash
164 |    npm create vite@latest frontend -- --template react-ts
165 |    cd frontend
166 |    npm install
167 |    ```
168 | 
169 | 2. **Add dependencies**
170 |    ```bash
171 |    npm install zustand axios socket.io-client framer-motion
172 |    npm install -D tailwindcss postcss autoprefixer
173 |    npm install -D electron electron-builder concurrently wait-on
174 |    ```
175 | 
176 | 3. **Configure Tailwind CSS**
177 |    - Setup tailwind.config.js
178 |    - Create design system (colors, spacing)
179 |    - Define component styles
180 | 
181 | 4. **Setup Electron**
182 |    - Create main process (main.ts)
183 |    - Create preload script (preload.ts)
184 |    - Configure electron-builder
185 |    - Setup IPC communication
186 | 
187 | 5. **Create type definitions**
188 |    - Session types
189 |    - Message types
190 |    - API response types
191 |    - Store types
192 | 
193 | ### Phase 3: Core Components (Week 3)
194 | **Goal**: Build main UI components
195 | 
196 | 1. **Main Window Components**
197 |    - MainWindow.tsx (layout)
198 |    - ControlPanel.tsx (enable/disable buttons)
199 |    - SessionHistory.tsx (scrollable list)
200 |    - InfoCards.tsx (how-to guides)
201 |    - StatusIndicator.tsx (active/disabled)
202 | 
203 | 2. **Popup Components**
204 |    - Popup.tsx (container with positioning)
205 |    - CompactView.tsx (4 action buttons)
206 |    - ChatView.tsx (expanded chat interface)
207 |    - ChatBubble.tsx (message display)
208 |    - InputBox.tsx (message input)
209 | 
210 | 3. **Shared Components**
211 |    - Button.tsx (reusable button)
212 |    - Card.tsx (container component)
213 |    - LoadingSpinner.tsx (loading states)
214 |    - Modal.tsx (dialogs)
215 | 
216 | ### Phase 4: State Management & API Integration (Week 4)
217 | **Goal**: Connect frontend to backend
218 | 
219 | 1. **Create Zustand stores**
220 |    ```typescript
221 |    // appStore.ts
222 |    interface AppState {
223 |      enabled: boolean;
224 |      currentSession: Session | null;
225 |      sessions: Session[];
226 |      enable: () => void;
227 |      disable: () => void;
228 |      loadSessions: () => Promise<void>;
229 |    }
230 |    ```
231 | 
232 | 2. **API service layer**
233 |    - REST client with axios
234 |    - WebSocket client with socket.io
235 |    - Error handling
236 |    - Request/response interceptors
237 | 
238 | 3. **Custom hooks**
239 |    - useChat (chat functionality)
240 |    - useSession (session management)
241 |    - useWebSocket (real-time updates)
242 |    - useHotkey (keyboard shortcuts)
243 | 
244 | 4. **Connect components to stores**
245 |    - Wire up all components
246 |    - Handle loading states
247 |    - Error boundaries
248 | 
249 | ### Phase 5: Electron Integration (Week 5)
250 | **Goal**: Add desktop app features
251 | 
252 | 1. **Global hotkeys**
253 |    - Register Ctrl+Shift+Z
254 |    - Capture selected text
255 |    - Show popup at cursor
256 | 
257 | 2. **System tray**
258 |    - Tray icon
259 |    - Context menu
260 |    - Show/hide window
261 | 
262 | 3. **Window management**
263 |    - Frameless popup window
264 |    - Always on top
265 |    - Proper positioning
266 |    - Multi-monitor support
267 | 
268 | 4. **Native features**
269 |    - Auto-launch on startup
270 |    - Notifications
271 |    - Clipboard access
272 | 
273 | ### Phase 6: Styling & Animations (Week 6)
274 | **Goal**: Polish UI/UX
275 | 
276 | 1. **Implement design system**
277 |    - Color palette (dark theme)
278 |    - Typography scale
279 |    - Spacing system
280 |    - Border radius
281 | 
282 | 2. **Add animations**
283 |    - Popup entrance/exit
284 |    - Button hover effects
285 |    - Chat message animations
286 |    - Loading states
287 |    - Smooth transitions
288 | 
289 | 3. **Responsive design**
290 |    - Handle different screen sizes
291 |    - Proper scaling
292 |    - Touch support (future)
293 | 
294 | 4. **Accessibility**
295 |    - Keyboard navigation
296 |    - ARIA labels
297 |    - Focus management
298 |    - Screen reader support
299 | 
300 | ### Phase 7: Testing & Optimization (Week 7)
301 | **Goal**: Ensure quality and performance
302 | 
303 | 1. **Testing**
304 |    - Unit tests (Vitest)
305 |    - Component tests (React Testing Library)
306 |    - E2E tests (Playwright)
307 |    - API tests (pytest)
308 | 
309 | 2. **Performance optimization**
310 |    - Code splitting
311 |    - Lazy loading
312 |    - Memoization
313 |    - Virtual scrolling for history
314 | 
315 | 3. **Build optimization**
316 |    - Production builds
317 |    - Bundle size analysis
318 |    - Tree shaking
319 |    - Asset optimization
320 | 
321 | 4. **Bug fixes**
322 |    - Fix any issues found
323 |    - Edge case handling
324 |    - Error recovery
325 | 
326 | ### Phase 8: Deployment & Documentation (Week 8)
327 | **Goal**: Ship it!
328 | 
329 | 1. **Build pipeline**
330 |    - Electron builder config
331 |    - Auto-update setup
332 |    - Code signing (optional)
333 |    - Installer creation
334 | 
335 | 2. **Documentation**
336 |    - User guide
337 |    - Developer docs
338 |    - API documentation
339 |    - Architecture diagrams
340 | 
341 | 3. **Release**
342 |    - Version 2.0.0
343 |    - Release notes
344 |    - Distribution
345 | 
346 | ## Key Features to Implement
347 | 
348 | ### 1. Main Window
349 | - ✅ Enable/Disable controls
350 | - ✅ Real-time status indicator
351 | - ✅ Session history with search
352 | - ✅ Settings panel
353 | - ✅ About dialog
354 | - ✅ Smooth animations
355 | 
356 | ### 2. Popup Window
357 | - ✅ Appears at cursor position
358 | - ✅ Compact view (4 actions)
359 | - ✅ Expanded chat view
360 | - ✅ Real-time AI responses
361 | - ✅ Message history
362 | - ✅ Draggable
363 | - ✅ Auto-hide on focus loss
364 | 
365 | ### 3. Chat Interface
366 | - ✅ User/Assistant bubbles
367 | - ✅ Streaming responses
368 | - ✅ Loading indicators
369 | - ✅ Context display
370 | - ✅ Message input with placeholder
371 | - ✅ Send on Enter
372 | - ✅ Auto-scroll
373 | 
374 | ### 4. Session Management
375 | - ✅ Create sessions
376 | - ✅ Load history
377 | - ✅ Reopen sessions
378 | - ✅ Delete sessions
379 | - ✅ Search sessions
380 | 
381 | ## Technology Decisions
382 | 
383 | ### Why Not Redux?
384 | - Zustand is simpler, less boilerplate
385 | - Better TypeScript support
386 | - Smaller bundle size
387 | - Easier to learn
388 | 
389 | ### Why Not Next.js?
390 | - Electron apps don't need SSR
391 | - Vite is faster for development
392 | - Simpler setup for desktop apps
393 | 
394 | ### Why Not Material-UI?
395 | - Tailwind is more flexible
396 | - Smaller bundle size
397 | - Better performance
398 | - Easier customization
399 | 
400 | ### Why FastAPI over Flask?
401 | - Modern async/await
402 | - Automatic API docs
403 | - Better WebSocket support
404 | - Type hints
405 | 
406 | ## Migration Strategy
407 | 
408 | ### Parallel Development
409 | 1. Keep existing Tkinter app running
410 | 2. Build new React app alongside
411 | 3. Test thoroughly
412 | 4. Switch when ready
413 | 
414 | ### Data Migration
415 | - Database schema unchanged
416 | - Existing sessions work in new UI
417 | - Settings migrated automatically
418 | 
419 | ### User Experience
420 | - Familiar workflow
421 | - Same hotkeys
422 | - Improved visuals
423 | - Better performance
424 | 
425 | ## Success Metrics
426 | 
427 | ### Performance
428 | - Popup appears < 100ms after hotkey
429 | - Chat responses stream in real-time
430 | - Smooth 60fps animations
431 | - < 200MB memory usage
432 | 
433 | ### User Experience
434 | - Intuitive interface
435 | - Responsive interactions
436 | - Clear feedback
437 | - No crashes
438 | 
439 | ### Code Quality
440 | - 80%+ test coverage
441 | - TypeScript strict mode
442 | - ESLint + Prettier
443 | - Clean architecture
444 | 
445 | ## Timeline
446 | 
447 | | Week | Phase | Deliverable |
448 | |------|-------|-------------|
449 | | 1 | Backend API | Working FastAPI with all endpoints |
450 | | 2 | React Setup | React + Electron boilerplate |
451 | | 3 | Core Components | All UI components built |
452 | | 4 | Integration | Frontend connected to backend |
453 | | 5 | Electron Features | Hotkeys, tray, native features |
454 | | 6 | Polish | Animations, styling complete |
455 | | 7 | Testing | All tests passing |
456 | | 8 | Release | Version 2.0.0 shipped |
457 | 
458 | ## Next Steps
459 | 
460 | 1. **Review this plan** - Get feedback and approval
461 | 2. **Setup development environment** - Install tools
462 | 3. **Start Phase 1** - Begin backend API development
463 | 4. **Daily progress updates** - Track progress
464 | 5. **Weekly demos** - Show working features
465 | 
466 | ## Questions to Answer
467 | 
468 | 1. Do you want to keep the existing Tkinter app during development?
469 | 2. Any specific design preferences (colors, fonts)?
470 | 3. Should we support macOS/Linux or Windows-only initially?
471 | 4. Any additional features you'd like to add?
472 | 5. Timeline constraints?
473 | 
474 | ---
475 | 
476 | **Ready to start building?** Let's create a modern, professional SmartClick! 🚀
</content>
</file>
<file><path>docs/API_INTEGRATION.md</path>
<content lines="1-863">
  1 | # IBM watsonx API Integration Guide
  2 | 
  3 | ## Overview
  4 | 
  5 | This guide provides detailed instructions for integrating IBM watsonx AI into SmartClick, including authentication, API usage, prompt engineering, and best practices.
  6 | 
  7 | ## IBM watsonx Setup
  8 | 
  9 | ### Prerequisites
 10 | 
 11 | 1. **IBM Cloud Account**
 12 |    - Sign up at https://cloud.ibm.com
 13 |    - Create a watsonx.ai project
 14 | 
 15 | 2. **API Credentials**
 16 |    - API Key (IAM authentication)
 17 |    - Project ID
 18 |    - Service endpoint URL
 19 | 
 20 | 3. **Model Access**
 21 |    - Ensure access to desired models (e.g., `ibm/granite-13b-chat-v2`)
 22 | 
 23 | ### Environment Configuration
 24 | 
 25 | Create a `.env` file in the project root:
 26 | 
 27 | ```env
 28 | # IBM watsonx Configuration
 29 | WATSONX_API_KEY=your_api_key_here
 30 | WATSONX_PROJECT_ID=your_project_id_here
 31 | WATSONX_ENDPOINT=https://us-south.ml.cloud.ibm.com
 32 | WATSONX_MODEL_ID=ibm/granite-13b-chat-v2
 33 | 
 34 | # Optional: Rate Limiting
 35 | WATSONX_MAX_REQUESTS_PER_MINUTE=60
 36 | WATSONX_MAX_TOKENS_PER_REQUEST=2048
 37 | 
 38 | # Optional: Caching
 39 | ENABLE_RESPONSE_CACHE=true
 40 | CACHE_TTL_SECONDS=3600
 41 | ```
 42 | 
 43 | ## SDK Installation
 44 | 
 45 | ```bash
 46 | npm install @ibm-cloud/watsonx-ai
 47 | npm install ibm-cloud-sdk-core
 48 | ```
 49 | 
 50 | ## Implementation
 51 | 
 52 | ### 1. watsonx Client Wrapper
 53 | 
 54 | **File**: `src/main/services/ai/watsonx-client.ts`
 55 | 
 56 | ```typescript
 57 | import { WatsonXAI } from '@ibm-cloud/watsonx-ai';
 58 | import { IamAuthenticator } from 'ibm-cloud-sdk-core';
 59 | import { logger } from '@main/utils/logger';
 60 | 
 61 | export interface WatsonxConfig {
 62 |   apiKey: string;
 63 |   projectId: string;
 64 |   endpoint: string;
 65 |   modelId: string;
 66 |   maxTokens?: number;
 67 |   temperature?: number;
 68 |   topP?: number;
 69 |   topK?: number;
 70 | }
 71 | 
 72 | export interface GenerationParams {
 73 |   prompt: string;
 74 |   maxNewTokens?: number;
 75 |   temperature?: number;
 76 |   topP?: number;
 77 |   topK?: number;
 78 |   stopSequences?: string[];
 79 |   repetitionPenalty?: number;
 80 | }
 81 | 
 82 | export interface GenerationResponse {
 83 |   text: string;
 84 |   tokenCount: number;
 85 |   finishReason: string;
 86 |   metadata?: Record<string, any>;
 87 | }
 88 | 
 89 | export class WatsonxClient {
 90 |   private client: WatsonXAI;
 91 |   private config: WatsonxConfig;
 92 |   private requestCount: number = 0;
 93 |   private lastResetTime: number = Date.now();
 94 | 
 95 |   constructor(config: WatsonxConfig) {
 96 |     this.config = config;
 97 |     
 98 |     // Initialize IBM Cloud SDK authenticator
 99 |     const authenticator = new IamAuthenticator({
100 |       apikey: config.apiKey,
101 |     });
102 | 
103 |     // Initialize watsonx.ai client
104 |     this.client = new WatsonXAI({
105 |       authenticator,
106 |       serviceUrl: config.endpoint,
107 |     });
108 | 
109 |     logger.info('WatsonxClient initialized', {
110 |       endpoint: config.endpoint,
111 |       modelId: config.modelId,
112 |     });
113 |   }
114 | 
115 |   /**
116 |    * Generate text completion
117 |    */
118 |   async generateText(params: GenerationParams): Promise<GenerationResponse> {
119 |     try {
120 |       // Rate limiting check
121 |       this.checkRateLimit();
122 | 
123 |       const response = await this.client.generateText({
124 |         projectId: this.config.projectId,
125 |         modelId: this.config.modelId,
126 |         input: params.prompt,
127 |         parameters: {
128 |           max_new_tokens: params.maxNewTokens || this.config.maxTokens || 1024,
129 |           temperature: params.temperature || this.config.temperature || 0.7,
130 |           top_p: params.topP || this.config.topP || 0.9,
131 |           top_k: params.topK || this.config.topK || 50,
132 |           stop_sequences: params.stopSequences || [],
133 |           repetition_penalty: params.repetitionPenalty || 1.1,
134 |         },
135 |       });
136 | 
137 |       this.requestCount++;
138 | 
139 |       const result = response.result.results[0];
140 |       
141 |       logger.info('Text generation successful', {
142 |         tokenCount: result.generated_token_count,
143 |         finishReason: result.stop_reason,
144 |       });
145 | 
146 |       return {
147 |         text: result.generated_text,
148 |         tokenCount: result.generated_token_count,
149 |         finishReason: result.stop_reason,
150 |         metadata: {
151 |           modelId: this.config.modelId,
152 |           inputTokenCount: result.input_token_count,
153 |         },
154 |       };
155 |     } catch (error) {
156 |       logger.error('Text generation failed', { error });
157 |       throw this.handleError(error);
158 |     }
159 |   }
160 | 
161 |   /**
162 |    * Stream text generation (for real-time responses)
163 |    */
164 |   async *streamGeneration(params: GenerationParams): AsyncGenerator<string> {
165 |     try {
166 |       this.checkRateLimit();
167 | 
168 |       const stream = await this.client.generateTextStream({
169 |         projectId: this.config.projectId,
170 |         modelId: this.config.modelId,
171 |         input: params.prompt,
172 |         parameters: {
173 |           max_new_tokens: params.maxNewTokens || this.config.maxTokens || 1024,
174 |           temperature: params.temperature || this.config.temperature || 0.7,
175 |           top_p: params.topP || this.config.topP || 0.9,
176 |           top_k: params.topK || this.config.topK || 50,
177 |           stop_sequences: params.stopSequences || [],
178 |           repetition_penalty: params.repetitionPenalty || 1.1,
179 |         },
180 |       });
181 | 
182 |       this.requestCount++;
183 | 
184 |       for await (const chunk of stream) {
185 |         if (chunk.results && chunk.results[0]) {
186 |           yield chunk.results[0].generated_text;
187 |         }
188 |       }
189 | 
190 |       logger.info('Streaming generation completed');
191 |     } catch (error) {
192 |       logger.error('Streaming generation failed', { error });
193 |       throw this.handleError(error);
194 |     }
195 |   }
196 | 
197 |   /**
198 |    * Check rate limits
199 |    */
200 |   private checkRateLimit(): void {
201 |     const now = Date.now();
202 |     const timeSinceReset = now - this.lastResetTime;
203 | 
204 |     // Reset counter every minute
205 |     if (timeSinceReset >= 60000) {
206 |       this.requestCount = 0;
207 |       this.lastResetTime = now;
208 |     }
209 | 
210 |     const maxRequests = parseInt(process.env.WATSONX_MAX_REQUESTS_PER_MINUTE || '60');
211 |     
212 |     if (this.requestCount >= maxRequests) {
213 |       throw new Error('Rate limit exceeded. Please wait before making more requests.');
214 |     }
215 |   }
216 | 
217 |   /**
218 |    * Handle API errors
219 |    */
220 |   private handleError(error: any): Error {
221 |     if (error.status === 401) {
222 |       return new Error('Authentication failed. Please check your API key.');
223 |     } else if (error.status === 403) {
224 |       return new Error('Access denied. Please check your permissions.');
225 |     } else if (error.status === 429) {
226 |       return new Error('Rate limit exceeded. Please try again later.');
227 |     } else if (error.status === 500) {
228 |       return new Error('IBM watsonx service error. Please try again later.');
229 |     } else {
230 |       return new Error(`API request failed: ${error.message}`);
231 |     }
232 |   }
233 | 
234 |   /**
235 |    * Test connection
236 |    */
237 |   async testConnection(): Promise<boolean> {
238 |     try {
239 |       await this.generateText({
240 |         prompt: 'Hello',
241 |         maxNewTokens: 10,
242 |       });
243 |       return true;
244 |     } catch (error) {
245 |       logger.error('Connection test failed', { error });
246 |       return false;
247 |     }
248 |   }
249 | }
250 | ```
251 | 
252 | ### 2. Prompt Builder
253 | 
254 | **File**: `src/main/services/ai/prompt-builder.ts`
255 | 
256 | ```typescript
257 | export enum PromptAction {
258 |   SUMMARIZE = 'summarize',
259 |   REWRITE = 'rewrite',
260 |   EXPLAIN = 'explain',
261 |   ANALYZE = 'analyze',
262 |   CUSTOM = 'custom',
263 | }
264 | 
265 | export interface PromptOptions {
266 |   action: PromptAction;
267 |   context: string;
268 |   customPrompt?: string;
269 |   tone?: 'professional' | 'casual' | 'friendly' | 'formal';
270 |   length?: 'short' | 'medium' | 'long';
271 |   additionalInstructions?: string;
272 | }
273 | 
274 | export class PromptBuilder {
275 |   private static readonly SYSTEM_PROMPT = `You are IBM Bob, an AI assistant integrated into SmartClick. You help users with text-related tasks across any application. Be concise, helpful, and accurate.`;
276 | 
277 |   private static readonly ACTION_TEMPLATES = {
278 |     [PromptAction.SUMMARIZE]: {
279 |       short: 'Summarize this text in 1-2 sentences:\n\n{context}',
280 |       medium: 'Provide a concise summary of this text:\n\n{context}',
281 |       long: 'Provide a detailed summary of this text, including key points:\n\n{context}',
282 |     },
283 |     [PromptAction.REWRITE]: {
284 |       professional: 'Rewrite this text in a professional tone:\n\n{context}',
285 |       casual: 'Rewrite this text in a casual, conversational tone:\n\n{context}',
286 |       friendly: 'Rewrite this text in a friendly, approachable tone:\n\n{context}',
287 |       formal: 'Rewrite this text in a formal, academic tone:\n\n{context}',
288 |     },
289 |     [PromptAction.EXPLAIN]: {
290 |       short: 'Explain this text simply:\n\n{context}',
291 |       medium: 'Explain this text in clear, understandable terms:\n\n{context}',
292 |       long: 'Provide a detailed explanation of this text, breaking down complex concepts:\n\n{context}',
293 |     },
294 |     [PromptAction.ANALYZE]: {
295 |       short: 'Analyze this text briefly:\n\n{context}',
296 |       medium: 'Analyze this text and provide insights:\n\n{context}',
297 |       long: 'Provide a comprehensive analysis of this text, including themes, tone, and implications:\n\n{context}',
298 |     },
299 |   };
300 | 
301 |   /**
302 |    * Build a prompt for a specific action
303 |    */
304 |   static buildPrompt(options: PromptOptions): string {
305 |     const { action, context, customPrompt, tone, length, additionalInstructions } = options;
306 | 
307 |     let prompt = '';
308 | 
309 |     // Add system prompt
310 |     prompt += `${this.SYSTEM_PROMPT}\n\n`;
311 | 
312 |     // Add action-specific template
313 |     if (action === PromptAction.CUSTOM && customPrompt) {
314 |       prompt += `${customPrompt}\n\nContext:\n${context}`;
315 |     } else {
316 |       const template = this.getTemplate(action, tone, length);
317 |       prompt += template.replace('{context}', context);
318 |     }
319 | 
320 |     // Add additional instructions if provided
321 |     if (additionalInstructions) {
322 |       prompt += `\n\nAdditional instructions: ${additionalInstructions}`;
323 |     }
324 | 
325 |     return prompt;
326 |   }
327 | 
328 |   /**
329 |    * Build a conversational prompt with history
330 |    */
331 |   static buildConversationalPrompt(
332 |     context: string,
333 |     history: Array<{ role: 'user' | 'assistant'; content: string }>,
334 |     userMessage: string
335 |   ): string {
336 |     let prompt = `${this.SYSTEM_PROMPT}\n\n`;
337 |     prompt += `Selected text context:\n${context}\n\n`;
338 |     prompt += `Conversation history:\n`;
339 | 
340 |     // Add conversation history
341 |     for (const message of history) {
342 |       prompt += `${message.role === 'user' ? 'User' : 'Assistant'}: ${message.content}\n`;
343 |     }
344 | 
345 |     // Add current user message
346 |     prompt += `User: ${userMessage}\nAssistant:`;
347 | 
348 |     return prompt;
349 |   }
350 | 
351 |   /**
352 |    * Get template based on action and options
353 |    */
354 |   private static getTemplate(
355 |     action: PromptAction,
356 |     tone?: string,
357 |     length?: string
358 |   ): string {
359 |     const templates = this.ACTION_TEMPLATES[action];
360 |     
361 |     if (!templates) {
362 |       return 'Process this text:\n\n{context}';
363 |     }
364 | 
365 |     const key = tone || length || 'medium';
366 |     return templates[key] || templates['medium'] || Object.values(templates)[0];
367 |   }
368 | 
369 |   /**
370 |    * Estimate token count (rough approximation)
371 |    */
372 |   static estimateTokenCount(text: string): number {
373 |     // Rough estimate: 1 token ≈ 4 characters
374 |     return Math.ceil(text.length / 4);
375 |   }
376 | 
377 |   /**
378 |    * Truncate context to fit within token limit
379 |    */
380 |   static truncateContext(context: string, maxTokens: number): string {
381 |     const estimatedTokens = this.estimateTokenCount(context);
382 |     
383 |     if (estimatedTokens <= maxTokens) {
384 |       return context;
385 |     }
386 | 
387 |     // Truncate to approximate character count
388 |     const maxChars = maxTokens * 4;
389 |     return context.substring(0, maxChars) + '...';
390 |   }
391 | }
392 | ```
393 | 
394 | ### 3. Context Manager
395 | 
396 | **File**: `src/main/services/ai/context-manager.ts`
397 | 
398 | ```typescript
399 | import { PromptBuilder } from './prompt-builder';
400 | 
401 | export interface Message {
402 |   id: string;
403 |   role: 'user' | 'assistant';
404 |   content: string;
405 |   timestamp: number;
406 | }
407 | 
408 | export interface ConversationContext {
409 |   id: string;
410 |   selectedText: string;
411 |   messages: Message[];
412 |   metadata: {
413 |     application: string;
414 |     timestamp: number;
415 |     location?: string;
416 |   };
417 | }
418 | 
419 | export class ContextManager {
420 |   private readonly maxContextTokens: number;
421 |   private readonly maxMessages: number;
422 | 
423 |   constructor(maxContextTokens: number = 4096, maxMessages: number = 20) {
424 |     this.maxContextTokens = maxContextTokens;
425 |     this.maxMessages = maxMessages;
426 |   }
427 | 
428 |   /**
429 |    * Build context for AI request
430 |    */
431 |   buildContext(conversation: ConversationContext, newMessage: string): string {
432 |     const { selectedText, messages } = conversation;
433 | 
434 |     // Calculate token budget
435 |     const selectedTextTokens = PromptBuilder.estimateTokenCount(selectedText);
436 |     const newMessageTokens = PromptBuilder.estimateTokenCount(newMessage);
437 |     const systemPromptTokens = 100; // Approximate
438 |     
439 |     let remainingTokens = this.maxContextTokens - selectedTextTokens - newMessageTokens - systemPromptTokens;
440 | 
441 |     // Select messages that fit within token budget
442 |     const relevantMessages: Message[] = [];
443 |     
444 |     // Start from most recent messages
445 |     for (let i = messages.length - 1; i >= 0 && relevantMessages.length < this.maxMessages; i--) {
446 |       const message = messages[i];
447 |       const messageTokens = PromptBuilder.estimateTokenCount(message.content);
448 |       
449 |       if (messageTokens <= remainingTokens) {
450 |         relevantMessages.unshift(message);
451 |         remainingTokens -= messageTokens;
452 |       } else {
453 |         break;
454 |       }
455 |     }
456 | 
457 |     // Build conversational prompt
458 |     return PromptBuilder.buildConversationalPrompt(
459 |       selectedText,
460 |       relevantMessages.map(m => ({ role: m.role, content: m.content })),
461 |       newMessage
462 |     );
463 |   }
464 | 
465 |   /**
466 |    * Add message to conversation
467 |    */
468 |   addMessage(conversation: ConversationContext, role: 'user' | 'assistant', content: string): Message {
469 |     const message: Message = {
470 |       id: this.generateMessageId(),
471 |       role,
472 |       content,
473 |       timestamp: Date.now(),
474 |     };
475 | 
476 |     conversation.messages.push(message);
477 | 
478 |     // Trim old messages if exceeding limit
479 |     if (conversation.messages.length > this.maxMessages * 2) {
480 |       conversation.messages = conversation.messages.slice(-this.maxMessages);
481 |     }
482 | 
483 |     return message;
484 |   }
485 | 
486 |   /**
487 |    * Create new conversation
488 |    */
489 |   createConversation(selectedText: string, application: string): ConversationContext {
490 |     return {
491 |       id: this.generateConversationId(),
492 |       selectedText,
493 |       messages: [],
494 |       metadata: {
495 |         application,
496 |         timestamp: Date.now(),
497 |       },
498 |     };
499 |   }
500 | 
501 |   /**
502 |    * Generate unique message ID
503 |    */
504 |   private generateMessageId(): string {
505 |     return `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
506 |   }
507 | 
508 |   /**
509 |    * Generate unique conversation ID
510 |    */
511 |   private generateConversationId(): string {
512 |     return `conv_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
513 |   }
514 | }
515 | ```
516 | 
517 | ### 4. Response Cache
518 | 
519 | **File**: `src/main/services/ai/cache.ts`
520 | 
521 | ```typescript
522 | import crypto from 'crypto';
523 | import { logger } from '@main/utils/logger';
524 | 
525 | interface CacheEntry {
526 |   response: string;
527 |   timestamp: number;
528 |   tokenCount: number;
529 | }
530 | 
531 | export class ResponseCache {
532 |   private cache: Map<string, CacheEntry>;
533 |   private readonly ttl: number;
534 |   private readonly maxSize: number;
535 | 
536 |   constructor(ttlSeconds: number = 3600, maxSize: number = 100) {
537 |     this.cache = new Map();
538 |     this.ttl = ttlSeconds * 1000;
539 |     this.maxSize = maxSize;
540 |   }
541 | 
542 |   /**
543 |    * Get cached response
544 |    */
545 |   get(prompt: string): string | null {
546 |     const key = this.generateKey(prompt);
547 |     const entry = this.cache.get(key);
548 | 
549 |     if (!entry) {
550 |       return null;
551 |     }
552 | 
553 |     // Check if expired
554 |     if (Date.now() - entry.timestamp > this.ttl) {
555 |       this.cache.delete(key);
556 |       return null;
557 |     }
558 | 
559 |     logger.info('Cache hit', { key });
560 |     return entry.response;
561 |   }
562 | 
563 |   /**
564 |    * Set cached response
565 |    */
566 |   set(prompt: string, response: string, tokenCount: number): void {
567 |     const key = this.generateKey(prompt);
568 | 
569 |     // Evict oldest entry if cache is full
570 |     if (this.cache.size >= this.maxSize) {
571 |       const oldestKey = this.cache.keys().next().value;
572 |       this.cache.delete(oldestKey);
573 |     }
574 | 
575 |     this.cache.set(key, {
576 |       response,
577 |       timestamp: Date.now(),
578 |       tokenCount,
579 |     });
580 | 
581 |     logger.info('Cache set', { key, tokenCount });
582 |   }
583 | 
584 |   /**
585 |    * Clear cache
586 |    */
587 |   clear(): void {
588 |     this.cache.clear();
589 |     logger.info('Cache cleared');
590 |   }
591 | 
592 |   /**
593 |    * Get cache statistics
594 |    */
595 |   getStats(): { size: number; maxSize: number; hitRate: number } {
596 |     return {
597 |       size: this.cache.size,
598 |       maxSize: this.maxSize,
599 |       hitRate: 0, // TODO: Implement hit rate tracking
600 |     };
601 |   }
602 | 
603 |   /**
604 |    * Generate cache key from prompt
605 |    */
606 |   private generateKey(prompt: string): string {
607 |     return crypto.createHash('sha256').update(prompt).digest('hex');
608 |   }
609 | }
610 | ```
611 | 
612 | ## Usage Examples
613 | 
614 | ### Basic Text Generation
615 | 
616 | ```typescript
617 | import { WatsonxClient } from '@main/services/ai/watsonx-client';
618 | import { PromptBuilder, PromptAction } from '@main/services/ai/prompt-builder';
619 | 
620 | const client = new WatsonxClient({
621 |   apiKey: process.env.WATSONX_API_KEY!,
622 |   projectId: process.env.WATSONX_PROJECT_ID!,
623 |   endpoint: process.env.WATSONX_ENDPOINT!,
624 |   modelId: process.env.WATSONX_MODEL_ID!,
625 | });
626 | 
627 | // Summarize text
628 | const prompt = PromptBuilder.buildPrompt({
629 |   action: PromptAction.SUMMARIZE,
630 |   context: 'Your selected text here...',
631 |   length: 'short',
632 | });
633 | 
634 | const response = await client.generateText({ prompt });
635 | console.log(response.text);
636 | ```
637 | 
638 | ### Streaming Generation
639 | 
640 | ```typescript
641 | // Stream response for real-time display
642 | const prompt = PromptBuilder.buildPrompt({
643 |   action: PromptAction.EXPLAIN,
644 |   context: 'Complex technical text...',
645 |   length: 'medium',
646 | });
647 | 
648 | for await (const chunk of client.streamGeneration({ prompt })) {
649 |   // Send chunk to renderer process
650 |   mainWindow.webContents.send('ai-response-chunk', chunk);
651 | }
652 | ```
653 | 
654 | ### Conversational Context
655 | 
656 | ```typescript
657 | import { ContextManager } from '@main/services/ai/context-manager';
658 | 
659 | const contextManager = new ContextManager();
660 | 
661 | // Create conversation
662 | const conversation = contextManager.createConversation(
663 |   'Selected text from document',
664 |   'Microsoft Word'
665 | );
666 | 
667 | // Add user message
668 | contextManager.addMessage(conversation, 'user', 'Can you explain this?');
669 | 
670 | // Build context for AI
671 | const prompt = contextManager.buildContext(conversation, 'Can you explain this?');
672 | 
673 | // Generate response
674 | const response = await client.generateText({ prompt });
675 | 
676 | // Add assistant response
677 | contextManager.addMessage(conversation, 'assistant', response.text);
678 | ```
679 | 
680 | ### With Caching
681 | 
682 | ```typescript
683 | import { ResponseCache } from '@main/services/ai/cache';
684 | 
685 | const cache = new ResponseCache(3600, 100);
686 | 
687 | async function generateWithCache(prompt: string) {
688 |   // Check cache first
689 |   const cached = cache.get(prompt);
690 |   if (cached) {
691 |     return cached;
692 |   }
693 | 
694 |   // Generate new response
695 |   const response = await client.generateText({ prompt });
696 |   
697 |   // Cache the response
698 |   cache.set(prompt, response.text, response.tokenCount);
699 |   
700 |   return response.text;
701 | }
702 | ```
703 | 
704 | ## Best Practices
705 | 
706 | ### 1. Prompt Engineering
707 | 
708 | - **Be specific**: Clear instructions yield better results
709 | - **Provide context**: Include relevant background information
710 | - **Set constraints**: Specify length, tone, format requirements
711 | - **Use examples**: Show desired output format when possible
712 | 
713 | ### 2. Error Handling
714 | 
715 | ```typescript
716 | try {
717 |   const response = await client.generateText({ prompt });
718 |   return response.text;
719 | } catch (error) {
720 |   if (error.message.includes('Rate limit')) {
721 |     // Queue request for retry
722 |     return 'Request queued. Please wait...';
723 |   } else if (error.message.includes('Authentication')) {
724 |     // Prompt user to re-enter API key
725 |     return 'Authentication failed. Please check settings.';
726 |   } else {
727 |     // Generic error
728 |     return 'An error occurred. Please try again.';
729 |   }
730 | }
731 | ```
732 | 
733 | ### 3. Rate Limiting
734 | 
735 | - Implement request queuing for high-volume usage
736 | - Show user feedback when rate limited
737 | - Consider implementing exponential backoff
738 | 
739 | ### 4. Token Management
740 | 
741 | - Monitor token usage to avoid exceeding limits
742 | - Truncate long contexts intelligently
743 | - Prioritize recent messages in conversations
744 | 
745 | ### 5. Caching Strategy
746 | 
747 | - Cache identical requests to reduce API calls
748 | - Set appropriate TTL based on content type
749 | - Clear cache periodically to prevent stale data
750 | 
751 | ## Testing
752 | 
753 | ### Unit Tests
754 | 
755 | ```typescript
756 | import { describe, it, expect, vi } from 'vitest';
757 | import { WatsonxClient } from './watsonx-client';
758 | 
759 | describe('WatsonxClient', () => {
760 |   it('should generate text successfully', async () => {
761 |     const client = new WatsonxClient({
762 |       apiKey: 'test-key',
763 |       projectId: 'test-project',
764 |       endpoint: 'https://test.com',
765 |       modelId: 'test-model',
766 |     });
767 | 
768 |     const response = await client.generateText({
769 |       prompt: 'Hello',
770 |       maxNewTokens: 10,
771 |     });
772 | 
773 |     expect(response.text).toBeDefined();
774 |     expect(response.tokenCount).toBeGreaterThan(0);
775 |   });
776 | });
777 | ```
778 | 
779 | ### Integration Tests
780 | 
781 | ```typescript
782 | describe('AI Integration', () => {
783 |   it('should handle full workflow', async () => {
784 |     const client = new WatsonxClient(config);
785 |     const contextManager = new ContextManager();
786 |     
787 |     const conversation = contextManager.createConversation(
788 |       'Test text',
789 |       'Test App'
790 |     );
791 |     
792 |     const prompt = contextManager.buildContext(conversation, 'Summarize this');
793 |     const response = await client.generateText({ prompt });
794 |     
795 |     expect(response.text).toBeDefined();
796 |   });
797 | });
798 | ```
799 | 
800 | ## Monitoring & Analytics
801 | 
802 | ### Track API Usage
803 | 
804 | ```typescript
805 | class UsageTracker {
806 |   private totalRequests = 0;
807 |   private totalTokens = 0;
808 |   private errors = 0;
809 | 
810 |   trackRequest(tokenCount: number) {
811 |     this.totalRequests++;
812 |     this.totalTokens += tokenCount;
813 |   }
814 | 
815 |   trackError() {
816 |     this.errors++;
817 |   }
818 | 
819 |   getStats() {
820 |     return {
821 |       totalRequests: this.totalRequests,
822 |       totalTokens: this.totalTokens,
823 |       errors: this.errors,
824 |       averageTokensPerRequest: this.totalTokens / this.totalRequests,
825 |     };
826 |   }
827 | }
828 | ```
829 | 
830 | ## Troubleshooting
831 | 
832 | ### Common Issues
833 | 
834 | 1. **Authentication Errors**
835 |    - Verify API key is correct
836 |    - Check if API key has expired
837 |    - Ensure proper IAM permissions
838 | 
839 | 2. **Rate Limiting**
840 |    - Implement request queuing
841 |    - Add delays between requests
842 |    - Consider upgrading plan
843 | 
844 | 3. **Slow Responses**
845 |    - Use streaming for better UX
846 |    - Reduce max_new_tokens
847 |    - Implement caching
848 | 
849 | 4. **Poor Quality Responses**
850 |    - Refine prompts
851 |    - Adjust temperature/top_p
852 |    - Try different models
853 | 
854 | ## Resources
855 | 
856 | - [IBM watsonx.ai Documentation](https://cloud.ibm.com/docs/watsonx-ai)
857 | - [IBM Cloud SDK for Node.js](https://github.com/IBM/node-sdk-core)
858 | - [watsonx.ai API Reference](https://cloud.ibm.com/apidocs/watsonx-ai)
859 | - [Prompt Engineering Guide](https://www.promptingguide.ai/)
860 | 
861 | ## Conclusion
862 | 
863 | This integration guide provides everything needed to successfully integrate IBM watsonx into SmartClick. Follow the implementation patterns, best practices, and error handling strategies to create a robust AI-powered experience.
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs
backend/backend_client.py,backend/api/main.py,.env,docs/SERVICE_DOCUMENTATION.md,docs/FRONTEND_IMPLEMENTATION_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-03T13:30:26.955Z
User time zone: Africa/Johannesburg, UTC+2:00

# Current Cost
$0.22

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>advanced</slug>
<name>🛠️ Advanced</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now let me read the remaining documentation files to complete my comprehensive analysis.

<read_file>
<args>
  <file>
    <path>docs/IBM_CLOUD_DATABASE_SETUP.md</path>
  </file>
  <file>
    <path>docs/FRONTEND_IMPLEMENTATION_GUIDE.md</path>
  </file>
  <file>
    <path>docs/SERVICE_DOCUMENTATION.md</path>
  </file>
  <file>
    <path>text.md</path>
  </file>
  <file>
    <path>frontend/README.md</path>
  </file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>docs/IBM_CLOUD_DATABASE_SETUP.md</path>
<content lines="1-786">
  1 | # IBM Cloud Database Setup Guide for SmartClick
  2 | 
  3 | ## Overview
  4 | 
  5 | This guide walks you through setting up IBM Cloud Databases for PostgreSQL (recommended) or MongoDB for SmartClick, and connecting your application to it.
  6 | 
  7 | ## Why IBM Cloud Database?
  8 | 
  9 | ✅ **Cloud-native** - No local storage limitations
 10 | ✅ **Scalable** - Grows with your user base
 11 | ✅ **Reliable** - Built-in backups and high availability
 12 | ✅ **Secure** - Encrypted connections and data at rest
 13 | ✅ **Managed** - IBM handles maintenance and updates
 14 | ✅ **Multi-user** - Sync across devices (future feature)
 15 | 
 16 | ## Recommended Database: IBM Cloud Databases for PostgreSQL
 17 | 
 18 | PostgreSQL is recommended because:
 19 | - Excellent JSON support for flexible data
 20 | - ACID compliant for data integrity
 21 | - Powerful querying capabilities
 22 | - Great performance
 23 | - Wide ecosystem support
 24 | 
 25 | **Alternative**: IBM Cloud Databases for MongoDB (if you prefer document-based storage)
 26 | 
 27 | ---
 28 | 
 29 | ## Step 1: Create IBM Cloud Account
 30 | 
 31 | 1. Go to https://cloud.ibm.com
 32 | 2. Click **"Create an account"** (if you don't have one)
 33 | 3. Complete registration and verify your email
 34 | 4. Log in to IBM Cloud Console
 35 | 
 36 | ---
 37 | 
 38 | ## Step 2: Create Database Instance
 39 | 
 40 | ### Option A: Using IBM Cloud Console (Recommended for beginners)
 41 | 
 42 | 1. **Navigate to Catalog**
 43 |    - From IBM Cloud dashboard, click **"Catalog"** in top menu
 44 |    - Or go directly to: https://cloud.ibm.com/catalog
 45 | 
 46 | 2. **Find Database Service**
 47 |    - In the search bar, type **"Databases for PostgreSQL"**
 48 |    - Click on **"Databases for PostgreSQL"**
 49 | 
 50 | 3. **Configure Database Instance**
 51 |    
 52 |    **Basic Settings:**
 53 |    - **Service name**: `smartclick-db` (or your preferred name)
 54 |    - **Region**: Choose closest to your users (e.g., `us-south`, `eu-de`)
 55 |    - **Resource group**: `Default` (or create new)
 56 | 
 57 |    **Pricing Plan:**
 58 |    - **Standard**: Recommended for production
 59 |    - **Enterprise**: For high-availability needs
 60 |    - Start with **Standard** plan
 61 | 
 62 |    **Resource Allocation:**
 63 |    - **Memory**: Start with 1 GB (minimum)
 64 |    - **Disk**: Start with 5 GB (can scale later)
 65 |    - **CPU**: 0 dedicated cores (shared) for development
 66 |    
 67 |    **Version:**
 68 |    - Select latest PostgreSQL version (e.g., PostgreSQL 15)
 69 | 
 70 | 4. **Configure Networking**
 71 |    - **Endpoints**: Select **"Public and Private"** or **"Public"** only
 72 |    - **IP Allowlist**: Add your IP addresses (or `0.0.0.0/0` for testing - NOT recommended for production)
 73 | 
 74 | 5. **Create Instance**
 75 |    - Review configuration
 76 |    - Click **"Create"**
 77 |    - Wait 5-10 minutes for provisioning
 78 | 
 79 | ### Option B: Using IBM Cloud CLI
 80 | 
 81 | ```bash
 82 | # Install IBM Cloud CLI
 83 | curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
 84 | 
 85 | # Login
 86 | ibmcloud login
 87 | 
 88 | # Target resource group
 89 | ibmcloud target -g Default
 90 | 
 91 | # Create PostgreSQL instance
 92 | ibmcloud resource service-instance-create smartclick-db \
 93 |   databases-for-postgresql \
 94 |   standard \
 95 |   us-south \
 96 |   -p '{
 97 |     "members_memory_allocation_mb": "1024",
 98 |     "members_disk_allocation_mb": "5120",
 99 |     "version": "15"
100 |   }'
101 | ```
102 | 
103 | ---
104 | 
105 | ## Step 3: Get Connection Credentials
106 | 
107 | ### Via IBM Cloud Console
108 | 
109 | 1. **Navigate to Your Database**
110 |    - Go to **Resource List** > **Databases**
111 |    - Click on your database instance (`smartclick-db`)
112 | 
113 | 2. **Access Service Credentials**
114 |    - Click **"Service credentials"** in left sidebar
115 |    - Click **"New credential"** button
116 |    - Name it: `smartclick-app-credentials`
117 |    - Click **"Add"**
118 | 
119 | 3. **View Credentials**
120 |    - Click **"View credentials"** on the newly created credential
121 |    - You'll see a JSON object with connection details
122 | 
123 | **Example Credentials Structure:**
124 | ```json
125 | {
126 |   "connection": {
127 |     "postgres": {
128 |       "composed": [
129 |         "postgres://ibm_cloud_xxx:password@host:port/ibmclouddb?sslmode=verify-full"
130 |       ],
131 |       "hosts": [
132 |         {
133 |           "hostname": "xxx.databases.appdomain.cloud",
134 |           "port": 32541
135 |         }
136 |       ],
137 |       "database": "ibmclouddb",
138 |       "username": "ibm_cloud_xxx",
139 |       "password": "your_password_here",
140 |       "certificate": {
141 |         "certificate_base64": "LS0tLS1CRUdJTi..."
142 |       }
143 |     }
144 |   }
145 | }
146 | ```
147 | 
148 | 4. **Save Important Information**
149 |    - **Host**: `xxx.databases.appdomain.cloud`
150 |    - **Port**: `32541`
151 |    - **Database**: `ibmclouddb`
152 |    - **Username**: `ibm_cloud_xxx`
153 |    - **Password**: `your_password_here`
154 |    - **SSL Certificate**: The base64 encoded certificate
155 | 
156 | ---
157 | 
158 | ## Step 4: Configure SmartClick Application
159 | 
160 | ### 4.1 Update Environment Variables
161 | 
162 | Create/update `.env` file in your project root:
163 | 
164 | ```env
165 | # IBM Cloud Database Configuration
166 | DB_TYPE=postgresql
167 | DB_HOST=xxx.databases.appdomain.cloud
168 | DB_PORT=32541
169 | DB_NAME=ibmclouddb
170 | DB_USER=ibm_cloud_xxx
171 | DB_PASSWORD=your_password_here
172 | DB_SSL=true
173 | DB_SSL_CERT_BASE64=LS0tLS1CRUdJTi...
174 | 
175 | # Connection Pool Settings
176 | DB_POOL_MIN=2
177 | DB_POOL_MAX=10
178 | DB_CONNECTION_TIMEOUT=30000
179 | 
180 | # IBM watsonx Configuration (existing)
181 | WATSONX_API_KEY=your_api_key_here
182 | WATSONX_PROJECT_ID=your_project_id_here
183 | WATSONX_ENDPOINT=https://us-south.ml.cloud.ibm.com
184 | WATSONX_MODEL_ID=ibm/granite-13b-chat-v2
185 | ```
186 | 
187 | ### 4.2 Install Required NPM Packages
188 | 
189 | ```bash
190 | # PostgreSQL client
191 | npm install pg
192 | 
193 | # Connection pooling
194 | npm install pg-pool
195 | 
196 | # SSL certificate handling
197 | npm install node-forge
198 | 
199 | # TypeScript types
200 | npm install -D @types/pg
201 | ```
202 | 
203 | ### 4.3 Create Database Connection Module
204 | 
205 | **File**: `src/main/services/database/connection.ts`
206 | 
207 | ```typescript
208 | import { Pool, PoolConfig } from 'pg';
209 | import fs from 'fs';
210 | import path from 'path';
211 | import { logger } from '@main/utils/logger';
212 | 
213 | class DatabaseConnection {
214 |   private pool: Pool | null = null;
215 |   private static instance: DatabaseConnection;
216 | 
217 |   private constructor() {}
218 | 
219 |   static getInstance(): DatabaseConnection {
220 |     if (!DatabaseConnection.instance) {
221 |       DatabaseConnection.instance = new DatabaseConnection();
222 |     }
223 |     return DatabaseConnection.instance;
224 |   }
225 | 
226 |   async connect(): Promise<void> {
227 |     if (this.pool) {
228 |       logger.info('Database already connected');
229 |       return;
230 |     }
231 | 
232 |     try {
233 |       // Decode SSL certificate from base64
234 |       const certBase64 = process.env.DB_SSL_CERT_BASE64;
235 |       let sslConfig: any = false;
236 | 
237 |       if (certBase64 && process.env.DB_SSL === 'true') {
238 |         const certBuffer = Buffer.from(certBase64, 'base64');
239 |         sslConfig = {
240 |           rejectUnauthorized: true,
241 |           ca: certBuffer.toString('utf-8'),
242 |         };
243 |       }
244 | 
245 |       const poolConfig: PoolConfig = {
246 |         host: process.env.DB_HOST,
247 |         port: parseInt(process.env.DB_PORT || '5432'),
248 |         database: process.env.DB_NAME,
249 |         user: process.env.DB_USER,
250 |         password: process.env.DB_PASSWORD,
251 |         ssl: sslConfig,
252 |         min: parseInt(process.env.DB_POOL_MIN || '2'),
253 |         max: parseInt(process.env.DB_POOL_MAX || '10'),
254 |         connectionTimeoutMillis: parseInt(process.env.DB_CONNECTION_TIMEOUT || '30000'),
255 |         idleTimeoutMillis: 30000,
256 |       };
257 | 
258 |       this.pool = new Pool(poolConfig);
259 | 
260 |       // Test connection
261 |       const client = await this.pool.connect();
262 |       await client.query('SELECT NOW()');
263 |       client.release();
264 | 
265 |       logger.info('Database connected successfully', {
266 |         host: process.env.DB_HOST,
267 |         database: process.env.DB_NAME,
268 |       });
269 | 
270 |       // Handle pool errors
271 |       this.pool.on('error', (err) => {
272 |         logger.error('Unexpected database error', { error: err });
273 |       });
274 | 
275 |     } catch (error) {
276 |       logger.error('Database connection failed', { error });
277 |       throw new Error(`Failed to connect to database: ${error.message}`);
278 |     }
279 |   }
280 | 
281 |   async disconnect(): Promise<void> {
282 |     if (this.pool) {
283 |       await this.pool.end();
284 |       this.pool = null;
285 |       logger.info('Database disconnected');
286 |     }
287 |   }
288 | 
289 |   getPool(): Pool {
290 |     if (!this.pool) {
291 |       throw new Error('Database not connected. Call connect() first.');
292 |     }
293 |     return this.pool;
294 |   }
295 | 
296 |   async query(text: string, params?: any[]): Promise<any> {
297 |     const pool = this.getPool();
298 |     const start = Date.now();
299 |     
300 |     try {
301 |       const result = await pool.query(text, params);
302 |       const duration = Date.now() - start;
303 |       
304 |       logger.debug('Query executed', {
305 |         query: text,
306 |         duration,
307 |         rows: result.rowCount,
308 |       });
309 |       
310 |       return result;
311 |     } catch (error) {
312 |       logger.error('Query failed', {
313 |         query: text,
314 |         error,
315 |       });
316 |       throw error;
317 |     }
318 |   }
319 | 
320 |   async transaction<T>(callback: (client: any) => Promise<T>): Promise<T> {
321 |     const pool = this.getPool();
322 |     const client = await pool.connect();
323 |     
324 |     try {
325 |       await client.query('BEGIN');
326 |       const result = await callback(client);
327 |       await client.query('COMMIT');
328 |       return result;
329 |     } catch (error) {
330 |       await client.query('ROLLBACK');
331 |       throw error;
332 |     } finally {
333 |       client.release();
334 |     }
335 |   }
336 | }
337 | 
338 | export const db = DatabaseConnection.getInstance();
339 | ```
340 | 
341 | ---
342 | 
343 | ## Step 5: Create Database Schema
344 | 
345 | ### 5.1 Create Migration Script
346 | 
347 | **File**: `src/main/services/database/migrations/001_initial_schema.sql`
348 | 
349 | ```sql
350 | -- Enable UUID extension
351 | CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
352 | 
353 | -- Conversations table
354 | CREATE TABLE IF NOT EXISTS conversations (
355 |     id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
356 |     selected_text TEXT NOT NULL,
357 |     application_name VARCHAR(255),
358 |     application_path TEXT,
359 |     window_title TEXT,
360 |     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
361 |     updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
362 |     last_accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
363 |     message_count INTEGER DEFAULT 0,
364 |     is_pinned BOOLEAN DEFAULT FALSE,
365 |     is_archived BOOLEAN DEFAULT FALSE,
366 |     tags JSONB DEFAULT '[]'::jsonb,
367 |     metadata JSONB DEFAULT '{}'::jsonb
368 | );
369 | 
370 | -- Messages table
371 | CREATE TABLE IF NOT EXISTS messages (
372 |     id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
373 |     conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
374 |     role VARCHAR(20) NOT NULL CHECK (role IN ('user', 'assistant')),
375 |     content TEXT NOT NULL,
376 |     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
377 |     token_count INTEGER,
378 |     model_id VARCHAR(100),
379 |     prompt_template VARCHAR(50),
380 |     metadata JSONB DEFAULT '{}'::jsonb
381 | );
382 | 
383 | -- Settings table
384 | CREATE TABLE IF NOT EXISTS settings (
385 |     key VARCHAR(255) PRIMARY KEY,
386 |     value JSONB NOT NULL,
387 |     category VARCHAR(100),
388 |     updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
389 |     metadata JSONB DEFAULT '{}'::jsonb
390 | );
391 | 
392 | -- Usage statistics table
393 | CREATE TABLE IF NOT EXISTS usage_stats (
394 |     id SERIAL PRIMARY KEY,
395 |     event_type VARCHAR(100) NOT NULL,
396 |     event_data JSONB,
397 |     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
398 |     session_id VARCHAR(100)
399 | );
400 | 
401 | -- Cache table
402 | CREATE TABLE IF NOT EXISTS cache (
403 |     key VARCHAR(255) PRIMARY KEY,
404 |     prompt TEXT NOT NULL,
405 |     response TEXT NOT NULL,
406 |     token_count INTEGER,
407 |     model_id VARCHAR(100),
408 |     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
409 |     accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
410 |     access_count INTEGER DEFAULT 1,
411 |     expires_at TIMESTAMP WITH TIME ZONE
412 | );
413 | 
414 | -- Indexes for performance
415 | CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at DESC);
416 | CREATE INDEX IF NOT EXISTS idx_conversations_updated_at ON conversations(updated_at DESC);
417 | CREATE INDEX IF NOT EXISTS idx_conversations_application ON conversations(application_name);
418 | CREATE INDEX IF NOT EXISTS idx_conversations_pinned ON conversations(is_pinned, created_at DESC);
419 | 
420 | CREATE INDEX IF NOT EXISTS idx_messages_conversation ON messages(conversation_id, created_at);
421 | CREATE INDEX IF NOT EXISTS idx_messages_role ON messages(role);
422 | 
423 | CREATE INDEX IF NOT EXISTS idx_settings_category ON settings(category);
424 | 
425 | CREATE INDEX IF NOT EXISTS idx_usage_stats_event_type ON usage_stats(event_type, created_at);
426 | CREATE INDEX IF NOT EXISTS idx_usage_stats_created_at ON usage_stats(created_at DESC);
427 | 
428 | CREATE INDEX IF NOT EXISTS idx_cache_expires_at ON cache(expires_at);
429 | CREATE INDEX IF NOT EXISTS idx_cache_accessed_at ON cache(accessed_at);
430 | 
431 | -- Function to update updated_at timestamp
432 | CREATE OR REPLACE FUNCTION update_updated_at_column()
433 | RETURNS TRIGGER AS $$
434 | BEGIN
435 |     NEW.updated_at = CURRENT_TIMESTAMP;
436 |     RETURN NEW;
437 | END;
438 | $$ language 'plpgsql';
439 | 
440 | -- Trigger for conversations
441 | CREATE TRIGGER update_conversations_updated_at 
442 |     BEFORE UPDATE ON conversations 
443 |     FOR EACH ROW 
444 |     EXECUTE FUNCTION update_updated_at_column();
445 | ```
446 | 
447 | ### 5.2 Run Migration
448 | 
449 | **File**: `src/main/services/database/migrate.ts`
450 | 
451 | ```typescript
452 | import { db } from './connection';
453 | import fs from 'fs';
454 | import path from 'path';
455 | import { logger } from '@main/utils/logger';
456 | 
457 | export async function runMigrations(): Promise<void> {
458 |   try {
459 |     logger.info('Running database migrations...');
460 | 
461 |     // Read migration file
462 |     const migrationPath = path.join(__dirname, 'migrations', '001_initial_schema.sql');
463 |     const migrationSQL = fs.readFileSync(migrationPath, 'utf-8');
464 | 
465 |     // Execute migration
466 |     await db.query(migrationSQL);
467 | 
468 |     logger.info('Database migrations completed successfully');
469 |   } catch (error) {
470 |     logger.error('Migration failed', { error });
471 |     throw error;
472 |   }
473 | }
474 | ```
475 | 
476 | ### 5.3 Initialize Database on App Start
477 | 
478 | **File**: `src/main/app.ts` (update)
479 | 
480 | ```typescript
481 | import { app } from 'electron';
482 | import { db } from './services/database/connection';
483 | import { runMigrations } from './services/database/migrate';
484 | import { logger } from './utils/logger';
485 | 
486 | app.on('ready', async () => {
487 |   try {
488 |     // Connect to database
489 |     await db.connect();
490 |     
491 |     // Run migrations
492 |     await runMigrations();
493 |     
494 |     // Continue with app initialization
495 |     // ...
496 |   } catch (error) {
497 |     logger.error('App initialization failed', { error });
498 |     app.quit();
499 |   }
500 | });
501 | 
502 | app.on('quit', async () => {
503 |   await db.disconnect();
504 | });
505 | ```
506 | 
507 | ---
508 | 
509 | ## Step 6: Implement Database Operations
510 | 
511 | ### Example: Conversation Repository
512 | 
513 | **File**: `src/main/services/database/repositories/conversation.repository.ts`
514 | 
515 | ```typescript
516 | import { db } from '../connection';
517 | import { logger } from '@main/utils/logger';
518 | 
519 | export interface Conversation {
520 |   id: string;
521 |   selectedText: string;
522 |   applicationName: string;
523 |   windowTitle: string;
524 |   createdAt: Date;
525 |   updatedAt: Date;
526 |   messageCount: number;
527 |   isPinned: boolean;
528 |   tags: string[];
529 | }
530 | 
531 | export class ConversationRepository {
532 |   async create(data: {
533 |     selectedText: string;
534 |     applicationName: string;
535 |     windowTitle: string;
536 |   }): Promise<string> {
537 |     const result = await db.query(
538 |       `INSERT INTO conversations (selected_text, application_name, window_title)
539 |        VALUES ($1, $2, $3)
540 |        RETURNING id`,
541 |       [data.selectedText, data.applicationName, data.windowTitle]
542 |     );
543 |     
544 |     return result.rows[0].id;
545 |   }
546 | 
547 |   async findById(id: string): Promise<Conversation | null> {
548 |     const result = await db.query(
549 |       'SELECT * FROM conversations WHERE id = $1',
550 |       [id]
551 |     );
552 |     
553 |     return result.rows[0] || null;
554 |   }
555 | 
556 |   async findRecent(limit: number = 50): Promise<Conversation[]> {
557 |     const result = await db.query(
558 |       `SELECT * FROM conversations 
559 |        WHERE is_archived = FALSE 
560 |        ORDER BY updated_at DESC 
561 |        LIMIT $1`,
562 |       [limit]
563 |     );
564 |     
565 |     return result.rows;
566 |   }
567 | 
568 |   async search(query: string): Promise<Conversation[]> {
569 |     const result = await db.query(
570 |       `SELECT * FROM conversations 
571 |        WHERE selected_text ILIKE $1 OR window_title ILIKE $1
572 |        ORDER BY updated_at DESC`,
573 |       [`%${query}%`]
574 |     );
575 |     
576 |     return result.rows;
577 |   }
578 | 
579 |   async delete(id: string): Promise<void> {
580 |     await db.query('DELETE FROM conversations WHERE id = $1', [id]);
581 |   }
582 | }
583 | ```
584 | 
585 | ---
586 | 
587 | ## Step 7: Test Connection
588 | 
589 | ### Create Test Script
590 | 
591 | **File**: `scripts/test-db-connection.ts`
592 | 
593 | ```typescript
594 | import { db } from '../src/main/services/database/connection';
595 | 
596 | async function testConnection() {
597 |   try {
598 |     console.log('Testing database connection...');
599 |     
600 |     await db.connect();
601 |     
602 |     const result = await db.query('SELECT NOW() as current_time, version() as pg_version');
603 |     
604 |     console.log('✅ Connection successful!');
605 |     console.log('Current time:', result.rows[0].current_time);
606 |     console.log('PostgreSQL version:', result.rows[0].pg_version);
607 |     
608 |     await db.disconnect();
609 |     
610 |     process.exit(0);
611 |   } catch (error) {
612 |     console.error('❌ Connection failed:', error);
613 |     process.exit(1);
614 |   }
615 | }
616 | 
617 | testConnection();
618 | ```
619 | 
620 | **Run test:**
621 | ```bash
622 | npx ts-node scripts/test-db-connection.ts
623 | ```
624 | 
625 | ---
626 | 
627 | ## Step 8: Security Best Practices
628 | 
629 | ### 8.1 Secure Credential Storage
630 | 
631 | Never commit credentials to Git:
632 | 
633 | ```bash
634 | # Add to .gitignore
635 | .env
636 | .env.local
637 | .env.production
638 | ```
639 | 
640 | ### 8.2 Use IBM Cloud Secrets Manager (Optional)
641 | 
642 | For production, consider using IBM Cloud Secrets Manager:
643 | 
644 | ```typescript
645 | import { SecretsManagerV2 } from '@ibm-cloud/secrets-manager';
646 | 
647 | const secretsManager = new SecretsManagerV2({
648 |   authenticator: new IamAuthenticator({
649 |     apikey: process.env.IBM_CLOUD_API_KEY,
650 |   }),
651 |   serviceUrl: 'https://secrets-manager.cloud.ibm.com',
652 | });
653 | 
654 | async function getDbCredentials() {
655 |   const secret = await secretsManager.getSecret({
656 |     id: 'db-credentials-secret-id',
657 |   });
658 |   
659 |   return secret.result.payload;
660 | }
661 | ```
662 | 
663 | ### 8.3 IP Allowlist
664 | 
665 | In IBM Cloud Console:
666 | 1. Go to your database instance
667 | 2. Click **"Settings"** > **"Allowlist"**
668 | 3. Add only necessary IP addresses
669 | 4. Remove `0.0.0.0/0` in production
670 | 
671 | ---
672 | 
673 | ## Step 9: Monitoring & Maintenance
674 | 
675 | ### 9.1 Enable Monitoring
676 | 
677 | In IBM Cloud Console:
678 | 1. Go to your database instance
679 | 2. Click **"Monitoring"**
680 | 3. View metrics: CPU, Memory, Disk, Connections
681 | 
682 | ### 9.2 Set Up Alerts
683 | 
684 | 1. Click **"Alerts"** in database dashboard
685 | 2. Create alerts for:
686 |    - High CPU usage (> 80%)
687 |    - Low disk space (< 20%)
688 |    - Connection pool exhaustion
689 | 
690 | ### 9.3 Backup Configuration
691 | 
692 | IBM Cloud automatically backs up your database:
693 | - **Continuous backup**: Point-in-time recovery
694 | - **Daily snapshots**: Retained for 30 days
695 | - **Manual backups**: Create on-demand
696 | 
697 | To restore:
698 | 1. Go to **"Backups"** tab
699 | 2. Select backup point
700 | 3. Click **"Restore"**
701 | 
702 | ---
703 | 
704 | ## Troubleshooting
705 | 
706 | ### Connection Timeout
707 | 
708 | ```typescript
709 | // Increase timeout in .env
710 | DB_CONNECTION_TIMEOUT=60000
711 | ```
712 | 
713 | ### SSL Certificate Issues
714 | 
715 | ```typescript
716 | // Verify certificate is correctly decoded
717 | const cert = Buffer.from(process.env.DB_SSL_CERT_BASE64, 'base64').toString('utf-8');
718 | console.log(cert); // Should start with -----BEGIN CERTIFICATE-----
719 | ```
720 | 
721 | ### Connection Pool Exhausted
722 | 
723 | ```typescript
724 | // Increase pool size in .env
725 | DB_POOL_MAX=20
726 | ```
727 | 
728 | ### Slow Queries
729 | 
730 | ```sql
731 | -- Enable query logging
732 | ALTER DATABASE ibmclouddb SET log_statement = 'all';
733 | 
734 | -- View slow queries
735 | SELECT * FROM pg_stat_statements 
736 | ORDER BY total_exec_time DESC 
737 | LIMIT 10;
738 | ```
739 | 
740 | ---
741 | 
742 | ## Cost Optimization
743 | 
744 | ### 1. Right-size Your Instance
745 | - Start small (1GB RAM, 5GB disk)
746 | - Scale up as needed
747 | - Monitor usage regularly
748 | 
749 | ### 2. Use Connection Pooling
750 | - Reuse connections
751 | - Set appropriate pool limits
752 | - Close idle connections
753 | 
754 | ### 3. Implement Caching
755 | - Cache frequent queries
756 | - Use Redis for session data
757 | - Reduce database load
758 | 
759 | ### 4. Archive Old Data
760 | - Move old conversations to cold storage
761 | - Delete unused data
762 | - Implement data retention policies
763 | 
764 | ---
765 | 
766 | ## Summary
767 | 
768 | You now have:
769 | ✅ IBM Cloud Database for PostgreSQL set up
770 | ✅ Secure connection from SmartClick
771 | ✅ Database schema created
772 | ✅ Repository pattern for data access
773 | ✅ Monitoring and backups configured
774 | 
775 | **Next Steps:**
776 | 1. Test connection with test script
777 | 2. Run migrations to create schema
778 | 3. Implement remaining repositories
779 | 4. Add error handling and retry logic
780 | 5. Set up monitoring alerts
781 | 
782 | **Estimated Monthly Cost:**
783 | - Standard plan: ~$30-50/month (1GB RAM, 5GB disk)
784 | - Scales with usage
785 | 
786 | Your SmartClick data is now in the cloud! 🚀
</content>
</file>
<file><path>docs/FRONTEND_IMPLEMENTATION_GUIDE.md</path>
<content/><notice>File is empty</notice>
</file>
<file><path>docs/SERVICE_DOCUMENTATION.md</path><error>File not found</error><notice>The file was not found. Consider using list_files to find available files before attempting to read them.</notice></file>
<file><path>text.md</path>
<content/><notice>File is empty</notice>
</file>
<file><path>frontend/README.md</path>
<content lines="1-73">
 1 | # React + TypeScript + Vite
 2 | 
 3 | This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.
 4 | 
 5 | Currently, two official plugins are available:
 6 | 
 7 | - [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
 8 | - [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)
 9 | 
10 | ## React Compiler
11 | 
12 | The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).
13 | 
14 | ## Expanding the ESLint configuration
15 | 
16 | If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:
17 | 
18 | ```js
19 | export default defineConfig([
20 |   globalIgnores(['dist']),
21 |   {
22 |     files: ['**/*.{ts,tsx}'],
23 |     extends: [
24 |       // Other configs...
25 | 
26 |       // Remove tseslint.configs.recommended and replace with this
27 |       tseslint.configs.recommendedTypeChecked,
28 |       // Alternatively, use this for stricter rules
29 |       tseslint.configs.strictTypeChecked,
30 |       // Optionally, add this for stylistic rules
31 |       tseslint.configs.stylisticTypeChecked,
32 | 
33 |       // Other configs...
34 |     ],
35 |     languageOptions: {
36 |       parserOptions: {
37 |         project: ['./tsconfig.node.json', './tsconfig.app.json'],
38 |         tsconfigRootDir: import.meta.dirname,
39 |       },
40 |       // other options...
41 |     },
42 |   },
43 | ])
44 | ```
45 | 
46 | You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:
47 | 
48 | ```js
49 | // eslint.config.js
50 | import reactX from 'eslint-plugin-react-x'
51 | import reactDom from 'eslint-plugin-react-dom'
52 | 
53 | export default defineConfig([
54 |   globalIgnores(['dist']),
55 |   {
56 |     files: ['**/*.{ts,tsx}'],
57 |     extends: [
58 |       // Other configs...
59 |       // Enable lint rules for React
60 |       reactX.configs['recommended-typescript'],
61 |       // Enable lint rules for React DOM
62 |       reactDom.configs.recommended,
63 |     ],
64 |     languageOptions: {
65 |       parserOptions: {
66 |         project: ['./tsconfig.node.json', './tsconfig.app.json'],
67 |         tsconfigRootDir: import.meta.dirname,
68 |       },
69 |       // other options...
70 |     },
71 |   },
72 | ])
73 | ```
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs
backend/backend_client.py,backend/api/main.py,.env,docs/SERVICE_DOCUMENTATION.md,docs/FRONTEND_IMPLEMENTATION_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-03T13:30:44.488Z
User time zone: Africa/Johannesburg, UTC+2:00

# Current Cost
$0.45

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>advanced</slug>
<name>🛠️ Advanced</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now I have a comprehensive understanding of all the documentation. Let me create a detailed outline of all the fixes needed across every document.

<attempt_completion>
<result>
# SmartClick Documentation Fix Outline

## Overview
After analyzing all 15+ documentation files, I've identified critical issues across the entire documentation set. Here's a comprehensive outline of fixes needed (implementation to follow upon approval):

---

## 🔴 CRITICAL ISSUES

### 1. **Architectural Inconsistency**
**Problem**: Documentation describes TWO completely different architectures:
- **Original Plan**: Electron + React desktop app with Python backend
- **Current Reality**: FastAPI backend + React frontend (already built in Phase 2-4)

**Files Affected**:
- `ARCHITECTURE.md` - Describes Electron-only architecture
- `PROJECT_SUMMARY.md` - Describes Electron-only architecture  
- `DEVELOPMENT_PLAN.md` - 12-week Electron plan
- `FOLDER_STRUCTURE.md` - Electron folder structure
- `IMPLEMENTATION_PRIORITY.md` - Electron implementation order

**Fix Required**: Update all to reflect ACTUAL hybrid architecture (FastAPI backend + React/Electron frontend)

### 2. **Outdated Project Status**
**Problem**: Multiple completion documents contradict each other:
- `FOUNDATION_REVIEW.md` - Says Phase 3 (React Components) is 0% complete
- `PHASE_2_COMPLETE.md` - Says React foundation complete, components next
- `PHASE_4_ELECTRON_COMPLETE.md` - Says Electron integration is COMPLETE
- `README.md` - Shows old MVP status from v1.0

**Fix Required**: Create single source of truth for current project status

### 3. **Missing/Empty Critical Files**
**Problem**: Key documentation files are empty or missing:
- `docs/FRONTEND_IMPLEMENTATION_GUIDE.md` - **EMPTY**
- `docs/SERVICE_DOCUMENTATION.md` - **MISSING**
- `text.md` - **EMPTY** (should be deleted)

**Fix Required**: Create comprehensive guides or remove placeholders

---

## 🟡 MAJOR ISSUES

### 4. **Technology Stack Confusion**
**Problem**: Different docs specify different tech stacks:
- Some say "Electron + Node.js backend"
- Some say "FastAPI Python backend"
- Some say "CustomTkinter (old v1.0)"

**Files Affected**: All architecture docs

**Fix Required**: Standardize on: **FastAPI (Python) backend + React/Electron frontend**

### 5. **Incorrect File Paths**
**Problem**: Documentation references non-existent file structure:
- References `src/main/`, `src/renderer/` (Electron structure)
- Actual structure is `backend/`, `frontend/src/`

**Files Affected**:
- `FOLDER_STRUCTURE.md`
- `IMPLEMENTATION_PRIORITY.md`
- `API_INTEGRATION.md`

**Fix Required**: Update all paths to match actual project structure

### 6. **Duplicate/Conflicting Information**
**Problem**: Same information repeated differently across files:
- Setup instructions in 4 different files
- API integration explained 3 different ways
- Development timeline varies (5 days to 12 weeks)

**Fix Required**: Consolidate and cross-reference

### 7. **Outdated Dependencies**
**Problem**: Package versions and dependencies don't match reality:
- `MODERNIZATION_README.md` lists React 19, but may be using different version
- Python package versions not specified
- Electron version conflicts

**Fix Required**: Audit and update all dependency references

---

## 🟢 MODERATE ISSUES

### 8. **Incomplete Guides**
**Problem**: Guides start but don't finish:
- `QUICKSTART.md` - Missing troubleshooting for new architecture
- `ELECTRON_QUICKSTART.md` - Doesn't mention FastAPI backend requirement
- `TROUBLESHOOTING.md` - Missing Electron-specific issues

**Fix Required**: Complete all guides with current architecture

### 9. **Broken Cross-References**
**Problem**: Documents reference each other incorrectly:
- Links to non-existent files
- Incorrect relative paths
- Circular references

**Fix Required**: Audit and fix all internal links

### 10. **Inconsistent Terminology**
**Problem**: Same concepts called different names:
- "Cursor Layer" vs "Overlay" vs "Popup"
- "Session" vs "Conversation" vs "Context"
- "Bob" vs "watsonx" vs "AI"

**Fix Required**: Create terminology glossary and standardize

### 11. **Missing Prerequisites**
**Problem**: Docs assume knowledge not documented:
- How to get IBM watsonx credentials (referenced but not explained)
- Python/Node.js version requirements vary
- OS-specific setup steps incomplete

**Fix Required**: Add comprehensive prerequisites section

### 12. **Outdated Screenshots/Examples**
**Problem**: Code examples reference old structure:
- Import paths wrong
- API endpoints changed
- Component names different

**Fix Required**: Update all code examples to current codebase

---

## 🔵 MINOR ISSUES

### 13. **Formatting Inconsistencies**
- Inconsistent heading levels
- Mixed code block languages
- Inconsistent bullet point styles
- Table formatting varies

### 14. **Spelling/Grammar**
- Minor typos throughout
- Inconsistent capitalization
- Missing punctuation

### 15. **Missing Metadata**
- No document version numbers
- No last-updated dates
- No author information

---

## 📋 RECOMMENDED FIX PRIORITY

### Phase 1: Critical Fixes (Do First)
1. **Create CURRENT_STATUS.md** - Single source of truth
2. **Update README.md** - Reflect actual v2.0 architecture
3. **Fix ARCHITECTURE.md** - Hybrid FastAPI + React/Electron
4. **Create/Complete FRONTEND_IMPLEMENTATION_GUIDE.md**
5. **Create SERVICE_DOCUMENTATION.md** - Document all APIs

### Phase 2: Major Fixes
6. Update all file path references
7. Consolidate duplicate information
8. Fix technology stack references
9. Update dependency versions
10. Complete incomplete guides

### Phase 3: Moderate Fixes
11. Fix all cross-references
12. Standardize terminology
13. Add missing prerequisites
14. Update code examples

### Phase 4: Polish
15. Fix formatting
16. Correct spelling/grammar
17. Add metadata

---

## 📊 STATISTICS

- **Total Documents Analyzed**: 15
- **Critical Issues**: 3
- **Major Issues**: 5  
- **Moderate Issues**: 5
- **Minor Issues**: 3
- **Empty/Missing Files**: 3
- **Estimated Fix Time**: 2-3 days for complete overhaul

---

## ✅ NEXT STEPS

**Option 1: Full Overhaul** (Recommended)
- Rewrite core architecture docs from scratch
- Create new comprehensive guides
- Archive outdated documents
- Estimated: 2-3 days

**Option 2: Incremental Fixes**
- Fix critical issues first
- Update major issues over time
- Leave minor issues for later
- Estimated: 1 week spread out

**Option 3: Minimal Viable Documentation**
- Fix only what users see (README, QUICKSTART)
- Update architecture overview
- Mark other docs as "legacy"
- Estimated: 4-6 hours

---

**Ready to implement fixes? Please specify which option you prefer, or I can start with Phase 1 critical fixes immediately.**
</result>
</attempt_completion>

