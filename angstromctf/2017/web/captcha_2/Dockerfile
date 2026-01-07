FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application code
COPY app/ /app/

# Install Python dependencies
RUN pip3 install flask flask-wtf wtforms pillow pycrypto

# Expose port 80
EXPOSE 80

# Set environment variables
ENV FLASK_APP=app.py
ENV PORT=80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:80/ || exit 1

# Run the application
CMD ["python3", "app.py"]

