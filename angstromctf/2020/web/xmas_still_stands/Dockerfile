FROM aplet123/puppeteer:node13

USER root
COPY . /ctf
WORKDIR /ctf

RUN npm install .

USER pptruser

EXPOSE 3000
ENV PORT 3000
ENV APP_HOST localhost
ENV CAPTCHA_SITE 6LfsiNsUAAAAANqwkmlw0xCemxE8eeb9j0vXju3p
ENV CAPTCHA_SECRET 6LfsiNsUAAAAAHexIOQu_OJugfE86YxpeD7Yxbol
# Use placeholder for flag that will be replaced at runtime
ENV FLAG PLACEHOLDER_FLAG
ENV CHROME_FLAGS --no-sandbox|--disable-setuid-sandbox

# Health check for container health monitoring
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

LABEL options='{"init": true}'

CMD ["npm", "start"]
