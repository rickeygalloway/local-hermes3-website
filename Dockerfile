# Use official Python runtime as the base image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install system dependencies (curl for Ollama installation)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir flask requests

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the hermes3:8b model (this runs during build)
RUN ollama pull hermes3:8b

# Expose ports (5000 for Flask, 11434 for Ollama)
EXPOSE 5000 11434

# Command to run Ollama in the background and then start Flask
CMD ["sh", "-c", "ollama serve & sleep 5 && python app.py"]