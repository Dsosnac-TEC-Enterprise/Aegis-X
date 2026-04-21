# 🛡️ Aegis-X Detailed Setup Guide

Welcome to the Aegis-X operations manual. This guide covers the physical hardware connection and advanced software configuration.

## 🔌 1. Hardware Requirements
To utilize the full capabilities of Aegis-X, you will need:
* **Host Machine:** Linux (Debian/Ubuntu/Kali) or macOS recommended for optimal SDR driver compatibility.
* **Flipper Zero:** Firmware with Sub-GHz capabilities (e.g., Unleashed or Xtreme).
* **HackRF One:** With an appropriate antenna for the 2.4GHz band if testing WiFi/Bluetooth frequencies.
* **IoT Nodes (Optional):** ESP32 or Raspberry Pi devices flashed with MQTT client scripts.

## ⚙️ 2. Hardware Connection & Verification

### Flipper Zero
1. Connect the Flipper to your host machine via USB-C.
2. Ensure it is turned on and on the main screen.
3. Aegis-X auto-detects the serial port. You can verify the connection in the mobile terminal by typing `info`.

### HackRF One
1. Connect via USB.
2. Verify the OS recognizes it by running `hackrf_info` in your native terminal. It should return the board ID and firmware version.

## 🚀 3. Running the Framework
Instead of launching the frontend and backend in separate terminal windows, use our unified launcher:
```bash
./scripts/start_all.sh
```

## 🏃4. Launching the Secure Beast

Now, when you run your backend, it will start on the secure port.

Start the server: `python main.py` (inside the backend/app folder).

Access the Dashboard: Open your browser to https://localhost:8443.

Confirm the Warning: Your browser will complain about the self-signed certificate—just click through it.