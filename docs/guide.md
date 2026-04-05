# 📖 Aegis-X Operator's Manual

Welcome to the official field guide for **Aegis-X**. This document covers the core architecture, hardware integration, and the command-line interface (CLI) commands necessary to operate the framework. 

Whether you are capturing Sub-GHz signals, sweeping the 2.4GHz spectrum, or mapping IoT mesh networks, this guide will get your environment online.

---

## 🧠 1. How Aegis-X Works (The Architecture)

Aegis-X is not a single script; it is a **Three-Tier Security Framework**:

1. **The Frontend (Mobile UI):** A React Native application running on your phone. It acts as your remote control, terminal, and visualizer.
2. **The Backend (FastAPI Gateway):** A Python server running on your host machine (Laptop/Raspberry Pi). It translates mobile commands into raw hardware instructions.
3. **The Hardware:** The physical devices (Flipper Zero, HackRF One, ESP32) connected to the backend via USB or local WiFi.

---

## 🔌 2. Hardware Setup & Connecting Sensors

### A. Flipper Zero (Sub-GHz & IR)
* **Connection:** Plug the Flipper Zero directly into the host machine running the backend via USB-C.
* **Firmware:** Aegis-X is optimized for custom firmwares like *Unleashed* or *Xtreme* that allow advanced CLI execution.
* **Detection:** The backend will automatically scan your `tty` or `COM` ports to lock onto the Flipper's serial interface.

### B. HackRF One (SDR)
* **Connection:** Connect via USB.
* **Antenna:** Ensure you have the correct antenna attached for the frequency you are scanning (e.g., 2.4GHz for WiFi/Bluetooth sweeps).
* **Validation:** Before launching Aegis-X, run `hackrf_info` in your computer's terminal to ensure the OS recognizes the SDR.

### C. IoT Nodes & Sensors (ESP32/Raspberry Pi)
Aegis-X interacts with external sensors via **MQTT (Message Queuing Telemetry Transport)**.
* **How to Connect:** You do not plug sensors directly into Aegis-X. Instead, you flash your ESP32 with the provided `wifi_tool.py` script.
* **The Broker:** Ensure your ESP32 is on the same WiFi network as your Aegis-X backend and point the MQTT IP to your Gateway machine. 
* **Data Flow:** The sensor publishes data to the Gateway, and the Aegis-X mobile app visualizes it on the "Mesh Map."

---

## 💻 3. The Command-Line Interface (CLI)

The Aegis-X Mobile Terminal allows you to type raw commands directly to your hardware. Here are the core commands you need to know:

### 🛠️ System Commands
| Command | Description |
| :--- | :--- |
| `sys_status` | Pings all connected hardware (Flipper, SDR, MQTT) and returns their online/offline state. |
| `export_logs` | Packages your current session log (including GPS coordinates) and prompts a download/share menu. |
| `clear` | Wipes the terminal screen. |

### 🐬 Flipper Zero Commands
| Command | Description | Example |
| :--- | :--- | :--- |
| `flipper_tx <path>` | Transmits a `.sub` payload saved on the Flipper's SD card. | `flipper_tx /ext/subghz/gate.sub` |
| `flipper_rx <freq>` | Starts listening and recording on a specific frequency. | `flipper_rx 433.92` |
| `flipper_ls <dir>` | Lists the files in a specific directory on the Flipper. | `flipper_ls /ext/subghz` |

### 📻 SDR & Recon Commands
| Command | Description | Example |
| :--- | :--- | :--- |
| `sdr_sweep <start> <end>` | Runs a rapid frequency sweep between two megahertz values. | `sdr_sweep 2400 2500` |
| `mesh_scan <node_id>` | Commands a specific ESP32 node to scan for local WiFi networks. | `mesh_scan node_delta_01` |
| `mqtt_brute <ip>` | Launches a dictionary attack against a target MQTT broker. | `mqtt_brute 192.168.1.50` |

---

## 📱 4. Using the Mobile Interface

If you prefer tapping over typing, Aegis-X features a highly intuitive Cyberpunk UI.

* **Login:** The default security PIN is `1337`. 
* **Payload Library:** Save your most-used Flipper commands here. One tap equals one transmission.
* **SDR View:** A live, glowing-green line chart that visualizes the data captured by the `sdr_sweep` command.
* **Map History:** Every command executed in Aegis-X is GPS-tagged. Check this tab to see a physical map of where your captures and transmissions occurred.

---

### ⚠️ Disclaimer
**Aegis-X is built strictly for authorized security auditing, penetration testing, and educational research.** Do not use this framework to interact with infrastructure, hardware, or networks without explicit, written permission from the owner.
