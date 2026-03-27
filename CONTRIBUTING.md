# Contributing to Aegis-X 🛡️

First off, thank you for considering contributing to Aegis-X! It's people like you that make this a powerful tool for the community.

## 🛠️ Development Workflow
1. **Fork the Repo**: Create your own copy of the project.
2. **Create a Branch**: `git checkout -b feature/your-feature-name`
3. **Hardware Modules**: If adding a new tool (e.g., Proxmark3), place the logic in `backend/app/modules/`.
4. **API Endpoints**: Link your module to a new route in `backend/app/api/`.
5. **UI**: Add a new screen or component in `frontend/src/`.

## 📜 Coding Standards
* **Python**: Follow PEP 8. Document all hardware-specific functions.
* **JS/React**: Use functional components and hooks.
* **Security**: Never hardcode credentials. Use the `.env` file.

## 🚨 Responsible Disclosure
If you find a security vulnerability within Aegis-X itself, please open a private issue or contact the maintainers directly before making it public.
