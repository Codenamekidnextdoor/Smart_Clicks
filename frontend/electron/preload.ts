/**
 * Electron Preload Script
 * Provides secure bridge between main process and renderer
 */

import { contextBridge, ipcRenderer } from 'electron';

// ============================================================================
// Exposed API
// ============================================================================

const electronAPI = {
  // Text selection events
  onTextSelected: (callback: (data: { text: string; x: number; y: number }) => void) => {
    // Remove previous listener before adding so we never accumulate duplicates.
    ipcRenderer.removeAllListeners('text-selected');
    ipcRenderer.on('text-selected', (_event, data) => callback(data));
  },

  // Close the floating popup window
  closePopup: () => ipcRenderer.send('close-popup'),

  // Move the OS-level window (used for unrestricted drag across full screen)
  moveWindow: (x: number, y: number) => ipcRenderer.send('move-window', { x, y }),

  // Window controls
  minimizeWindow: () => ipcRenderer.send('minimize-window'),
  maximizeWindow: () => ipcRenderer.send('maximize-window'),
  closeWindow: () => ipcRenderer.send('close-window'),

  // System info
  getPlatform: () => process.platform,
  getVersion: () => process.versions.electron,

  // Clipboard
  writeClipboard: (text: string) => ipcRenderer.invoke('write-clipboard', text),
  readClipboard: () => ipcRenderer.invoke('read-clipboard'),

  // Notifications
  showNotification: (title: string, body: string) => {
    ipcRenderer.send('show-notification', { title, body });
  },
};

// Expose protected methods to renderer
contextBridge.exposeInMainWorld('electron', electronAPI);

// Made with Bob
