FROM php:8.1.5-apache-bullseye

# Install gcc for compiling C program
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Copy and compile the flag program
COPY printflag.c /tmp/printflag.c
RUN gcc -o /printflag /tmp/printflag.c && rm /tmp/printflag.c
RUN chmod 111 /printflag

# Copy web application files
COPY src /var/www/html

# Set proper permissions
RUN chown -R root:root /var/www/html && chmod -R 555 /var/www/html
RUN mkdir -p /var/www/html/abyss && \
    chown -R root:root /var/www/html/abyss && \
    chmod -R 333 /var/www/html/abyss

# Ensure tmp directory is writable for SQLite databases
RUN chmod 777 /tmp

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Set default environment variable
ENV FLAG="actf{default_flag_placeholder}"

EXPOSE 80
