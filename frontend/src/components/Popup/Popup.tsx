/**
 * Popup Component
 * Floating window that appears near cursor when text is selected
 */

import { useState, useEffect } from 'react';
import { CompactView } from './CompactView';
import { ChatView } from './ChatView';
import { useAppStore } from '../../stores/appStore';
import { useChatStore } from '../../stores/chatStore';
import type { ActionType } from '../../types';

interface PopupProps {
  selectedText: string;
  position: { x: number; y: number };
  onClose: () => void;
  onAction: (action: ActionType, text: string) => void;
}

export function Popup({ selectedText, position, onClose, onAction }: PopupProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ mouseX: 0, mouseY: 0, winX: 0, winY: 0 });
  const { createSession } = useAppStore();
  const { clearMessages, performAction } = useChatStore();

  // Create a DB session whenever the popup opens with new text
  useEffect(() => {
    if (!selectedText) return;
    clearMessages();
    createSession(selectedText, position.x, position.y)
      .then((id) => setSessionId(id))
      .catch(() => setSessionId(null));
  }, [selectedText]);

  const handleMouseDown = async (e: React.MouseEvent) => {
    e.preventDefault();
    // Get the real OS window position from Electron before drag starts
    const pos = await window.electron?.getWindowPosition() ?? { x: 0, y: 0 };
    setIsDragging(true);
    setDragStart({ mouseX: e.screenX, mouseY: e.screenY, winX: pos.x, winY: pos.y });
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (!isDragging) return;
    const newX = dragStart.winX + (e.screenX - dragStart.mouseX);
    const newY = dragStart.winY + (e.screenY - dragStart.mouseY);
    window.electron?.moveWindow(newX, newY);
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  useEffect(() => {
    if (isDragging) {
      window.addEventListener('mousemove', handleMouseMove);
      window.addEventListener('mouseup', handleMouseUp);
      return () => {
        window.removeEventListener('mousemove', handleMouseMove);
        window.removeEventListener('mouseup', handleMouseUp);
      };
    }
  }, [isDragging, dragStart]);

  const handleAction = (action: ActionType) => {
    setIsExpanded(true);
    if (action !== 'chat' && sessionId !== null) {
      // Fire the quick action and show result in chat view
      performAction(sessionId, action, selectedText);
    }
    onAction(action, selectedText);
  };

  const handleCollapse = () => {
    setIsExpanded(false);
  };

  return (
    <div
      className="fixed z-50 animate-fade-in"
      style={{ left: 0, top: 0 }}
    >
      <div
        className="bg-bg-surface border border-border rounded-xl shadow-popup"
        style={{ opacity: 0.97 }}
      >
        {/* Drag Handle */}
        <div
          className="bg-bg-surface2 rounded-t-xl px-4 py-2 cursor-move flex items-center justify-between"
          onMouseDown={handleMouseDown}
        >
          <span className="text-accent text-sm font-bold">✦ Smart Click</span>
          <button
            onClick={onClose}
            className="text-text-tertiary hover:text-red transition-colors text-sm"
          >
            ✕
          </button>
        </div>

        {/* Content */}
        {isExpanded ? (
          <ChatView
            selectedText={selectedText}
            sessionId={sessionId}
            onCollapse={handleCollapse}
            onClose={onClose}
          />
        ) : (
          <CompactView selectedText={selectedText} onAction={handleAction} />
        )}
      </div>
    </div>
  );
}

// Made with Bob
