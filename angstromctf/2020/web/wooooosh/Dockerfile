FROM node:22

# Install curl for health check
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY app /ctf
WORKDIR /ctf
EXPOSE 3000
ENV PORT 3000
ENV FLAG={{FLAG_PLACEHOLDER}}

RUN npm install
CMD ["node", "index.js"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/ || exit 1
