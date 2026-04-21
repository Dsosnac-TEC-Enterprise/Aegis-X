![Aegis-X](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=Aegis-X&fontSize=70&fontAlignY=40&desc=IoTMesh%20Gateway%20&descAlignY=60&descAlign=50)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![React Native](https://img.shields.io/badge/React_Native-Cross--Platform-61DAFB.svg)](https://reactnative.dev/)

**Aegis-X** is an open-source, modular gateway and terminal designed for security researchers and IT specialists. It bridges the gap between high-level mobile interfaces and low-level hardware like the **Flipper Zero**, **HackRF One**, and custom **MQTT-based IoT mesh networks**.

**Author:** David Sosnac 

---

## 🔑 Key Features
* **Unified Hardware Terminal:** A single mobile interface to control multiple SDR and Serial devices.
* **IoT Mesh Mapping:** Real-time visualization of MQTT nodes in your network.
* **Sub-GHz Command Center:** Remote triggering of RF captures and replays via Flipper Zero.
* **SDR Integration:** Quick-action signal captures using HackRF One.
* **Modular Architecture:** Easily add new "attack modules" or hardware drivers.

## 🛠️ System Architecture
- **Frontend:** React Native (Mobile Terminal & Mesh Visualizer)
- **Backend:** FastAPI (Python Gateway)
- **Communications:** MQTT (IoT Mesh) & Serial (Hardware)

## 🚀 Getting Started

Follow these steps to clone and deploy **Aegis-X** on your local machine.

### 1. Clone the Repository
Open your terminal and run the following command to clone the project from GitHub:

```bash
git clone https://github.com/Dsosnac-TEC-Enterprise/Aegis-X.git
cd Aegis-X
```

### 2. Run the Automated Setup
We have provided a unified setup script that installs all system dependencies, configures the Python virtual environment, and prepares the React Native frontend.

```bash
chmod +x setup.sh
./setup.sh
```
### 3. Launch the Framework
Use our custom start script to boot both the FastAPI Gateway and the Mobile Terminal simultaneously:

```bash
./scripts/start_all.sh
```
## 🧭Guidance 
For guidance kindly open our documentation folder (docs) and view guidance files for more clarity.

## 🛡️ Responsible Use
Aegis-X is built for educational and authorized security testing purposes ONLY. The creators are not responsible for misuse or damage caused by this software. Use your powers for good. ⚒️


