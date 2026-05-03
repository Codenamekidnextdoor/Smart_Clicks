/**
 * Chat Bubble Component
 * Displays individual messages in the chat
 */

import type { Message } from '../../types';

interface ChatBubbleProps {
  message: Message;
  isStreaming?: boolean;
}

export function ChatBubble({ message, isStreaming }: ChatBubbleProps) {
  const isUser = message.role === 'user';
  const isContext = message.role === 'context';

  if (isContext) {
    return (
      <div className="text-xs text-text-tertiary italic text-center py-2">
        {message.content}
      </div>
    );
  }

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`
          max-w-[80%] rounded-lg p-3
          ${
            isUser
              ? 'bg-blue-dark border border-blue text-text'
              : 'bg-bg-surface2 border border-border text-text'
          }
        `}
      >
        {/* Header */}
        <div className="flex items-center gap-2 mb-1">
          <span
            className={`text-xs font-bold ${isUser ? 'text-blue' : 'text-accent'}`}
          >
            {isUser ? 'You' : 'Bob ✦'}
          </span>
        </div>

        {/* Content */}
        <div className="text-sm whitespace-pre-wrap break-words">
          {message.content}
          {isStreaming && !isUser && (
            <span className="inline-block w-1 h-4 bg-accent ml-1 animate-pulse" />
          )}
        </div>
      </div>
    </div>
  );
}

// Made with Bob
