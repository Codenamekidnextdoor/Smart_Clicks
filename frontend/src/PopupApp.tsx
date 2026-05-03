/**
 * PopupApp — rendered inside the dedicated floating popup BrowserWindow.
 * The window is transparent and always-on-top; this component fills it.
 */

import { useState, useEffect } from 'react';
import { Popup } from './components/Popup';
import type { ActionType } from './types';

export function PopupApp() {
  const [showPopup, setShowPopup] = useState(false);
  const [selectedText, setSelectedText] = useState('');

  // Make html/body transparent so only the popup card is visible
  useEffect(() => {
    document.documentElement.style.background = 'transparent';
    document.body.style.background = 'transparent';
    document.body.style.overflow = 'hidden';
  }, []);

  useEffect(() => {
    if (!window.electron) return;
    window.electron.onTextSelected((data) => {
      if (!data.text?.trim()) return;
      setSelectedText(data.text);
      setShowPopup(true);
    });
  }, []);

  const handleClose = () => {
    setShowPopup(false);
    window.electron?.closePopup?.();
  };

  const handleAction = (_action: ActionType, _text: string) => {
    // Actions are handled inside ChatView / CompactView
  };

  if (!showPopup) {
    // Transparent placeholder while waiting for text-selected event
    return <div style={{ background: 'transparent', width: '100vw', height: '100vh' }} />;
  }

  return (
    // Full-size transparent container; popup card positions itself at top-left
    <div style={{ background: 'transparent', width: '100vw', height: '100vh', overflow: 'visible' }}>
      <Popup
        selectedText={selectedText}
        position={{ x: 8, y: 8 }}
        onClose={handleClose}
        onAction={handleAction}
      />
    </div>
  );
}
