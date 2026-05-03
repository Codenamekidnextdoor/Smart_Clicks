/**
 * Compact View Component
 * Shows 4 action buttons in a grid
 */

import { Button } from '../shared';
import type { ActionType } from '../../types';

interface CompactViewProps {
  selectedText: string;
  onAction: (action: ActionType) => void;
}

const actions: Array<{ label: string; action: ActionType; emoji: string; color: string }> = [
  { label: 'Chat', action: 'chat', emoji: '💬', color: 'secondary' },
  { label: 'Summarize', action: 'summarize', emoji: '📝', color: 'success' },
  { label: 'Rewrite', action: 'rewrite', emoji: '✏️', color: 'primary' },
  { label: 'Explain', action: 'explain', emoji: '💡', color: 'secondary' },
];

export function CompactView({ selectedText, onAction }: CompactViewProps) {
  const preview = selectedText.length > 64 ? `${selectedText.substring(0, 64)}…` : selectedText;

  return (
    <div className="p-4 w-80">
      {/* Text Preview */}
      <div className="mb-4 p-3 bg-bg-surface2 rounded-lg">
        <p className="text-xs text-text-tertiary italic line-clamp-2">"{preview}"</p>
      </div>

      {/* Action Grid */}
      <div className="grid grid-cols-2 gap-2">
        {actions.map(({ label, action, emoji }) => (
          <button
            key={action}
            onClick={() => onAction(action)}
            className="
              p-3 rounded-lg
              bg-bg-surface2 hover:bg-bg-surface3
              border border-transparent hover:border-accent/30
              transition-all duration-200
              flex flex-col items-center gap-2
              group
            "
          >
            <span className="text-2xl group-hover:scale-110 transition-transform">{emoji}</span>
            <span className="text-sm font-medium text-text-secondary group-hover:text-text">
              {label}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}

// Made with Bob
