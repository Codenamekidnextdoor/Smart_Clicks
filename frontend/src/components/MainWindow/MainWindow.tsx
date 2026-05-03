/**
 * Main Window Component
 * The primary control interface for SmartClick
 */

import { useEffect, useState } from 'react';
import { useAppStore } from '../../stores/appStore';
import { ControlPanel } from './ControlPanel';
import { SessionHistory } from './SessionHistory';
import { InfoCards } from './InfoCards';
import { StatusIndicator } from './StatusIndicator';
import { Popup } from '../Popup';
import type { ActionType } from '../../types';

export function MainWindow() {
  const { enabled, loadSessions } = useAppStore();
  const [showPopup, setShowPopup] = useState(false);
  const [popupPosition, setPopupPosition] = useState({ x: 400, y: 300 });

  useEffect(() => {
    // Load sessions on mount
    loadSessions();
  }, [loadSessions]);

  const handleAction = (action: ActionType, text: string) => {
    console.log('Action:', action, 'Text:', text);
    // TODO: Implement actual action handling
  };

  const handleTestPopup = () => {
    setPopupPosition({ x: window.innerWidth / 2 - 150, y: window.innerHeight / 2 - 150 });
    setShowPopup(true);
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
            <SessionHistory />
          </div>

          {/* Right Column - Info Cards */}
          <div className="lg:col-span-2">
            <InfoCards />
          </div>
        </div>

        {/* Test Popup Button */}
        <div className="mt-6 text-center">
          <button
            onClick={handleTestPopup}
            className="
              px-6 py-3 rounded-lg
              bg-accent/10 hover:bg-accent/20
              border border-accent
              text-accent font-medium
              transition-all duration-200
            "
          >
            🧪 Test Popup (Demo)
          </button>
        </div>
      </div>

      {/* Popup */}
      {showPopup && (
        <Popup
          selectedText="This is a sample text that was selected. You can ask questions about it, summarize it, rewrite it, or get an explanation!"
          position={popupPosition}
          onClose={() => setShowPopup(false)}
          onAction={handleAction}
        />
      )}
    </div>
  );
}

// Made with Bob
