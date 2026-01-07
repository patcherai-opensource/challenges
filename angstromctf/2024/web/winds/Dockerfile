FROM python:3.12-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py entrypoint.sh ./
# Create flag.txt with placeholder that can be substituted at runtime
RUN echo "FLAG_PLACEHOLDER" > flag.txt
RUN chmod +x entrypoint.sh
USER nobody
EXPOSE 8000
CMD ["./entrypoint.sh"]
