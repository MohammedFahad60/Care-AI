# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install the required ADK and Flask packages
RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run injects a $PORT environment variable. Gunicorn will listen on it.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 backend.app:app