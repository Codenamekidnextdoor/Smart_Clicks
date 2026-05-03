"use strict";
/**
 * Electron Preload Script
 * Provides secure bridge between main process and renderer
 */
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
// ============================================================================
// Exposed API
// ============================================================================
const electronAPI = {
    // Text selection events
    onTextSelected: (callback) => {
        // Remove previous listener before adding so we never accumulate duplicates.
        electron_1.ipcRenderer.removeAllListeners('text-selected');
        electron_1.ipcRenderer.on('text-selected', (_event, data) => callback(data));
    },
    // Close the floating popup window
    closePopup: () => electron_1.ipcRenderer.send('close-popup'),
    // Move the OS-level window (used for unrestricted drag across full screen)
    moveWindow: (x, y) => electron_1.ipcRenderer.send('move-window', { x, y }),
    // Get the current OS-level window position
    getWindowPosition: () => electron_1.ipcRenderer.invoke('get-window-position'),
    // Window controls
    minimizeWindow: () => electron_1.ipcRenderer.send('minimize-window'),
    maximizeWindow: () => electron_1.ipcRenderer.send('maximize-window'),
    closeWindow: () => electron_1.ipcRenderer.send('close-window'),
    // System info
    getPlatform: () => process.platform,
    getVersion: () => process.versions.electron,
    // Clipboard
    writeClipboard: (text) => electron_1.ipcRenderer.invoke('write-clipboard', text),
    readClipboard: () => electron_1.ipcRenderer.invoke('read-clipboard'),
    // Notifications
    showNotification: (title, body) => {
        electron_1.ipcRenderer.send('show-notification', { title, body });
    },
};
// Expose protected methods to renderer
electron_1.contextBridge.exposeInMainWorld('electron', electronAPI);
// Made with Bob
