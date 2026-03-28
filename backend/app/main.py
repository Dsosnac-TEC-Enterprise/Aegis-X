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

@app.get("/sdr/sweep")
def hackrf_spectral_sweep(start: int = 2400, end: int = 2500):
    """Triggers a 100MHz sweep on the HackRF."""
    return sdr.start_sweep(start_mhz=start, end_mhz=end)

@app.post("/mesh/wifi-scan")
def trigger_node_wifi_scan(node_id: str):
    """Tells a specific ESP32 node to perform a WiFi reconnaissance scan."""
    mqtt_net.publish_command(node_id, {"action": "wifi_scan"})
    return {"status": f"Scan command sent to {node_id}"}

from .modules.mqtt_brute import MQTTBruter

@app.post("/mesh/brute-force")
def start_mqtt_brute(target_ip: str):
    bruter = MQTTBruter(target_ip)
    # Simple example wordlist; in production, you'd load a file
    users = ["admin", "root", "user"]
    pwds = ["1234", "password", "admin", "mosquitto"]
    
    result = bruter.run_wordlist(users, pwds)
    if result:
        return {"status": "Compromised", "credentials": result}
    return {"status": "Secure", "message": "Wordlist exhausted"}

from .modules.payload_manager import PayloadManager

@app.get("/payloads")
def list_payloads():
    return PayloadManager.get_all()

@app.post("/payloads/launch/{payload_id}")
def launch_payload(payload_id: int):
    """Finds a payload by ID and tells the Flipper to transmit it."""
    payloads = PayloadManager.get_all()
    target = next((p for p in payloads if p["id"] == payload_id), None)
    
    if not target:
        raise HTTPException(status_code=404, detail="Payload not found")
        
    # Reuse our Flipper logic from before
    output = flipper.subghz_replay(target["file_path"])
    return {"status": f"Launched {target['name']}", "flipper_output": output}

from .modules.logger import SessionLogger

# Initialize logger on startup
SessionLogger.initialize()

@app.get("/system/logs")
def export_logs():
    """Returns the full session log as a string."""
    content = SessionLogger.get_log_content()
    return {"filename": "aegis_x_log.txt", "content": content}





