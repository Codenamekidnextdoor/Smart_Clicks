# SmartClick Quick Start Guide

## 🚀 Get Started in 5 Minutes!

### Step 1: Install Dependencies

```bash
npm install
```

This will install all required packages including:
- Electron
- React
- TypeScript
- IBM watsonx SDK
- And more...

### Step 2: Configure Environment Variables

1. Copy the example file:
```bash
copy .env.example .env
```

2. Edit `.env` and add your IBM watsonx credentials:
```env
WATSONX_API_KEY=your_actual_api_key_here
WATSONX_PROJECT_ID=your_actual_project_id_here
```

**Where to get these:**
- API Key: https://cloud.ibm.com/iam/apikeys
- Project ID: Look at URL when in your watsonx project

### Step 3: Run the App

```bash
npm run dev
```

This will:
- Compile TypeScript
- Start Vite dev server
- Launch Electron app
- Open with hot reload enabled

### Step 4: Test It!

1. The SmartClick window will appear
2. Paste some text in the textarea
3. Click "Summarize", "Rewrite", or "Explain"
4. See the AI response!

## 📝 What You Have

✅ Complete Electron + React app
✅ IBM watsonx AI integration (mock for now)
✅ Beautiful UI with animations
✅ IPC communication working
✅ TypeScript throughout
✅ Hot reload for development

## 🔧 Development Commands

```bash
# Start development mode
npm run dev

# Build for production
npm run build

# Create installers
npm run package

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format
```

## 📁 Project Structure

```
Smart_Clicks/
├── src/
│   ├── main/              # Electron main process
│   │   ├── index.ts       # Entry point
│   │   ├── app.ts         # App initialization
│   │   ├── ipc/           # IPC handlers
│   │   ├── services/      # Business logic
│   │   └── utils/         # Utilities
│   ├── renderer/          # React UI
│   │   └── overlay/       # Popup interface
│   ├── preload/           # Preload scripts
│   └── shared/            # Shared code
├── docs/                  # Documentation
└── tests/                 # Tests
```

## 🎯 Next Steps

### For Hackathon (Quick Demo):

1. **Keep it simple** - The current mock AI works for demo
2. **Focus on UI** - Make it look good
3. **Practice demo** - 3-minute pitch
4. **Add real AI later** - After you win! 🏆

### For Production:

1. **Replace mock AI** with real IBM watsonx SDK:
   - See `docs/API_INTEGRATION.md`
   - Update `src/main/services/ai/watsonx-client.ts`

2. **Add text selection detection**:
   - See `docs/DEVELOPMENT_PLAN.md` Phase 2
   - Implement platform-specific APIs

3. **Add database** (optional):
   - See `docs/IBM_CLOUD_DATABASE_SETUP.md`
   - Or use local SQLite

4. **Add more features**:
   - Chat interface
   - Settings UI
   - Keyboard shortcuts
   - System tray

## 🐛 Troubleshooting

### "Cannot find module" errors
```bash
npm install
```

### "Missing environment variables"
Check your `.env` file has:
- WATSONX_API_KEY
- WATSONX_PROJECT_ID

### App won't start
1. Check Node.js version (need 18+)
2. Delete `node_modules` and `package-lock.json`
3. Run `npm install` again

### TypeScript errors
These are normal before `npm install`. They'll go away after installing dependencies.

## 📚 Documentation

- **Architecture**: `docs/ARCHITECTURE.md`
- **Development Plan**: `docs/DEVELOPMENT_PLAN.md`
- **API Integration**: `docs/API_INTEGRATION.md`
- **Implementation Priority**: `docs/IMPLEMENTATION_PRIORITY.md`
- **Database Setup**: `docs/IBM_CLOUD_DATABASE_SETUP.md`

## 💡 Tips

1. **Start simple** - Get one feature working perfectly
2. **Test often** - Run the app frequently
3. **Read logs** - Check console for errors
4. **Ask for help** - Check documentation
5. **Have fun!** - You're building something cool! 🚀

## ✅ Checklist

- [ ] Dependencies installed (`npm install`)
- [ ] `.env` file created with credentials
- [ ] App runs (`npm run dev`)
- [ ] Can see the UI
- [ ] Buttons work (even with mock responses)
- [ ] Ready to demo or develop further!

**You're all set! Time to build SmartClick! 🎉**