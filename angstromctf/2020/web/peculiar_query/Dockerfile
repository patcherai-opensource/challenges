FROM aplet123/nodegres:node13-pg11

COPY . /ctf
WORKDIR /ctf

RUN npm install .

# Make init script executable
RUN chmod +x /ctf/init_db.sh

EXPOSE 3000
ENV PORT 3000
ENV DBNAME CriminalDB
ENV DBUSER readonly
ENV DBPASS readonlylmao
ENV DBPORT 5432
ENV DBHOST 127.0.0.1

# Health check for K8s
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:3000/ || exit 1

# Use the initialization script that supports flag injection
CMD ["/ctf/init_db.sh"]
