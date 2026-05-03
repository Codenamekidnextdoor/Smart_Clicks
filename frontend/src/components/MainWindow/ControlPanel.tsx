/**
 * Control Panel Component
 * Enable/Disable controls and about button
 */

import { useState } from 'react';
import { useAppStore } from '../../stores/appStore';
import { Button } from '../shared';
import { Card } from '../shared';

export function ControlPanel() {
  const { enabled, enable, disable } = useAppStore();
  const [showAbout, setShowAbout] = useState(false);

  return (
    <Card title="CONTROLS">
      <div className="space-y-3">
        <Button
          variant="success"
          fullWidth
          onClick={enable}
          disabled={enabled}
          className="justify-start"
        >
          <span>▶</span>
          <span>Enable</span>
        </Button>

        <Button
          variant="danger"
          fullWidth
          onClick={disable}
          disabled={!enabled}
          className="justify-start"
        >
          <span>■</span>
          <span>Disable</span>
        </Button>

        <Button
          variant="secondary"
          fullWidth
          onClick={() => setShowAbout(true)}
          className="justify-start"
        >
          <span>?</span>
          <span>What is Smart Click</span>
        </Button>
      </div>

      {/* About Modal */}
      {showAbout && (
        <div
          className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4"
          onClick={() => setShowAbout(false)}
        >
          <div
            className="bg-bg-surface border border-border rounded-xl max-w-md w-full p-6 animate-fade-in"
            onClick={(e) => e.stopPropagation()}
          >
            <h2 className="text-xl font-bold text-accent mb-4">✦ What is Smart Click?</h2>
            <div className="h-px bg-accent/20 mb-4" />
            <div className="text-text-secondary text-sm space-y-3 mb-6">
              <p>
                Smart Click is an AI-powered cursor layer that watches for selected text anywhere on
                your screen.
              </p>
              <p>
                Highlight text, press <span className="text-accent font-mono">Ctrl + Shift + Z</span>,
                and a popup appears near your cursor offering:
              </p>
              <ul className="space-y-2 ml-4">
                <li>💬 <span className="text-text">Chat</span> - Ask anything about the text</li>
                <li>📝 <span className="text-text">Summarize</span> - Get a concise summary</li>
                <li>✏️ <span className="text-text">Rewrite</span> - Rewrite in a different tone</li>
                <li>💡 <span className="text-text">Explain</span> - Get a clear explanation</li>
              </ul>
              <p>All conversations are saved automatically.</p>
            </div>
            <Button variant="success" fullWidth onClick={() => setShowAbout(false)}>
              Got it
            </Button>
          </div>
        </div>
      )}
    </Card>
  );
}

// Made with Bob
