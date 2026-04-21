import time

class MeshController:
    """Manages the lifecycle and state of ESP32/IoT nodes."""
    
    def __init__(self):
        self.nodes = {} # Stores node_id: {last_seen, status, capabilities}

    def register_node(self, node_id, capabilities):
        self.nodes[node_id] = {
            "status": "ONLINE",
            "last_seen": time.time(),
            "capabilities": capabilities
        }
        print(f"[MESH] Node {node_id} registered.")

    def get_active_nodes(self):
        # Filter nodes that haven't checked in for 60 seconds
        current_time = time.time()
        return {nid: n for nid, n in self.nodes.items() if current_time - n['last_seen'] < 60}

    def process_node_data(self, node_id, payload):
        if node_id in self.nodes:
            self.nodes[node_id]["last_seen"] = time.time()
            # Logic to handle incoming sensor/recon data
            return True
        return False

# Global instance for the app
mesh_manager = MeshController()
