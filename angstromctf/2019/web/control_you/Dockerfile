FROM nginx

# Copy the HTML template
COPY index.html /usr/share/nginx/html/index.html.template

# Create a startup script that substitutes the flag
RUN echo '#!/bin/bash' > /usr/local/bin/start.sh && \
    echo 'FLAG=${FLAG:-actf{placeholder_flag}}' >> /usr/local/bin/start.sh && \
    echo 'sed "s/FLAG_PLACEHOLDER/$FLAG/g" /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html' >> /usr/local/bin/start.sh && \
    echo 'exec nginx -g "daemon off;"' >> /usr/local/bin/start.sh && \
    chmod +x /usr/local/bin/start.sh

# Expose port 80
EXPOSE 80

# Use the startup script as the entrypoint
CMD ["/usr/local/bin/start.sh"]
