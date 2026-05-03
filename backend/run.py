"""
SmartClick Backend Server
Run this to start the FastAPI backend server.
"""

import uvicorn
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

if __name__ == "__main__":
    print("=" * 60)
    print("SmartClick Backend API Server")
    print("=" * 60)
    print("Starting server on http://127.0.0.1:8000")
    print("API docs available at http://127.0.0.1:8000/docs")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    uvicorn.run(
        "api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

# Made with Bob
