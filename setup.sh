#!/bin/bash

echo "🛡️ Aegis-X: Initializing Security Framework..."

# 1. Install System Dependencies (Linux/Debian example)
echo "[+] Installing System Dependencies (SDR & MQTT)..."
sudo apt-get update
sudo apt-get install -y hackrf mosquitto mosquitto-clients python3-venv nodejs npm

# 2. Setup Python Backend
echo "[+] Setting up Python Virtual Environment..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# 3. Setup Frontend
echo "[+] Installing Node Modules for React Native..."
cd frontend
npm install
cd ..

echo "✅ Setup Complete!"
echo "To start the gateway: cd backend && source venv/bin/activate && python app/main.py"
echo "To start the UI: cd frontend && npx expo start"
