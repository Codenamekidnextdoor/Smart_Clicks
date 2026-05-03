/**
 * Electron Main Process
 * Handles window management, system tray, and global hotkeys
 */

import { app, BrowserWindow, Tray, Menu, globalShortcut, screen, ipcMain } from 'electron';
import path from 'path';
import http from 'http';

let mainWindow: BrowserWindow | null = null;
let popupWindow: BrowserWindow | null = null;
let tray: Tray | null = null;
let isQuitting = false;

// app.isPackaged is false during development and true in a built binary.
// This is more reliable than NODE_ENV which is often not set when launching via `electron .`
const isDev = !app.isPackaged;
const VITE_DEV_SERVER_URL = 'http://localhost:5174';

// ============================================================================
// Window Management
// ============================================================================

function createMainWindow() {
  mainWindow = new BrowserWindow({
    width: 900,
    height: 600,
    minWidth: 800,
    minHeight: 500,
    backgroundColor: '#0a0a0a',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.cjs'),
    },
    icon: path.join(__dirname, '../public/icon.png'),
    show: false, // Don't show until ready
  });

  // Load the app
  if (isDev) {
    mainWindow.loadURL(VITE_DEV_SERVER_URL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, '../dist/index.html'));
  }

  // Show window when ready
  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  // Handle window close
  mainWindow.on('close', (event) => {
    if (!isQuitting) {
      event.preventDefault();
      mainWindow?.hide();
    }
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// ============================================================================
// System Tray
// ============================================================================

function createTray() {
  // Create tray icon — use favicon.svg as fallback if tray-icon.png is invalid
  let iconPath = path.join(__dirname, '../public/tray-icon.png');
  try {
    tray = new Tray(iconPath);
  } catch {
    try {
      iconPath = path.join(__dirname, '../public/icon.png');
      tray = new Tray(iconPath);
    } catch (e) {
      console.warn('Tray icon could not be loaded, running without system tray:', e);
      return;
    }
  }

  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Show SmartClick',
      click: () => {
        mainWindow?.show();
      },
    },
    {
      label: 'Hide SmartClick',
      click: () => {
        mainWindow?.hide();
      },
    },
    { type: 'separator' },
    {
      label: 'Quit',
      click: () => {
        isQuitting = true;
        app.quit();
      },
    },
  ]);

  tray.setToolTip('SmartClick - AI Cursor Layer');
  tray.setContextMenu(contextMenu);

  // Show/hide window on tray click
  tray.on('click', () => {
    if (mainWindow?.isVisible()) {
      mainWindow.hide();
    } else {
      mainWindow?.show();
    }
  });
}

// ============================================================================
// Popup Window — separate always-on-top window that floats over all apps
// ============================================================================

function createPopupWindow(text: string, screenX: number, screenY: number) {
  // Close any existing popup first
  if (popupWindow && !popupWindow.isDestroyed()) {
    popupWindow.close();
  }

  // Clamp so the popup is fully visible on whatever display it appears on
  const display = screen.getDisplayNearestPoint({ x: screenX, y: screenY });
  const { bounds } = display;
  const winW = 400;
  const winH = 560;
  const clampedX = Math.min(Math.max(screenX, bounds.x + 8), bounds.x + bounds.width - winW - 8);
  const clampedY = Math.min(Math.max(screenY, bounds.y + 8), bounds.y + bounds.height - winH - 8);

  const isMac = process.platform === 'darwin';
  popupWindow = new BrowserWindow({
    width: winW,
    height: winH,
    x: clampedX,
    y: clampedY,
    frame: false,
    transparent: true,
    hasShadow: false,           // required for correct transparency on macOS
    alwaysOnTop: true,
    skipTaskbar: true,
    resizable: false,
    // On macOS use 'floating' panel level so popup stays above full-screen apps
    ...(isMac ? { type: 'panel' as const } : {}),
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.cjs'),
    },
  });

  if (isDev) {
    popupWindow.loadURL(`${VITE_DEV_SERVER_URL}?mode=popup`);
  } else {
    popupWindow.loadFile(path.join(__dirname, '../dist/index.html'), { query: { mode: 'popup' } });
  }

  // Send the captured text once the page is ready
  popupWindow.webContents.once('did-finish-load', () => {
    popupWindow?.webContents.send('text-selected', { text, x: 8, y: 8 });
  });

  popupWindow.on('closed', () => {
    popupWindow = null;
  });
}

