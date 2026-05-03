/**
 * SmartClick TypeScript Type Definitions
 */

// ============================================================================
// Session Types
// ============================================================================

export interface Session {
  id: number;
  selected_text: string;
  app_name?: string;
  window_title?: string;
  cursor_x?: number;
  cursor_y?: number;
  created_at: string;
  updated_at: string;
  message_count: number;
}

export interface CreateSessionRequest {
  selected_text: string;
  app_name?: string;
  window_title?: string;
  cursor_x?: number;
  cursor_y?: number;
}

// ============================================================================
// Message Types
// ============================================================================

export interface Message {
  id: number;
  session_id: number;
  role: 'user' | 'assistant' | 'context';
  content: string;
  created_at: string;
}

export interface AddMessageRequest {
  role: 'user' | 'assistant';
  content: string;
}

// ============================================================================
// Chat Types
// ============================================================================

export interface ChatRequest {
  message: string;
  context?: string;
  session_id?: number;
}

export interface ChatResponse {
  response: string;
  status: string;
}

export interface ActionRequest {
  text: string;
  session_id?: number;
}

export interface ActionResponse {
  response: string;
  action: string;
  status: string;
}

export type ActionType = 'chat' | 'summarize' | 'rewrite' | 'explain';

// ============================================================================
// WebSocket Types
// ============================================================================

export interface WebSocketMessage {
  type: 'start' | 'chunk' | 'end' | 'error';
  content?: string;
  message?: string;
}

export interface WebSocketChatRequest {
  message: string;
  context?: string;
  session_id?: number;
}

// ============================================================================
// Settings Types
// ============================================================================

export interface Settings {
  watsonx_api_key?: string;
  watsonx_project_id?: string;
  watsonx_endpoint?: string;
}

// ============================================================================
// API Response Types
// ============================================================================

export interface ApiResponse<T = any> {
  data?: T;
  error?: string;
  status: number;
}

export interface SessionsResponse {
  sessions: Session[];
}

export interface SessionResponse {
  session: Session;
}

export interface MessagesResponse {
  messages: Message[];
}

export interface SettingsResponse {
  settings: Settings;
}

export interface HealthResponse {
  status: string;
  database: string;
  ai_client: string;
}

// ============================================================================
// UI State Types
// ============================================================================

export interface AppState {
  enabled: boolean;
  currentSession: Session | null;
  sessions: Session[];
  loading: boolean;
  error: string | null;
}

export interface ChatState {
  messages: Message[];
  isStreaming: boolean;
  isLoading: boolean;
  error: string | null;
}

export interface PopupState {
  isVisible: boolean;
  isExpanded: boolean;
  selectedText: string;
  position: { x: number; y: number };
}

// ============================================================================
// Component Props Types
// ============================================================================

export interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary' | 'danger' | 'success';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  className?: string;
}

export interface CardProps {
  children: React.ReactNode;
  title?: string;
  className?: string;
}

export interface ChatBubbleProps {
  message: Message;
  isStreaming?: boolean;
}

export interface SessionItemProps {
  session: Session;
  onClick: (session: Session) => void;
}

// ============================================================================
// Electron IPC Types
// ============================================================================

export interface ElectronAPI {
  // Hotkey events
  onHotkeyPressed: (callback: () => void) => void;
  
  // Window controls
  minimizeWindow: () => void;
  maximizeWindow: () => void;
  closeWindow: () => void;
  
  // System
  getSelectedText: () => Promise<string>;
  getCursorPosition: () => Promise<{ x: number; y: number }>;
  
  // Settings
  getSettings: () => Promise<Settings>;
  saveSettings: (settings: Settings) => Promise<void>;
}

declare global {
  interface Window {
    electronAPI?: ElectronAPI;
  }
}

// ============================================================================
// Utility Types
// ============================================================================

export type Nullable<T> = T | null;
export type Optional<T> = T | undefined;
export type AsyncFunction<T = void> = () => Promise<T>;

// Made with Bob
