FROM php:7.0-apache

# Set environment variable for flag
ENV FLAG="actf{placeholder_flag}"

# Install curl for health check
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY app /var/www/html/

# Create a startup script that injects the flag
RUN echo '#!/bin/bash' > /usr/local/bin/start.sh && \
    echo 'sed -i "s/{{FLAG}}/$FLAG/g" /var/www/html/stories/restricted/9cd6ef9734ae48d1bbdf0a65511e4700/4f4c5884242396af6a1d3951a11688b9.story' >> /usr/local/bin/start.sh && \
    echo 'apache2-foreground' >> /usr/local/bin/start.sh && \
    chmod +x /usr/local/bin/start.sh

# Set proper permissions
RUN chown -R www-data:www-data /var/www/html

# Expose port 80
EXPOSE 80

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Use custom startup script
CMD ["/usr/local/bin/start.sh"]