// ============================================================================
// Global Hotkeys
// ============================================================================

function registerHotkeys() {
  // Ctrl+Shift+B on Windows/Linux, Cmd+Shift+Z on macOS
  const isMac = process.platform === 'darwin';
  const hotkey = isMac ? 'Command+Shift+Z' : 'Control+Shift+B';

  const registered = globalShortcut.register(hotkey, async () => {
    console.log(`Hotkey pressed: ${hotkey}`);

    // Blur the Electron window so the source app regains focus before we
    // simulate Ctrl+C.  Without this the backend copies an empty selection.
    if (mainWindow && mainWindow.isFocused()) {
      mainWindow.blur();
      // macOS needs more time to transfer focus back than Windows/Linux
      const blurDelay = process.platform === 'darwin' ? 300 : 150;
      await new Promise((r) => setTimeout(r, blurDelay));
    }

    // Ask the Python backend to capture currently-selected text via Ctrl+C simulation.
    const selectedText = await captureTextFromBackend();

    if (selectedText) {
      const cursorPos = screen.getCursorScreenPoint();
      // Open the floating popup window at the cursor's screen position
      createPopupWindow(selectedText, cursorPos.x, cursorPos.y);
      console.log('Text captured:', selectedText.substring(0, 50) + '...');
    } else {
      console.log('No text captured from backend');
    }
  });

  if (!registered) {
    console.error('Failed to register global hotkey');
  } else {
    console.log(`Global hotkey registered: ${hotkey}`);
  }
}

/**
 * Ask the Python FastAPI backend to simulate Ctrl+C and return the selected text.
 * Uses Node's built-in http module (no extra dependencies).
 */
function captureTextFromBackend(): Promise<string> {
  return new Promise((resolve) => {
    const req = http.request(
      { hostname: '127.0.0.1', port: 8000, path: '/api/capture-text', method: 'POST' },
      (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          try { resolve(JSON.parse(data).text || ''); }
          catch { resolve(''); }
        });
      }
    );
    req.on('error', (e) => {
      console.error('Backend capture-text error:', e.message);
      resolve('');
    });
    req.end();
  });
}

// ============================================================================
// App Lifecycle
// ============================================================================

app.whenReady().then(() => {
  // On macOS, check for Accessibility permission needed for text capture via pynput.
  // Prompt the user immediately so they know what to enable.
  if (process.platform === 'darwin') {
    const { systemPreferences } = require('electron');
    const trusted = systemPreferences.isTrustedAccessibilityClient(false);
    if (!trusted) {
      // Calling with `true` shows the system prompt asking user to grant access
      systemPreferences.isTrustedAccessibilityClient(true);
      console.warn('[macOS] Accessibility permission not granted — text capture will not work.');
      console.warn('[macOS] Go to: System Settings → Privacy & Security → Accessibility → add Terminal');
    }
  }

  createMainWindow();
  createTray();
  registerHotkeys();

  // Let the popup window close itself via IPC
  ipcMain.on('close-popup', () => {
    if (popupWindow && !popupWindow.isDestroyed()) {
      popupWindow.close();
    }
  });

  // Move the popup window to an absolute screen position (for full-screen drag)
  ipcMain.on('move-window', (_event, { x, y }: { x: number; y: number }) => {
    if (popupWindow && !popupWindow.isDestroyed()) {
      popupWindow.setPosition(Math.round(x), Math.round(y));
    }
  });

  // Return the popup window's current screen position
  ipcMain.handle('get-window-position', () => {
    if (popupWindow && !popupWindow.isDestroyed()) {
      const [x, y] = popupWindow.getPosition();
      return { x, y };
    }
    return { x: 0, y: 0 };
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow();
    } else {
      mainWindow?.show();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('will-quit', () => {
  // Unregister all shortcuts
  globalShortcut.unregisterAll();
});

app.on('before-quit', () => {
  isQuitting = true;
});

// ============================================================================
// Error Handling
// ============================================================================

process.on('uncaughtException', (error) => {
  console.error('Uncaught exception:', error);
});

process.on('unhandledRejection', (error) => {
  console.error('Unhandled rejection:', error);
});

// Made with Bob
