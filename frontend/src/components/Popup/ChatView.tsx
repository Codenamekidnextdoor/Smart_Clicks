/**
 * Chat View Component
 * Expanded chat interface with message history and input
 */

import { useState, useRef, useEffect } from 'react';
import { useChatStore } from '../../stores/chatStore';
import { ChatBubble } from './ChatBubble';
import { Button, LoadingDots } from '../shared';

interface ChatViewProps {
  selectedText: string;
  sessionId: number | null;
  onCollapse: () => void;
  onClose: () => void;
}

export function ChatView({ selectedText, sessionId, onCollapse, onClose }: ChatViewProps) {
  const { messages, isStreaming, isLoading, sendMessage } = useChatStore();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || isStreaming || isLoading) return;

    const message = input.trim();
    setInput('');

    await sendMessage(sessionId ?? 0, message, selectedText);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const preview = selectedText.length > 90 ? `${selectedText.substring(0, 90)}…` : selectedText;

  return (
    <div className="w-96 h-[500px] flex flex-col">
      {/* Context Bar */}
      <div className="px-4 py-3 bg-bg-surface3 border-b border-border">
        <div className="flex items-center justify-between mb-1">
          <span className="text-xs text-text-tertiary">Context:</span>
          <button
            onClick={onCollapse}
            className="text-text-tertiary hover:text-text-secondary text-xs"
          >
            ⊟ Collapse
          </button>
        </div>
        <p className="text-xs text-text-tertiary italic line-clamp-2">"{preview}"</p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {messages.length === 0 ? (
          <div className="flex items-center justify-center h-full text-text-tertiary text-sm">
            <p>Start a conversation...</p>
          </div>
        ) : (
          messages.map((message) => (
            <ChatBubble key={message.id} message={message} isStreaming={isStreaming} />
          ))
        )}
        {isLoading && (
          <div className="flex items-center gap-2 text-text-tertiary text-sm">
            <span>Bob is thinking</span>
            <LoadingDots />
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 border-t border-border bg-bg-surface2">
        <div className="flex gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask anything…"
            className="
              flex-1 px-3 py-2 rounded-lg
              bg-bg-surface3 border border-border
              text-text text-sm
              placeholder:text-text-tertiary
              focus:outline-none focus:border-accent
              resize-none
            "
            rows={2}
            disabled={isStreaming || isLoading}
          />
          <Button
            onClick={handleSend}
            disabled={!input.trim() || isStreaming || isLoading}
            variant="success"
            className="self-end"
          >
            {isStreaming || isLoading ? '...' : '↑'}
          </Button>
        </div>
      </div>
    </div>
  );
}

// Made with Bob
