## 🛡️Aegis-X: The Ultimate Security & IoT Mesh Gateway

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![React Native](https://img.shields.io/badge/React_Native-Cross--Platform-61DAFB.svg)](https://reactnative.dev/)

**Aegis-X** is an open-source, modular gateway and terminal designed for security researchers and IT specialists. It bridges the gap between high-level mobile interfaces and low-level hardware like the **Flipper Zero**, **HackRF One**, and custom **MQTT-based IoT mesh networks**.

---

## 🚀 Key Features
* **Unified Hardware Terminal:** A single mobile interface to control multiple SDR and Serial devices.
* **IoT Mesh Mapping:** Real-time visualization of MQTT nodes in your network.
* **Sub-GHz Command Center:** Remote triggering of RF captures and replays via Flipper Zero.
* **SDR Integration:** Quick-action signal captures using HackRF One.
* **Modular Architecture:** Easily add new "attack modules" or hardware drivers.

## 🛠️ System Architecture
- **Frontend:** React Native (Mobile Terminal & Mesh Visualizer)
- **Backend:** FastAPI (Python Gateway)
- **Communications:** MQTT (IoT Mesh) & Serial (Hardware)

## 📦 Installation

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py
```
### 2. Frontend Setup
```bash
cd frontend
npm install
npx expo start
```
### 🛡️ Responsible Use
Aegis-X is built for educational and authorized security testing purposes ONLY. The creators are not responsible for misuse or damage caused by this software. Use your powers for good. ⚒️

*Copyright (c) 2026 David Sosnac, All rights reserved*
