import datetime
import os

LOG_DIR = "app/logs"
LOG_FILE = f"{LOG_DIR}/session_log.txt"

class SessionLogger:
    """Handles persistent logging for Aegis-X sessions."""
    
    @staticmethod
    def initialize():
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                f.write(f"--- AEGIS-X SESSION INITIALIZED: {datetime.datetime.now()} ---\n")

    @staticmethod
    def log(entry_type, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] [{entry_type.upper()}] {message}\n")

    @staticmethod
    def get_log_content():
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                return f.read()
        return "No logs found."

import datetime
import os

LOG_DIR = "app/logs"
LOG_FILE = f"{LOG_DIR}/session_log.txt"

class SessionLogger:
    @staticmethod
    def initialize():
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                f.write("--- AEGIS-X AUDIT LOG INITIALIZED ---\n")

    @staticmethod
    def log(entry_type, message, lat=None, lon=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        geo_tag = f" @ [{lat}, {lon}]" if lat and lon else " @ [NO_GPS]"
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] [{entry_type.upper()}]{geo_tag} {message}\n")

