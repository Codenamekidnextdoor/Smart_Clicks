/**
 * Electron API Type Definitions
 * Extends the Window interface with Electron APIs
 */

export interface ElectronAPI {
  onTextSelected: (callback: (data: { text: string; x: number; y: number }) => void) => void;
  closePopup: () => void;
  moveWindow: (x: number, y: number) => void;
  getWindowPosition: () => Promise<{ x: number; y: number }>;
  minimizeWindow: () => void;
  maximizeWindow: () => void;
  closeWindow: () => void;
  showWindow: () => void;
  getPlatform: () => string;
  getVersion: () => string;
  writeClipboard: (text: string) => Promise<void>;
  readClipboard: () => Promise<string>;
  showNotification: (title: string, body: string) => void;
}

declare global {
  interface Window {
    electron?: ElectronAPI;
  }
}

export {};

// Made with Bob
