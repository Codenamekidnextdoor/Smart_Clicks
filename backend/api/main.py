"""
SmartClick FastAPI Backend
Main application entry point that exposes Python functionality via REST API and WebSocket.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import Optional
import asyncio
import logging
import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from database.db_manager import DatabaseManager
from ai_integration.bob_client import WatsonxClient, MockWatsonxClient

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global instances
db: DatabaseManager = None
ai_client = None


# ============================================================================
# Request Models
# ============================================================================

class CreateSessionRequest(BaseModel):
    selected_text: str
    app_name: Optional[str] = None
    window_title: Optional[str] = None
    cursor_x: Optional[int] = None
    cursor_y: Optional[int] = None

class AddMessageRequest(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None
    session_id: Optional[int] = None

class ActionRequest(BaseModel):
    text: str
    session_id: Optional[int] = None

class SettingsRequest(BaseModel):
    watsonx_api_key: Optional[str] = None
    watsonx_project_id: Optional[str] = None
    watsonx_endpoint: Optional[str] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and cleanup resources"""
    global db, ai_client
    
    # Startup
    logger.info("Initializing SmartClick API...")
    db = DatabaseManager()

    # Seed credentials from environment variables (or defaults) if not already in DB.
    # Set WATSONX_API_KEY / WATSONX_PROJECT_ID / WATSONX_ENDPOINT env vars to override.
    _default_api_key    = os.environ.get('WATSONX_API_KEY',    'Gp3l8WFWhrBDuHQkv9lVLABbEXbQLJ0ZquW67oo4Yd8T')
    _default_project_id = os.environ.get('WATSONX_PROJECT_ID', '25be7a94-4de9-4add-ac4a-4eb52df5c6cf')
    _default_endpoint   = os.environ.get('WATSONX_ENDPOINT',   'https://us-south.ml.cloud.ibm.com')

    if not db.get_setting('watsonx_api_key'):
        db.set_setting('watsonx_api_key', _default_api_key)
    if not db.get_setting('watsonx_project_id'):
        db.set_setting('watsonx_project_id', _default_project_id)
    if not db.get_setting('watsonx_endpoint'):
        db.set_setting('watsonx_endpoint', _default_endpoint)

    # Initialize AI client
    api_key    = db.get_setting('watsonx_api_key')
    project_id = db.get_setting('watsonx_project_id')
    endpoint   = db.get_setting('watsonx_endpoint')
    
    if not all([api_key, project_id]):
        logger.warning("IBM watsonx credentials not configured. Using mock client.")
        ai_client = MockWatsonxClient()
    else:
        try:
            ai_client = WatsonxClient(
                api_key=api_key,
                project_id=project_id,
                endpoint=endpoint
            )
            logger.info("IBM watsonx client initialized")
        except Exception as e:
            logger.error(f"Failed to initialize watsonx client: {e}")
            ai_client = MockWatsonxClient()
    
    logger.info("SmartClick API ready")
    
    yield
    
    # Shutdown
    logger.info("Shutting down SmartClick API...")


# Create FastAPI app
app = FastAPI(
    title="SmartClick API",
    description="AI-powered cursor layer backend API",
    version="2.0.0",
    lifespan=lifespan
)

# CORS middleware - allow Electron app to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Health Check
# ============================================================================

@app.get("/")
async def root():
    """API health check"""
    return {
        "status": "ok",
        "service": "SmartClick API",
        "version": "2.0.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected" if db else "disconnected",
        "ai_client": "mock" if isinstance(ai_client, MockWatsonxClient) else "watsonx"
    }


# ============================================================================
# Session Endpoints
# ============================================================================

@app.post("/api/sessions")
async def create_session(req: CreateSessionRequest):
    """Create a new session"""
    try:
        cursor_pos = (req.cursor_x, req.cursor_y) if req.cursor_x is not None and req.cursor_y is not None else None
        session_id = db.create_session(
            selected_text=req.selected_text,
            app_name=req.app_name,
            window_title=req.window_title,
            cursor_pos=cursor_pos
        )
        return {"session_id": session_id, "status": "created"}
    except Exception as e:
        logger.error(f"Failed to create session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/sessions")
async def get_sessions(limit: int = 15):
    """Get recent sessions"""
    try:
        sessions = db.get_recent_sessions(limit=limit)
        return {"sessions": sessions}
    except Exception as e:
        logger.error(f"Failed to get sessions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/sessions/{session_id}")
async def get_session(session_id: int):
    """Get session details"""
    try:
        session = db.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        return {"session": session}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/sessions/{session_id}/messages")
