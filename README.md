# Gen_AI

A GenAI workspace/project containing an API service, a Streamlit chatbot UI, and notebooks for experimentation.

## Repository structure

- `app/api/` — Backend API service (FastAPI/Uvicorn, workspace member)
- `app/chatbot-ui/` — Streamlit-based chatbot UI (workspace member)
- `notebooks/` — Jupyter notebooks for prerequisites and experimentation
- `docker-compose.yml` — Local multi-service setup (API + Streamlit UI)
- `pyproject.toml` — Project metadata, dependencies, and `uv` workspace configuration
- `env.example` — Example environment variables template
- `.env` — Local environment variables (not committed; ignored by git)

## Prerequisites

- Python **>= 3.12**
- [uv](https://github.com/astral-sh/uv) for dependency/environment management
- Docker & Docker Compose (optional, for containerized runs)
- API keys/credentials for the LLM providers you plan to use (e.g. OpenAI, Google GenAI, Groq), as configured in your environment

## Development environment setup

1. **Install Python 3.12+ and uv**
2. **Initialize/sync the environment** (from the project root):
   ```bash
   uv sync
   ```
   If you are setting up from scratch, you can also initialize with:
   ```bash
   uv init --python=3.12
   uv add ipykernel
   ```
3. **Configure environment variables**
   - Copy `env.example` to `.env` (if applicable) and fill in required values:
     ```bash
     cp env.example .env
     ```
   - On Windows PowerShell:
     ```powershell
     Copy-Item env.example .env
     ```
   - Update `.env` with the necessary API keys/settings.

## Running the project

### Using Docker Compose
From the project root:
```bash
docker compose up --build
```
Services (as defined in `docker-compose.yml`):
- **API**: http://localhost:8000
- **Streamlit UI**: http://localhost:8501

Source directories are mounted into containers for local development, and services load variables from `.env`.

### Running locally (without Docker)
Use `uv` to run services in your environment. Examples:
```bash
# API (from project root)
uv run uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload

# Streamlit UI (adjust path/module as needed)
uv run streamlit run app/chatbot-ui/src/<your_app_entry>.py
```
> Note: Exact local run commands may vary depending on the app entrypoints inside `app/api/src` and `app/chatbot-ui/src`.

## Notebooks

- Notebooks live under `notebooks/` (e.g. `notebooks/prerequisites/`).
- To work with notebooks, ensure `ipykernel` is installed (included in dependencies) and select the appropriate Python environment/kernel in your editor.

## Workspace & dependencies

This repo uses a `uv` workspace with members:
- `app/api`
- `app/chatbot-ui`

Core dependencies include libraries such as `openai`, `google-genai`, `groq`, `streamlit`, `pydantic`, and `python-dotenv` (see `pyproject.toml` for the full list).

## Notes

- Do not commit secrets: `.env` is ignored by `.gitignore`.
- `uv.lock` and `.venv/` are also ignored in this repository configuration.