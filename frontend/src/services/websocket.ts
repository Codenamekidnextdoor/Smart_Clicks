/**
 * SmartClick WebSocket Client
 * Uses native WebSocket API to stream chat responses from the FastAPI backend.
 * (Replaces socket.io-client — FastAPI uses standard WS, not Socket.IO protocol)
 */

import type { WebSocketChatRequest, WebSocketMessage } from '../types';

const WS_URL = import.meta.env.VITE_WS_URL || 'ws://127.0.0.1:8000';

export class WebSocketClient {
  private ws: WebSocket | null = null;

  isConnected(): boolean {
    return this.ws !== null && this.ws.readyState === WebSocket.OPEN;
  }

  disconnect() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }

  reconnect() {
    this.disconnect();
  }

  /**
   * Open a fresh WebSocket connection per request, stream chunks, close when done.
   */
  async streamChat(
    request: WebSocketChatRequest,
    onChunk: (chunk: string) => void,
    onComplete: () => void,
    onError: (error: string) => void
  ): Promise<void> {
    return new Promise((resolve, reject) => {
      const ws = new WebSocket(`${WS_URL}/ws/chat`);
      let settled = false;

      const finish = (err?: string) => {
        if (settled) return;
        settled = true;
        ws.close();
        clearTimeout(timer);
        if (err) { onError(err); reject(new Error(err)); }
        else { onComplete(); resolve(); }
      };

      const timer = setTimeout(() => finish('Request timeout'), 30_000);

      ws.onopen = () => {
        console.log('[WebSocket] Connected, sending request');
        ws.send(JSON.stringify(request));
      };

      ws.onmessage = (event: MessageEvent) => {
        try {
          const data: WebSocketMessage = JSON.parse(event.data as string);
          if (data.type === 'chunk' && data.content) onChunk(data.content);
          else if (data.type === 'end') finish();
          else if (data.type === 'error') finish(data.message || 'Server error');
        } catch { /* ignore malformed frame */ }
      };

      ws.onerror = () => finish('WebSocket error — is the backend running on port 8000?');
      ws.onclose = (e) => { if (!settled) finish(e.wasClean ? undefined : 'Connection closed unexpectedly'); };
    });
  }
}

export const wsClient = new WebSocketClient();
export default WebSocketClient;

// Made with Bob