async def get_session_messages(session_id: int):
    """Get all messages for a session"""
    try:
        messages = db.get_session_messages(session_id)
        return {"messages": messages}
    except Exception as e:
        logger.error(f"Failed to get messages: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/sessions/{session_id}/messages")
async def add_message(session_id: int, req: AddMessageRequest):
    """Add a message to a session"""
    try:
        if req.role not in ["user", "assistant"]:
            raise HTTPException(status_code=400, detail="Role must be 'user' or 'assistant'")
        message_id = db.add_message(
            session_id=session_id,
            role=req.role,
            content=req.content
        )
        return {"message_id": message_id, "status": "added"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to add message: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Chat Endpoints
# ============================================================================

@app.post("/api/chat")
async def chat(req: ChatRequest):
    """Send a chat message and get AI response"""
    try:
        history = []
        if req.session_id:
            messages = db.get_session_messages(req.session_id)
            history = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in messages
            ]
        response = await asyncio.to_thread(
            ai_client.chat, req.message, req.context, history
        )
        if req.session_id:
            db.add_message(req.session_id, "user", req.message)
            db.add_message(req.session_id, "assistant", response)
        return {"response": response, "status": "success"}
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/actions/{action}")
async def perform_action(action: str, req: ActionRequest):
    """Perform a quick action (summarize, rewrite, explain)"""
    try:
        if action not in ["summarize", "rewrite", "explain"]:
            raise HTTPException(status_code=400, detail="Invalid action")
        method = getattr(ai_client, action)
        response = await asyncio.to_thread(method, req.text)
        if req.session_id:
            db.add_message(req.session_id, "user", f"{action.capitalize()} this text")
            db.add_message(req.session_id, "assistant", response)
        return {"response": response, "action": action, "status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Action error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Settings Endpoints
# ============================================================================

@app.get("/api/settings")
async def get_settings():
    """Get all settings"""
    try:
        settings = {
            "watsonx_api_key": db.get_setting('watsonx_api_key'),
            "watsonx_project_id": db.get_setting('watsonx_project_id'),
            "watsonx_endpoint": db.get_setting('watsonx_endpoint'),
        }
        return {"settings": settings}
    except Exception as e:
        logger.error(f"Failed to get settings: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/settings")
async def update_settings(req: SettingsRequest):
    """Update settings"""
    try:
        data = req.model_dump(exclude_none=True)
        for key, value in data.items():
            db.set_setting(key, value)
        return {"status": "updated"}
    except Exception as e:
        logger.error(f"Failed to update settings: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# WebSocket for Real-time Chat
# ============================================================================

class ConnectionManager:
    """Manage WebSocket connections"""
    
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket connected. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"WebSocket disconnected. Total connections: {len(self.active_connections)}")
    
    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    """WebSocket endpoint for streaming chat responses"""
    await manager.connect(websocket)
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_json()
            
            message = data.get("message")
            context = data.get("context")
            session_id = data.get("session_id")
            
            if not message:
                await websocket.send_json({"error": "Message is required"})
                continue
            
            # Get conversation history
            history = []
            if session_id:
                messages = db.get_session_messages(session_id)
                history = [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in messages
                ]
            
            # Stream AI response
            try:
                await websocket.send_json({"type": "start"})

                # Run blocking AI call in thread pool to avoid blocking the event loop
                full_response = await asyncio.to_thread(
                    ai_client.chat, message, context, history
                )

                # Stream response word by word for a nice effect
                words = full_response.split()
                for word in words:
                    await websocket.send_json({"type": "chunk", "content": word + " "})
                    await asyncio.sleep(0.04)

                await websocket.send_json({"type": "end"})

                if session_id:
                    db.add_message(session_id, "user", message)
                    db.add_message(session_id, "assistant", full_response)
                
            except Exception as e:
                logger.error(f"Error streaming response: {e}")
                await websocket.send_json({
                    "type": "error",
                    "message": str(e)
                })
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket)


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


# ============================================================================
# Text Capture — called by Electron after it blurs its window
# ============================================================================

@app.post("/api/capture-text")
async def capture_text():
    """Simulate Ctrl+C on the currently focused window and return selected text."""
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent.parent))
        from backend.text_capture import get_selected_text
        text = await asyncio.get_event_loop().run_in_executor(None, get_selected_text)
        logger.info(f"capture-text: '{(text or '')[:60]}'")
        return {"text": text or ""}
    except Exception as e:
        logger.error(f"capture-text error: {e}")
        return {"text": ""}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

# Made with Bob
