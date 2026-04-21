from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import uvicorn

# Internal Modular Imports
from .api.routes import router as api_router
from .core.mesh import mesh_manager
from .modules.payload_manager import PayloadManager
from .modules.logger import SessionLogger

app = FastAPI(title="Aegis-X Secure Gateway")

# --- Security & Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Session Logger
SessionLogger.initialize()

# --- Static Dashboard Hosting ---
static_path = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_path):
    os.makedirs(static_path)

app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_path, "index.html"))

# --- Hardware & Core Routes ---
@app.post("/flipper/command")
def execute_flipper(command: str, lat: float = None, lon: float = None):
    # Log the action with geo-tags
    SessionLogger.log("FLIPPER", command, lat, lon)
    # Placeholder for serial communication logic
    return {"status": "success", "command": command, "output": "Payload Transmitted"}

@app.get("/system/logs")
def get_logs():
    return {"content": SessionLogger.get_log_content()}

@app.get("/system/map-history")
def get_map_history():
    # Your logic for parsing log files into geo-points
    return []

# --- Include Modular API (WebSockets & Mesh) ---
app.include_router(api_router, prefix="/api/v1")

# --- Secure Server Launch (Port 8443) ---
if __name__ == "__main__":
    # Ensure certs exist before running
    if os.path.exists("key.pem") and os.path.exists("cert.pem"):
        uvicorn.run(
            "main:app", 
            host="0.0.0.0", 
            port=8443, 
            ssl_keyfile="key.pem", 
            ssl_certfile="cert.pem",
            reload=True
        )
    else:
        print("[!] SSL Certificates missing. Run 'openssl' command first.")
        print("[*] Falling back to HTTP on port 8000 for local dev.")
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
