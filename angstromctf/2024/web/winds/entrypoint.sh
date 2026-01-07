#!/bin/bash

# Substitute FLAG_PLACEHOLDER with actual flag if FLAG environment variable is provided
if [ -n "$FLAG" ]; then
    echo "$FLAG" > /app/flag.txt
fi

# Start the application
exec gunicorn -w8 -t5 --graceful-timeout 0 -b0.0.0.0:8000 app:app