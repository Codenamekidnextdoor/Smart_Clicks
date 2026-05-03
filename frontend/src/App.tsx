import { useEffect, useRef, useState } from 'react';
import { MainWindow } from './components/MainWindow';
import { Popup } from './components/Popup';
import { PopupApp } from './PopupApp';
import type { ActionType } from './types';

// Popup windows are opened with ?mode=popup so they render only the floating popup
const isPopupMode = new URLSearchParams(window.location.search).get('mode') === 'popup';

// Main SmartClick window (settings, sessions, etc.)
function MainApp() {
  const [showPopup, setShowPopup] = useState(false);
  const [popupPosition, setPopupPosition] = useState({ x: 0, y: 0 });
  const [selectedText, setSelectedText] = useState('');
  const selectedTextRef = useRef('');

  const handleAction = (action: ActionType, text: string) => {
    console.log(`Action: ${action}, Text: ${text.substring(0, 50)}...`);
  };

  useEffect(() => {
    if (!window.electron) {
      console.log('Running in browser mode');
      return;
    }
    console.log('Running in Electron mode (main window)');
    window.electron.onTextSelected((data) => {
      if (!data.text?.trim()) return;
      selectedTextRef.current = data.text;
      setSelectedText(data.text);
      setPopupPosition({ x: data.x, y: data.y });
      setShowPopup(true);
    });
  }, []);

  const handleClosePopup = () => {
    setShowPopup(false);
    setSelectedText('');
  };

  return (
    <>
      <MainWindow />
      {showPopup && (
        <Popup
          selectedText={selectedText}
          position={popupPosition}
          onClose={handleClosePopup}
          onAction={handleAction}
        />
      )}
    </>
  );
}

function App() {
  if (isPopupMode) return <PopupApp />;
  return <MainApp />;
}

export default App;
