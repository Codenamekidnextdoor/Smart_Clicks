/**
 * SmartClick API Client
 * Handles all HTTP requests to the FastAPI backend
 */

import axios from 'axios';
import type { AxiosInstance, AxiosError } from 'axios';
import type {
  Session,
  CreateSessionRequest,
  Message,
  AddMessageRequest,
  ChatRequest,
  ChatResponse,
  ActionRequest,
  ActionResponse,
  Settings,
  SessionsResponse,
  SessionResponse,
  MessagesResponse,
  SettingsResponse,
  HealthResponse,
  ActionType,
} from '../types';

// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`);
        return config;
      },
      (error) => {
        console.error('[API] Request error:', error);
        return Promise.reject(error);
      }
    );

    // Response interceptor
    this.client.interceptors.response.use(
      (response) => {
        console.log(`[API] Response:`, response.status, response.data);
        return response;
      },
      (error: AxiosError) => {
        console.error('[API] Response error:', error.response?.status, error.message);
        return Promise.reject(this.handleError(error));
      }
    );
  }

  private handleError(error: AxiosError): Error {
    if (error.response) {
      // Server responded with error status
      const message = (error.response.data as any)?.detail || error.message;
      return new Error(`API Error: ${message}`);
    } else if (error.request) {
      // Request made but no response
      return new Error('No response from server. Is the backend running?');
    } else {
      // Something else happened
      return new Error(`Request failed: ${error.message}`);
    }
  }

  // ============================================================================
  // Health Check
  // ============================================================================

  async healthCheck(): Promise<HealthResponse> {
    const response = await this.client.get<HealthResponse>('/health');
    return response.data;
  }

  // ============================================================================
  // Session Endpoints
  // ============================================================================

  async createSession(data: CreateSessionRequest): Promise<{ session_id: number }> {
    const response = await this.client.post('/api/sessions', data);
    return response.data;
  }

  async getSessions(limit: number = 15): Promise<Session[]> {
    const response = await this.client.get<SessionsResponse>('/api/sessions', {
      params: { limit },
    });
    return response.data.sessions;
  }

  async getSession(sessionId: number): Promise<Session> {
    const response = await this.client.get<SessionResponse>(`/api/sessions/${sessionId}`);
    return response.data.session;
  }

  async getSessionMessages(sessionId: number): Promise<Message[]> {
    const response = await this.client.get<MessagesResponse>(
      `/api/sessions/${sessionId}/messages`
    );
    return response.data.messages;
  }

  async addMessage(sessionId: number, data: AddMessageRequest): Promise<{ message_id: number }> {
    const response = await this.client.post(`/api/sessions/${sessionId}/messages`, data);
    return response.data;
  }

  // ============================================================================
  // Chat Endpoints
  // ============================================================================

  async chat(data: ChatRequest): Promise<string> {
    const response = await this.client.post<ChatResponse>('/api/chat', data);
    return response.data.response;
  }

  async performAction(action: ActionType, data: ActionRequest): Promise<string> {
    const response = await this.client.post<ActionResponse>(`/api/actions/${action}`, data);
    return response.data.response;
  }

  // ============================================================================
  // Settings Endpoints
  // ============================================================================

  async getSettings(): Promise<Settings> {
    const response = await this.client.get<SettingsResponse>('/api/settings');
    return response.data.settings;
  }

  async updateSettings(settings: Settings): Promise<void> {
    await this.client.put('/api/settings', settings);
  }
}

// Export singleton instance
export const api = new ApiClient();

// Export class for testing
export default ApiClient;

// Made with Bob
