FROM nginx:1.25-alpine

# Install curl for healthcheck
RUN apk add --no-cache curl

EXPOSE 80

COPY ./ /usr/share/nginx/html/

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# Run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
