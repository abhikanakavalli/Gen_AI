
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy workspace root files
COPY pyproject.toml uv.lock ./

# Copy chatbot UI package
COPY app/chatbot-ui ./app/chatbot-ui

ENV UV_COMPILE_BYTECODE=1

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package chatbot-ui

ENV PYTHONOPTIMIZE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/app/.venv/bin:$PATH"

# Python package source path
ENV PYTHONPATH="/app/app/chatbot-ui/src:$PYTHONPATH"

# Create non-root user
RUN addgroup --system app && \
    adduser --system --ingroup app app && \
    chown -R app:app /app && \
    mkdir -p /home/app/.streamlit/data && \
    mkdir -p /home/app/.streamlit/cache && \
    chown -R app:app /home/app

ENV HOME=/home/app

USER app

EXPOSE 8501

# Set the correct working directory
WORKDIR /app/app/chatbot-ui/src

# Start Streamlit
CMD ["streamlit", "run", "chatbot_ui/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
