import { app, BrowserWindow } from 'electron';
import path from 'path';
import { initializeApp } from './app';

// Handle creating/removing shortcuts on Windows when installing/uninstalling
if (require('electron-squirrel-startup')) {
  app.quit();
}

let mainWindow: BrowserWindow | null = null;

const createWindow = () => {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 400,
    height: 600,
    show: false,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    webPreferences: {
      preload: path.join(__dirname, '../preload/overlay.preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  // Load the overlay UI
  if (process.env.NODE_ENV === 'development') {
    mainWindow.loadURL('http://localhost:5173/overlay/');
  } else {
    mainWindow.loadFile(path.join(__dirname, '../renderer/overlay/index.html'));
  }

  // Show window when ready
  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  // Open DevTools in development
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools();
  }
};

// This method will be called when Electron has finished initialization
app.whenReady().then(async () => {
  await initializeApp();
  createWindow();

  app.on('activate', () => {
    // On macOS, re-create window when dock icon is clicked
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Quit when all windows are closed
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Handle app quit
app.on('will-quit', () => {
  // Cleanup
  mainWindow = null;
});

// Made with Bob
