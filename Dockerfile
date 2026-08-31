# Multi-stage production Dockerfile for Enterprise Fintech Engine
FROM python:3.10-slim as backend-runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

EXPOSE 8000

CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]
