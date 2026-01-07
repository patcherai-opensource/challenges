FROM buildkite/puppeteer
COPY deploy /ctf
WORKDIR /ctf
ENV FLAG placeholder_flag_value
ENV URL http://localhost:8080
ENV UBI http://localhost:5000
ENV ADMIN 2881c2705e0f05729949439b5619cc78
RUN npm install
USER 1000
EXPOSE 5001
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5001/ || exit 1
CMD ["node", "index.js"]
