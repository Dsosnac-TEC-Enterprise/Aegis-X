from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .modules.flipper import FlipperManager
from .modules.iot_mqtt import MQTTGateway

app = FastAPI(title="Aegis-X Gateway", version="1.0.0")

# --- Initialization ---
flipper = FlipperManager()
mqtt_net = MQTTGateway(broker="localhost") # Use your broker IP if not local

@app.on_event("startup")
async def startup_event():
    # Start the MQTT listener
    mqtt_net.start()
    # Attempt to connect to Flipper if plugged in
    flipper.connect()

# --- Models ---
class FlipperCmd(BaseModel):
    command: str

class MeshCmd(BaseModel):
    target_node: str
    action: str

# --- Endpoints ---

@app.get("/status")
def get_system_status():
    return {
        "flipper_connected": flipper.serial_conn is not None and flipper.serial_conn.is_open,
        "mqtt_status": "Listening",
        "mesh_messages_count": len(mqtt_net.latest_messages)
    }

@app.post("/flipper/exec")
def execute_flipper_command(cmd: FlipperCmd):
    """Send a CLI command to the Flipper Zero via the API."""
    result = flipper.send_command(cmd.command)
    if result is None:
        raise HTTPException(status_code=500, detail="Flipper not connected or command failed")
    return {"command": cmd.command, "output": result}

@app.get("/mesh/logs")
def get_mesh_logs():
    """Returns the latest traffic from the IoT mesh."""
    return {"logs": mqtt_net.latest_messages}

@app.post("/mesh/send")
def send_mesh_command(cmd: MeshCmd):
    """Sends a command to a specific IoT node via MQTT."""
    mqtt_net.publish_command(cmd.target_node, {"action": cmd.action})
    return {"status": "Command published"}

from .modules.hackrf import HackRFManager

sdr = HackRFManager()

@app.get("/sdr/info")
def get_sdr_info():
    return {"info": sdr.get_info()}

@app.post("/sdr/capture")
def start_sdr_capture(frequency: int):
    return {"status": sdr.start_rx(frequency)}

# Add to FastAPI main.py

@app.post("/flipper/replay")
def trigger_replay(filename: str):
    """
    Triggers a Sub-GHz replay from the Flipper's SD card.
    Example filename: '/ext/subghz/garage_door.sub'
    """
    if not flipper.serial_conn:
        raise HTTPException(status_code=500, detail="Flipper not connected")
        
    output = flipper.subghz_replay(filename)
    return {"status": "Replay triggered", "output": output}

