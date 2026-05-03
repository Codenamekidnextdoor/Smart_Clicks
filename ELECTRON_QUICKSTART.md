# SmartClick Electron - Quick Start Guide

## Prerequisites

1. **Backend Running**
   ```bash
   cd backend
   python run.py
   ```
   Backend should be running on http://127.0.0.1:8000

2. **Dependencies Installed**
   ```bash
   cd frontend
   npm install
   ```

## Running the Electron App

### Option 1: Development Mode (Recommended for Testing)

```bash
cd frontend
npm run electron:dev
```

This will:
- Start Vite dev server on http://localhost:5174
- Wait for server to be ready
- Launch Electron with DevTools open
- Enable hot module replacement (HMR)

**What you'll see:**
- Main window opens with SmartClick UI
- System tray icon appears (look for it in your taskbar)
- DevTools open for debugging
- Console logs show "Running in Electron mode"

### Option 2: Compiled Mode

```bash
cd frontend
npm run electron:start
```

This will:
- Compile Electron TypeScript files to `dist-electron/`
- Launch Electron with compiled files
- Use Vite dev server for React app

### Option 3: Production Build

```bash
cd frontend
npm run build              # Build React app
npm run electron:compile   # Compile Electron files
npm run electron:build     # Package for distribution
```

Output in `frontend/release/`:
- Windows: `SmartClick Setup.exe` + portable version
- macOS: `SmartClick.dmg` + ZIP
- Linux: `SmartClick.AppImage` + DEB package

## Testing the Global Hotkey

1. **Start the app** using one of the methods above
2. **Enable SmartClick** by clicking the "Enable" button in the main window
3. **Open any text editor** (Notepad, VS Code, browser, etc.)
4. **Select some text**
5. **Press Ctrl+Shift+Z**
6. **Popup should appear** at your cursor position with the selected text

## System Tray Features

**Right-click the tray icon:**
- Show SmartClick - Opens the main window
- Hide SmartClick - Hides the main window
- Quit - Exits the application

**Left-click the tray icon:**
- Toggles window visibility (show/hide)

**Closing the window:**
- Window hides to tray (doesn't quit)
- App continues running in background
- Use "Quit" from tray menu to exit

## Troubleshooting

### Hotkey Not Working

**Check:**
1. Is SmartClick enabled? (Green status in main window)
2. Is another app using Ctrl+Shift+Z?
3. Check console for "Hotkey pressed" message
4. Try restarting the app

**Fix:**
- Close other apps that might use the same hotkey
- Check Windows/macOS accessibility permissions
- Look for error messages in DevTools console

### Popup Not Appearing

**Check:**
1. Is text actually selected?
2. Is SmartClick enabled?
3. Check console for "Text selected" message
4. Check cursor position detection

**Fix:**
- Try selecting text again
- Check if popup is off-screen
- Restart the app

### Backend Connection Issues

**Check:**
1. Is backend running on http://127.0.0.1:8000?
2. Check backend terminal for errors
3. Check frontend console for API errors

**Fix:**
```bash
# Restart backend
cd backend
python run.py

# Check if it's running
curl http://127.0.0.1:8000/api/sessions?limit=1
```

### Compilation Errors

**If `npm run electron:compile` fails:**

```bash
# Clean and reinstall
cd frontend
rm -rf node_modules dist-electron
npm install
npm run electron:compile
```

### Build Errors

**If `npm run electron:build` fails:**

1. Make sure React app is built first:
   ```bash
   npm run build
   ```

2. Check that dist-electron exists:
   ```bash
   npm run electron:compile
   ```

3. Try building again:
   ```bash
   npm run electron:build
   ```

## Development Tips

### Hot Reload
- React changes: Instant HMR (no restart needed)
- Electron main process changes: Requires app restart
- Preload script changes: Requires app restart

### Debugging

**React (Renderer Process):**
- DevTools open automatically in dev mode
- Use `console.log()` as usual
- React DevTools extension works

**Electron (Main Process):**
- Check terminal output
- Use `console.log()` in main.ts
- Logs appear in terminal, not DevTools

**IPC Communication:**
- Log in both main and renderer
- Check preload.ts for bridge issues
- Verify event names match

### Useful Commands

```bash
# Check if Electron is installed
npx electron --version

# List all npm scripts
npm run

# Clean build artifacts
rm -rf dist dist-electron release

# Full rebuild
npm run build && npm run electron:compile && npm run electron:build
```

## File Locations

**Source Files:**
- `frontend/electron/main.ts` - Main process
- `frontend/electron/preload.ts` - Preload script
- `frontend/src/App.tsx` - React integration

**Compiled Files:**
- `frontend/dist-electron/main.js` - Compiled main
- `frontend/dist-electron/preload.js` - Compiled preload
- `frontend/dist/` - Built React app

**Build Output:**
- `frontend/release/` - Packaged installers

## Next Steps

1. **Test the hotkey** - Select text and press Ctrl+Shift+Z
2. **Test the popup** - Verify it appears at cursor position
3. **Test system tray** - Right-click icon, try show/hide
4. **Test window management** - Minimize, maximize, close
5. **Create real icons** - Replace placeholder icons
6. **Build for distribution** - Package the app

## Known Issues

1. **Text capture uses clipboard** - May interfere with user's clipboard
2. **Icons are placeholders** - Need real icon files
3. **No auto-launch** - App doesn't start with OS (yet)

## Support

If you encounter issues:
1. Check this guide first
2. Look at PHASE_4_ELECTRON_COMPLETE.md for details
3. Check console logs in both terminals
4. Verify all prerequisites are met

---

**Made with Bob** 🚀