/**
 * SmartClick App Store
 * Global application state management using Zustand
 */

import { create } from 'zustand';
import { devtools } from 'zustand/middleware';
import { api } from '../services/api';
import type { Session, AppState } from '../types';

interface AppStore extends AppState {
  // Actions
  enable: () => void;
  disable: () => void;
  setCurrentSession: (session: Session | null) => void;
  loadSessions: () => Promise<void>;
  createSession: (selectedText: string, x?: number, y?: number) => Promise<number>;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  clearError: () => void;
}

export const useAppStore = create<AppStore>()(
  devtools(
    (set, get) => ({
      // Initial state
      enabled: false,
      currentSession: null,
      sessions: [],
      loading: false,
      error: null,

      // Actions
      enable: () => {
        console.log('[AppStore] Enabling SmartClick');
        set({ enabled: true, error: null });
      },

      disable: () => {
        console.log('[AppStore] Disabling SmartClick');
        set({ enabled: false, currentSession: null, error: null });
      },

      setCurrentSession: (session) => {
        console.log('[AppStore] Setting current session:', session?.id);
        set({ currentSession: session });
      },

      loadSessions: async () => {
        console.log('[AppStore] Loading sessions');
        set({ loading: true, error: null });
        
        try {
          const sessions = await api.getSessions(15);
          set({ sessions, loading: false });
          console.log('[AppStore] Loaded', sessions.length, 'sessions');
        } catch (error) {
          const message = error instanceof Error ? error.message : 'Failed to load sessions';
          console.error('[AppStore] Error loading sessions:', message);
          set({ error: message, loading: false });
        }
      },

      createSession: async (selectedText, x, y) => {
        console.log('[AppStore] Creating session');
        set({ loading: true, error: null });
        
        try {
          const { session_id } = await api.createSession({
            selected_text: selectedText,
            cursor_x: x,
            cursor_y: y,
          });
          
          console.log('[AppStore] Created session:', session_id);
          
          // Reload sessions to include the new one
          await get().loadSessions();
          
          set({ loading: false });
          return session_id;
        } catch (error) {
          const message = error instanceof Error ? error.message : 'Failed to create session';
          console.error('[AppStore] Error creating session:', message);
          set({ error: message, loading: false });
          throw error;
        }
      },

      setLoading: (loading) => {
        set({ loading });
      },

      setError: (error) => {
        set({ error });
      },

      clearError: () => {
        set({ error: null });
      },
    }),
    { name: 'AppStore' }
  )
);

// Made with Bob
