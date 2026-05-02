import React, { useState } from 'react';

function App() {
  const [selectedText, setSelectedText] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    if (!selectedText.trim()) {
      alert('Please enter some text!');
      return;
    }

    setLoading(true);
    setResult('');

    try {
      const summary = await window.electronAPI.summarizeText(selectedText);
      setResult(summary);
    } catch (error) {
      setResult(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleRewrite = async () => {
    if (!selectedText.trim()) {
      alert('Please enter some text!');
      return;
    }

    setLoading(true);
    setResult('');

    try {
      const rewritten = await window.electronAPI.rewriteText(selectedText, 'professional');
      setResult(rewritten);
    } catch (error) {
      setResult(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleExplain = async () => {
    if (!selectedText.trim()) {
      alert('Please enter some text!');
      return;
    }

    setLoading(true);
    setResult('');

    try {
      const explanation = await window.electronAPI.explainText(selectedText);
      setResult(explanation);
    } catch (error) {
      setResult(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>🤖 SmartClick</h1>
        <p className="subtitle">AI-Powered Text Assistant</p>

        <div className="input-section">
          <textarea
            value={selectedText}
            onChange={(e) => setSelectedText(e.target.value)}
            placeholder="Paste or type your text here..."
            rows={6}
          />
        </div>

        <div className="button-group">
          <button onClick={handleSummarize} disabled={loading}>
            ✨ Summarize
          </button>
          <button onClick={handleRewrite} disabled={loading}>
            ✍️ Rewrite
          </button>
          <button onClick={handleExplain} disabled={loading}>
            💡 Explain
          </button>
        </div>

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>AI is thinking...</p>
          </div>
        )}

        {result && !loading && (
          <div className="result">
            <h3>📝 Result:</h3>
            <p>{result}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

// Made with Bob
