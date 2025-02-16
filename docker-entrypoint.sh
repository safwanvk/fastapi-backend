#!/bin/sh
set -e  # Exit immediately if a command fails

# Apply database migrations
alembic upgrade head

# Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000
