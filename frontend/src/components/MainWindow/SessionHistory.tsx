/**
 * Session History Component
 * Displays recent sessions with ability to reopen them
 */

import { useAppStore } from '../../stores/appStore';
import { Card, LoadingSpinner } from '../shared';
import type { Session } from '../../types';

interface SessionHistoryProps {
  onSessionClick: (session: Session) => void;
}

export function SessionHistory({ onSessionClick }: SessionHistoryProps) {
  const { sessions, loading, loadSessions } = useAppStore();

  const formatTimeAgo = (timestamp: string): string => {
    try {
      // SQLite stores timestamps as UTC but without 'Z' suffix, so append it
      const date = new Date(timestamp.endsWith('Z') ? timestamp : timestamp + 'Z');
      const now = new Date();
      const seconds = Math.floor((now.getTime() - date.getTime()) / 1000);

      if (seconds < 60) return 'just now';
      if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
      if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
      return `${Math.floor(seconds / 86400)}d ago`;
    } catch {
      return '';
    }
  };

  return (
    <Card title="RECENT SESSIONS">
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs text-text-tertiary">Recent activity</span>
        <button
          onClick={() => loadSessions()}
          className="text-text-tertiary hover:text-text-secondary transition-colors"
          disabled={loading}
        >
          {loading ? <LoadingSpinner size="sm" /> : '↺'}
        </button>
      </div>

      <div className="space-y-2 max-h-96 overflow-y-auto">
        {loading && sessions.length === 0 ? (
          <div className="flex items-center justify-center py-8">
            <LoadingSpinner />
          </div>
        ) : sessions.length === 0 ? (
          <div className="text-center py-8 text-text-tertiary text-sm">
            <p>No sessions yet.</p>
            <p className="mt-1">Enable and select some text!</p>
          </div>
        ) : (
          sessions.map((session) => (
            <button
              key={session.id}
              onClick={() => onSessionClick(session)}
              className="
                w-full text-left p-3 rounded-lg
                bg-bg-surface2 hover:bg-bg-surface3
                border border-transparent hover:border-accent/40
                transition-all duration-200
                group
              "
            >
              <div className="text-sm text-text mb-1 line-clamp-2">
                "{session.selected_text.substring(0, 60)}
                {session.selected_text.length > 60 ? '…' : ''}"
              </div>
              <div className="flex items-center justify-between text-xs text-text-tertiary">
                <span>
                  {session.message_count} message{session.message_count !== 1 ? 's' : ''}
                </span>
                <span>{formatTimeAgo(session.updated_at)}</span>
              </div>
            </button>
          ))
        )}
      </div>
    </Card>
  );
}

// Made with Bob
