#!/bin/bash
# Test if the server can start successfully

cd /Users/antheonaidoo/Smart_Clicks
source .venv/bin/activate

echo "Testing server startup..."
echo "Starting server (will auto-stop after 3 seconds)..."

# Start server in background
python3 backend/run.py &
SERVER_PID=$!

# Wait 3 seconds
sleep 3

# Check if server is still running
if ps -p $SERVER_PID > /dev/null; then
    echo "✓ Server started successfully!"
    echo "✓ Server is running on http://127.0.0.1:8000"
    echo "✓ Stopping test server..."
    kill $SERVER_PID
    exit 0
else
    echo "✗ Server failed to start"
    exit 1
fi

# Made with Bob
