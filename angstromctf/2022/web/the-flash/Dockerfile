FROM nginx:mainline-alpine

# Copy the website files
COPY site /usr/share/nginx/html

# Add a health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# Expose port 80
EXPOSE 80

# Use nginx's default command which handles graceful shutdown
CMD ["nginx", "-g", "daemon off;"]
