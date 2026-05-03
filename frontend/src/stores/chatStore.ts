/**
 * SmartClick Chat Store
 * Manages chat messages and streaming state
 */

import { create } from 'zustand';
import { devtools } from 'zustand/middleware';
import { api } from '../services/api';
import { wsClient } from '../services/websocket';
import type { Message, ChatState, ActionType } from '../types';

interface ChatStore extends ChatState {
  // Actions
  loadMessages: (sessionId: number) => Promise<void>;
  sendMessage: (sessionId: number, message: string, context?: string) => Promise<void>;
  performAction: (sessionId: number, action: ActionType, text: string) => Promise<void>;
  addMessage: (message: Message) => void;
  clearMessages: () => void;
  setStreaming: (isStreaming: boolean) => void;
  setLoading: (isLoading: boolean) => void;
  setError: (error: string | null) => void;
}

export const useChatStore = create<ChatStore>()(
  devtools(
    (set, get) => ({
      // Initial state
      messages: [],
      isStreaming: false,
      isLoading: false,
      error: null,

      // Actions
      loadMessages: async (sessionId) => {
        console.log('[ChatStore] Loading messages for session:', sessionId);
        set({ isLoading: true, error: null });
        
        try {
          const messages = await api.getSessionMessages(sessionId);
          set({ messages, isLoading: false });
          console.log('[ChatStore] Loaded', messages.length, 'messages');
        } catch (error) {
          const message = error instanceof Error ? error.message : 'Failed to load messages';
          console.error('[ChatStore] Error loading messages:', message);
          set({ error: message, isLoading: false });
        }
      },

      sendMessage: async (sessionId, message, context) => {
        console.log('[ChatStore] Sending message:', message);
        set({ isStreaming: true, error: null });
        
        // Add user message immediately
        const userMessage: Message = {
          id: Date.now(), // Temporary ID
          session_id: sessionId,
          role: 'user',
          content: message,
          created_at: new Date().toISOString(),
        };
        set((state) => ({ messages: [...state.messages, userMessage] }));
        
        try {
          // Use WebSocket for streaming response
          let assistantContent = '';
          const assistantMessage: Message = {
            id: Date.now() + 1, // Temporary ID
            session_id: sessionId,
            role: 'assistant',
            content: '',
            created_at: new Date().toISOString(),
          };
          
          // Add empty assistant message
          set((state) => ({ messages: [...state.messages, assistantMessage] }));
          
          await wsClient.streamChat(
            { message, context, session_id: sessionId },
            (chunk) => {
              // Update assistant message with new chunk
              assistantContent += chunk;
              set((state) => ({
                messages: state.messages.map((msg) =>
                  msg.id === assistantMessage.id
                    ? { ...msg, content: assistantContent }
                    : msg
                ),
              }));
            },
            () => {
              // Stream complete
              console.log('[ChatStore] Stream complete');
              set({ isStreaming: false });
            },
            (error) => {
              // Stream error
              console.error('[ChatStore] Stream error:', error);
              set({ error, isStreaming: false });
            }
          );
        } catch (error) {
          const message = error instanceof Error ? error.message : 'Failed to send message';
          console.error('[ChatStore] Error sending message:', message);
          set({ error: message, isStreaming: false });
        }
      },

      performAction: async (sessionId, action, text) => {
        console.log('[ChatStore] Performing action:', action);
        set({ isLoading: true, error: null });
        
        // Add user message
        const userMessage: Message = {
          id: Date.now(),
          session_id: sessionId,
          role: 'user',
          content: `${action.charAt(0).toUpperCase() + action.slice(1)} this text`,
          created_at: new Date().toISOString(),
        };
        set((state) => ({ messages: [...state.messages, userMessage] }));
        
        try {
          const response = await api.performAction(action, { text, session_id: sessionId });
          
          // Add assistant response
          const assistantMessage: Message = {
            id: Date.now() + 1,
            session_id: sessionId,
            role: 'assistant',
            content: response,
            created_at: new Date().toISOString(),
          };
          set((state) => ({
            messages: [...state.messages, assistantMessage],
            isLoading: false,
          }));
          
          console.log('[ChatStore] Action complete');
        } catch (error) {
          const message = error instanceof Error ? error.message : 'Failed to perform action';
          console.error('[ChatStore] Error performing action:', message);
          set({ error: message, isLoading: false });
        }
      },

      addMessage: (message) => {
        set((state) => ({ messages: [...state.messages, message] }));
      },

      clearMessages: () => {
        set({ messages: [], error: null });
      },

      setStreaming: (isStreaming) => {
        set({ isStreaming });
      },

      setLoading: (isLoading) => {
        set({ isLoading });
      },

      setError: (error) => {
        set({ error });
      },
    }),
    { name: 'ChatStore' }
  )
);

// Made with Bob
