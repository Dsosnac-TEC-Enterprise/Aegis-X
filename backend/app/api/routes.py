from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..core.mesh import mesh_manager

router = APIRouter()

# --- REST ENDPOINTS ---
@router.get("/mesh/nodes")
async def list_nodes():
    return mesh_manager.get_active_nodes()

# --- WEBSOCKET FOR REAL-TIME DATA ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@router.websocket("/ws/signals")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Wait for data from hardware, then broadcast to UI
            data = await websocket.receive_text()
            # Logic to echo or process
    except WebSocketDisconnect:
        manager.disconnect(websocket)
