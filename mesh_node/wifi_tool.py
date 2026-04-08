import network
import machine
import time
from umqtt.simple import MQTTClient
import json

# Configuration
WIFI_SSID = "Home_WiFi"
WIFI_PASS = "Password"
MQTT_BROKER = "127.0.0.1" # Aegis-X Backend IP
NODE_ID = "node_delta_01"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        pass
    print("Connected to WiFi")

def on_message(topic, msg):
    """Callback for when Aegis-X sends a command."""
    data = json.loads(msg)
    if data.get("action") == "wifi_scan":
        perform_scan()

def perform_scan():
    """Scans for nearby WiFi networks and reports back via MQTT."""
    wlan = network.WLAN(network.STA_IF)
    networks = wlan.scan() # [(ssid, bssid, channel, RSSI, auth, hidden), ...]
    
    results = []
    for n in networks:
        results.append({
            "ssid": n[0].decode('utf-8'),
            "rssi": n[3],
            "channel": n[2]
        })
    
    # Send results back to the Aegis-X Gateway
    client.publish(f"aegis_x/mesh/{NODE_ID}", json.dumps({"type": "wifi_report", "networks": results}))

# Main execution
connect_wifi()
client = MQTTClient(NODE_ID, MQTT_BROKER)
client.set_callback(on_message)
client.connect()
client.subscribe(f"aegis_x/commands/{NODE_ID}")

print(f"Node {NODE_ID} online and listening...")

while True:
    client.check_msg()
    time.sleep(1)
