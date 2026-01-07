FROM python:3.9-slim

# Install any needed packages
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd -ms /bin/bash app

# Copy application code
COPY app /app
RUN chown -R app:app /app

# Switch to app user
USER app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Run the application
CMD ["python3", "leettube.py"]
