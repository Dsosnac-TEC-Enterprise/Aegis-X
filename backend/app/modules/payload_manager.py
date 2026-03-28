import json
import os

PAYLOADS_FILE = "app/data/payloads.json"

class PayloadManager:
    """Manages the library of saved RF and IoT payloads."""
    
    @staticmethod
    def get_all():
        if not os.path.exists(PAYLOADS_FILE):
            return []
        with open(PAYLOADS_FILE, 'r') as f:
            return json.load(f)

    @staticmethod
    def add_payload(name, p_type, frequency, file_path):
        payloads = PayloadManager.get_all()
        new_entry = {
            "id": len(payloads) + 1,
            "name": name,
            "type": p_type,
            "frequency": frequency,
            "file_path": file_path
        }
        payloads.append(new_entry)
        with open(PAYLOADS_FILE, 'w') as f:
            json.dump(payloads, f, indent=4)
        return new_entry
