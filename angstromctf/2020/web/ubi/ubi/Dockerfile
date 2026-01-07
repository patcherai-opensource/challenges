FROM python:3
COPY deploy /app
WORKDIR /app
RUN pip install --no-cache-dir flask gunicorn pycryptodome
RUN curl https://raw.githubusercontent.com/pshved/timeout/master/timeout > /usr/local/bin/timeout && chmod 755 /usr/local/bin/timeout
RUN apt-get update && apt-get install -y gcc curl && rm -rf /var/lib/apt/lists/*
RUN chown -R 1000 /app
USER 1000
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
