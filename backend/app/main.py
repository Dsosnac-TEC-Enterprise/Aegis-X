from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Aegis-X Gateway Terminal", version="1.0.0")

# Allow the React Native frontend to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Aegis-X Gateway is ONLINE 🔥"}

@app.get("/devices")
def get_connected_devices():
    # In the future, this will scan and return live hardware
    return {
        "devices": [
            {"id": "flipper_1", "type": "FlipperZero", "status": "disconnected"},
            {"id": "hackrf_1", "type": "HackRFOne", "status": "disconnected"},
            {"id": "iot_node_a", "type": "ESP32", "status": "connected"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
