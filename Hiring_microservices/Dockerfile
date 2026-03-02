FROM python:3.8-slim

WORKDIR /app

# Install system dependencies for psycopg2 and other tools
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This ARG will be overridden by docker-compose for each service
ARG SERVICE_DIR
COPY ./${SERVICE_DIR}/ /app/

# Port will be passed as environment variable or mapped in compose
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}