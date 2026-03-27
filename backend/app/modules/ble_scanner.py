import asyncio
from bleak import BleakScanner

class BLEManager:
    """
    Handles Bluetooth Low Energy reconnaissance.
    """
    def __init__(self):
        self.discovered_devices = []

    async def scan(self, duration=5):
        """
        Scans for nearby BLE devices and returns their metadata.
        """
        print(f"[*] Starting BLE scan for {duration}s...")
        devices = await BleakScanner.discover(timeout=duration)
        
        results = []
        for d in devices:
            results.append({
                "name": d.name if d.name else "Unknown",
                "address": d.address,
                "rssi": d.rssi,
                "metadata": d.metadata
            })
        
        self.discovered_devices = results
        return results

# API Bridge in main.py
# @app.get("/ble/scan")
# async def trigger_ble_scan():
#     ble = BLEManager()
#     return await ble.scan()
