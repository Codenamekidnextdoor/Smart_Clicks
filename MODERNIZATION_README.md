# SmartClick 2.0 - React Modernization

## 🎯 Overview

This document guides you through the modernization of SmartClick from a CustomTkinter desktop app to a modern React + Electron application with a FastAPI backend.

## 🏗️ Architecture

### Before (v1.0)
```
┌─────────────────────────────────┐
│   CustomTkinter Desktop App     │
│  (UI + Logic + AI + Database)   │
└─────────────────────────────────┘
```

### After (v2.0)
```
┌──────────────────────────────────────┐
│     React + Electron Frontend        │
│  (Modern UI with smooth animations)  │
└──────────────┬───────────────────────┘
               │ REST API + WebSocket
┌──────────────▼───────────────────────┐
│       FastAPI Python Backend         │
│  (AI Logic + Database + Text Capture)│
└──────────────────────────────────────┘
```

## 📦 What's Included

### Backend (FastAPI)
- ✅ **REST API** - All CRUD operations for sessions, messages, settings
- ✅ **WebSocket** - Real-time streaming chat responses
- ✅ **AI Integration** - IBM watsonx client (existing code reused)
- ✅ **Database** - SQLite manager (existing code reused)
- ✅ **CORS** - Configured for Electron app

### Frontend (Coming Next)
- ⏳ **React + TypeScript** - Type-safe, modern UI
- ⏳ **Electron** - Desktop app wrapper with native features
- ⏳ **Zustand** - Simple state management
- ⏳ **Tailwind CSS** - Beautiful, consistent styling
- ⏳ **Framer Motion** - Smooth animations
- ⏳ **WebSocket Client** - Real-time chat streaming

## 🚀 Quick Start

### Step 1: Install Backend Dependencies

```bash
# Navigate to backend directory
cd backend

# Install FastAPI and dependencies
pip install -r requirements.txt
```

### Step 2: Start the Backend Server

```bash
# From the backend directory
python run.py
```

The API will be available at:
- **API**: http://127.0.0.1:8000
- **Docs**: http://127.0.0.1:8000/docs (Interactive API documentation)
- **Health**: http://127.0.0.1:8000/health

### Step 3: Test the API

Open http://127.0.0.1:8000/docs in your browser to see the interactive API documentation and test endpoints.

Example API calls:

```bash
# Health check
curl http://127.0.0.1:8000/health

# Create a session
curl -X POST http://127.0.0.1:8000/api/sessions \
  -H "Content-Type: application/json" \
  -d '{"selected_text": "Hello world", "cursor_x": 100, "cursor_y": 200}'

# Get recent sessions
curl http://127.0.0.1:8000/api/sessions

# Chat
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is this about?", "context": "Hello world"}'
```

## 📚 API Endpoints

### Sessions
- `POST /api/sessions` - Create new session
- `GET /api/sessions` - Get recent sessions (limit=15)
- `GET /api/sessions/{id}` - Get session details
- `GET /api/sessions/{id}/messages` - Get session messages
- `POST /api/sessions/{id}/messages` - Add message to session

### Chat
- `POST /api/chat` - Send chat message (with optional context and history)
- `POST /api/actions/{action}` - Perform quick action (summarize, rewrite, explain)
- `WS /ws/chat` - WebSocket for streaming responses

### Settings
- `GET /api/settings` - Get all settings
- `PUT /api/settings` - Update settings

### Health
- `GET /` - Basic health check
- `GET /health` - Detailed health status

## 🔧 Development Workflow

### Running Both Old and New

You can run both the old Tkinter app and the new backend simultaneously:

**Terminal 1 - Old App (for reference)**
```bash
python main.py
```

**Terminal 2 - New Backend**
```bash
cd backend
python run.py
```

This allows you to:
1. Compare functionality
2. Test API endpoints while seeing the old UI
3. Gradually migrate features

## 📋 Next Steps

### Phase 1: Backend ✅ (COMPLETED)
- [x] FastAPI setup
- [x] REST endpoints
- [x] WebSocket support
- [x] Integration with existing Python code

### Phase 2: React Frontend (NEXT)
1. **Initialize React Project**
   ```bash
   npm create vite@latest frontend -- --template react-ts
   cd frontend
   npm install
   ```

2. **Add Dependencies**
   ```bash
   npm install zustand axios socket.io-client framer-motion
   npm install -D tailwindcss postcss autoprefixer
   npm install -D electron electron-builder
   ```

3. **Setup Tailwind**
   ```bash
   npx tailwindcss init -p
   ```

4. **Create Components**
   - MainWindow
   - Popup
   - Chat interface
   - Session history

5. **Setup Electron**
   - Main process
   - Preload script
   - IPC communication
   - Global hotkeys

### Phase 3: Integration
- Connect React to FastAPI
- Implement WebSocket streaming
- Add state management
- Style with Tailwind

### Phase 4: Polish
- Animations
- Error handling
- Loading states
- Testing

## 🎨 Design System

### Colors (Dark Theme)
```css
--bg: #0a0a0a
--surface: #141414
--surface-2: #1e1e1e
--surface-3: #282828
--border: #2a2a2a
--accent: #00e676 (green)
--blue: #40c4ff
--red: #ff5252
--orange: #ffab40
--purple: #ce93d8
--text: #ffffff
--text-2: #9e9e9e
--text-3: #5a5a5a
```

### Typography
- **Headings**: Segoe UI, Bold
- **Body**: Segoe UI, Regular
- **Code**: Consolas, Monospace

## 🐛 Troubleshooting

### Backend won't start
```bash
# Make sure you're in the backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run
python run.py
```

### Import errors
```bash
# Make sure project root is in Python path
# The run.py script handles this automatically
```

### Database errors
The backend uses the same SQLite database as the old app:
- Location: `C:\Users\{username}\.smartclick\smartclick.db`
- It will be created automatically if it doesn't exist

## 📖 Documentation

- **Full Plan**: See `docs/REACT_MODERNIZATION_PLAN.md`
- **API Docs**: http://127.0.0.1:8000/docs (when server is running)
- **Architecture**: See `docs/ARCHITECTURE.md`

## 🤝 Contributing

This is a modernization project. The goal is to:
1. Keep all existing functionality
2. Improve UI/UX dramatically
3. Make the codebase more maintainable
4. Enable future enhancements

## 📝 Notes

### Why FastAPI?
- Modern, fast, async Python framework
- Automatic API documentation
- Built-in WebSocket support
- Type hints and validation
- Easy to integrate with existing code

### Why React + Electron?
- Professional, modern UI
- Cross-platform desktop app
- Native OS integration
- Large ecosystem
- Great developer experience

### Why Zustand?
- Simpler than Redux
- Less boilerplate
- Better TypeScript support
- Smaller bundle size

### Why Tailwind?
- Rapid development
- Consistent design
- No CSS conflicts
- Easy customization
- Great with React

## 🎯 Success Criteria

- ✅ Backend API working with all endpoints
- ⏳ React frontend with smooth animations
- ⏳ Electron app with global hotkeys
- ⏳ Real-time chat streaming
- ⏳ All existing features working
- ⏳ Better performance than v1.0
- ⏳ Professional, polished UI

## 🚀 Let's Build!

The backend is ready. Now let's create an amazing React frontend!

**Next command to run:**
```bash
npm create vite@latest frontend -- --template react-ts
```

---

**Questions?** Check the docs or ask for help!