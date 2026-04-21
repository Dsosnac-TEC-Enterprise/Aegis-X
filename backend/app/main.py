from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI(title="Aegis-X Secure Gateway")

# Enable CORS (Important for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 📂 STATIC FILE CONFIGURATION ---
static_path = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_path):
    os.makedirs(static_path)

# Mount the static folder for CSS/JS/Images
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_path, "index.html"))

# --- 🐬 HARDWARE ENDPOINTS (KEEP THESE!) ---
@app.post("/flipper/command")
def execute_flipper_cmd(command: str, lat: float = None, lon: float = None):
    # Your existing logic here...
    return {"status": "success", "output": f"Executed {command}"}

# ... (Keep all your other routes: /sdr/sweep, /system/map-history, etc.)

# --- 🚀 SECURE SERVER CONFIGURATION  ---
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8443, 
        ssl_keyfile="key.pem", 
        ssl_certfile="cert.pem",
        reload=True
    )
