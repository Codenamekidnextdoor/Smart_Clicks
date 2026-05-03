/**
 * Info Cards Component
 * How-to guides for setup and usage
 */

import { Card } from '../shared';

export function InfoCards() {
  return (
    <div className="space-y-6">
      <Card title="How To Setup">
        <div className="space-y-3 text-text-secondary">
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">1.</span>
            <p className="text-sm">Press <span className="text-text font-semibold">Enable</span> in this window</p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">2.</span>
            <p className="text-sm">Allow changes if prompted</p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">3.</span>
            <p className="text-sm">You're all set!</p>
          </div>
        </div>
      </Card>

      <Card title="How To Use">
        <div className="space-y-3 text-text-secondary">
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">1.</span>
            <p className="text-sm">Highlight text in any application</p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">2.</span>
            <p className="text-sm">
              Press <span className="text-accent font-mono">Ctrl + Shift + Z</span>
            </p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-accent font-mono text-sm">3.</span>
            <p className="text-sm">Ask Smart Click anything you like</p>
          </div>
        </div>
      </Card>

      <Card title="Features">
        <div className="grid grid-cols-2 gap-4">
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-2xl">💬</span>
              <div>
                <div className="text-sm font-semibold text-text">Chat</div>
                <div className="text-xs text-text-tertiary">Ask anything</div>
              </div>
            </div>
          </div>
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-2xl">📝</span>
              <div>
                <div className="text-sm font-semibold text-text">Summarize</div>
                <div className="text-xs text-text-tertiary">Get summary</div>
              </div>
            </div>
          </div>
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-2xl">✏️</span>
              <div>
                <div className="text-sm font-semibold text-text">Rewrite</div>
                <div className="text-xs text-text-tertiary">Change tone</div>
              </div>
            </div>
          </div>
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-2xl">💡</span>
              <div>
                <div className="text-sm font-semibold text-text">Explain</div>
                <div className="text-xs text-text-tertiary">Clear explanation</div>
              </div>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}

// Made with Bob
