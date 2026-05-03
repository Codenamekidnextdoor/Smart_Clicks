/**
 * Main Window Component
 * The primary control interface for SmartClick
 */

import { useEffect, useState } from 'react';
import { useAppStore } from '../../stores/appStore';
import { useChatStore } from '../../stores/chatStore';
import { ControlPanel } from './ControlPanel';
import { SessionHistory } from './SessionHistory';
import { InfoCards } from './InfoCards';
import { StatusIndicator } from './StatusIndicator';
import { ChatBubble } from '../Popup/ChatBubble';
import { LoadingSpinner } from '../shared';
import type { ActionType, Session } from '../../types';

export function MainWindow() {
  const { enabled, loadSessions } = useAppStore();
  const { messages, isLoading, loadMessages, sendMessage } = useChatStore();
  const [activeSession, setActiveSession] = useState<Session | null>(null);
  const [chatInput, setChatInput] = useState('');

  useEffect(() => {
    loadSessions();
  }, [loadSessions]);

  const handleSessionClick = async (session: Session) => {
    setActiveSession(session);
    await loadMessages(session.id);
  };

  const handleSend = async () => {
    if (!chatInput.trim() || !activeSession) return;
    const msg = chatInput.trim();
    setChatInput('');
    await sendMessage(activeSession.id, msg, activeSession.selected_text);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="min-h-screen bg-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-6">
          <div className="flex items-center justify-between mb-2">
            <h1 className="text-3xl font-bold text-accent flex items-center gap-2">
              <span>✦</span>
              <span>Smart Click</span>
            </h1>
            <StatusIndicator enabled={enabled} />
          </div>
          <div className="h-px bg-border" />
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left Column - Controls & History */}
          <div className="lg:col-span-1 space-y-6">
            <ControlPanel />
            <SessionHistory onSessionClick={handleSessionClick} />
          </div>

          {/* Right Column */}
          <div className="lg:col-span-2">
            {activeSession ? (
              <div className="bg-bg-surface border border-border rounded-xl flex flex-col h-[600px]">
                {/* Session header */}
                <div className="flex items-center justify-between px-4 py-3 border-b border-border">
                  <div className="flex-1 min-w-0">
                    <p className="text-xs text-text-tertiary mb-0.5">Selected text</p>
                    <p className="text-sm text-text truncate italic">
                      "{activeSession.selected_text.substring(0, 80)}{activeSession.selected_text.length > 80 ? '…' : ''}"
                    </p>
                  </div>
                  <button
                    onClick={() => setActiveSession(null)}
                    className="ml-4 text-text-tertiary hover:text-text transition-colors text-lg leading-none"
                  >
                    ✕
                  </button>
                </div>

                {/* Messages */}
                <div className="flex-1 overflow-y-auto p-4 space-y-3">
                  {isLoading ? (
                    <div className="flex justify-center py-8"><LoadingSpinner /></div>
                  ) : messages.length === 0 ? (
                    <div className="flex items-center justify-center h-full text-text-tertiary text-sm">
                      No messages in this session yet.
                    </div>
                  ) : (
                    messages.map((msg) => (
                      <ChatBubble key={msg.id} message={msg} isStreaming={false} />
                    ))
                  )}
                </div>

                {/* Input */}
                <div className="p-3 border-t border-border flex gap-2">
                  <input
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Continue the conversation…"
                    className="
                      flex-1 bg-bg-surface2 border border-border rounded-lg
                      px-3 py-2 text-sm text-text placeholder-text-tertiary
                      focus:outline-none focus:border-accent
                    "
                  />
                  <button
                    onClick={handleSend}
                    disabled={!chatInput.trim() || isLoading}
                    className="px-4 py-2 bg-accent text-bg rounded-lg text-sm font-medium disabled:opacity-40 hover:bg-accent/90 transition-colors"
                  >
                    Send
                  </button>
                </div>
              </div>
            ) : (
              <InfoCards />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

// Made with Bob
