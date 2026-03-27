import paho.mqtt.client as mqtt
import json

class MQTTGateway:
    """
    Manages IoT device communication via MQTT.
    Acts as the bridge between the mesh network and the Aegis-X API.
    """
    def __init__(self, broker="localhost", port=1883, topic="aegis_x/mesh/#"):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        self.latest_messages = [] # Buffer for UI updates

        # Assign callbacks
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"[+] Connected to MQTT Broker at {self.broker}")
            self.client.subscribe(self.topic)
        else:
            print(f"[-] MQTT Connection failed with code {rc}")

    def _on_message(self, client, userdata, msg):
        """Triggered when a mesh node sends data."""
        try:
            payload = json.loads(msg.payload.decode())
            print(f"[Mesh Data] Topic: {msg.topic} | Data: {payload}")
            # Keep only the last 20 messages for the terminal
            self.latest_messages.append({"topic": msg.topic, "data": payload})
            if len(self.latest_messages) > 20:
                self.latest_messages.pop(0)
        except Exception as e:
            print(f"[-] Failed to parse MQTT message: {e}")

    def start(self):
        """Starts the MQTT loop in a background thread."""
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"[-] Could not start MQTT Gateway: {e}")

    def publish_command(self, sub_topic, command_json):
        """Send a command out to the mesh network."""
        target_topic = f"aegis_x/commands/{sub_topic}"
        self.client.publish(target_topic, json.dumps(command_json))
        print(f"[+] Published to {target_topic}")

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

import time

class MQTTGateway:
    def __init__(self, broker="localhost"):
        # ... (previous init code)
        self.nodes = {} # Stores node_id: {status, last_seen, data}

    def _on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            node_id = msg.topic.split('/')[-1] # Assuming topic is aegis_x/mesh/NODE_ID
            
            # Update node registry
            self.nodes[node_id] = {
                "id": node_id,
                "last_seen": time.time(),
                "data": payload,
                "status": "online"
            }
        except Exception as e:
            print(f"Error: {e}")

