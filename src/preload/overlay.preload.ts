import { contextBridge, ipcRenderer } from 'electron';

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // AI operations
  summarizeText: (text: string) => ipcRenderer.invoke('ai:summarize', text),
  rewriteText: (text: string, tone: string) => ipcRenderer.invoke('ai:rewrite', { text, tone }),
  explainText: (text: string) => ipcRenderer.invoke('ai:explain', text),
  analyzeText: (text: string) => ipcRenderer.invoke('ai:analyze', text),
  customPrompt: (text: string, prompt: string) => ipcRenderer.invoke('ai:custom', { text, prompt }),

  // Text selection
  onTextSelected: (callback: (data: any) => void) => {
    ipcRenderer.on('text-selected', (_event, data) => callback(data));
  },

  // Window operations
  hideWindow: () => ipcRenderer.send('window:hide'),
  showWindow: () => ipcRenderer.send('window:show'),
  
  // Settings
  getSettings: () => ipcRenderer.invoke('settings:get'),
  updateSettings: (settings: any) => ipcRenderer.invoke('settings:update', settings),
});

// Type definitions for TypeScript
declare global {
  interface Window {
    electronAPI: {
      summarizeText: (text: string) => Promise<string>;
      rewriteText: (text: string, tone: string) => Promise<string>;
      explainText: (text: string) => Promise<string>;
      analyzeText: (text: string) => Promise<string>;
      customPrompt: (text: string, prompt: string) => Promise<string>;
      onTextSelected: (callback: (data: any) => void) => void;
      hideWindow: () => void;
      showWindow: () => void;
      getSettings: () => Promise<any>;
      updateSettings: (settings: any) => Promise<void>;
    };
  }
}

// Made with Bob
