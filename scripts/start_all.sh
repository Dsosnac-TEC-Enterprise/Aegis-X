#!/bin/bash

echo "🛡️  Booting up Aegis-X Framework..."

# 1. Start the Python Backend in the background
echo "[+] Starting FastAPI Gateway on port 8000..."
cd backend
source venv/bin/activate
python app/main.py &
BACKEND_PID=$!
cd ..

# 2. Start the React Native Frontend
echo "[+] Starting React Native Terminal UI..."
cd frontend
npx expo start &
FRONTEND_PID=$!

echo ""
echo "🔥 Aegis-X is LIVE! 🔥"
echo "Press Ctrl+C to shut down all services safely."

# This trap ensures that when you press Ctrl+C, it kills both the frontend and backend
trap "echo 'Shutting down Aegis-X...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT TERM EXIT
wait
