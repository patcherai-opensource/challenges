#!/bin/bash

# Start PostgreSQL
/etc/init.d/postgresql start

# Wait for PostgreSQL to be ready
until pg_isready -U postgres; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 2
done

# Create database user and database
su postgres -c "psql --command \"CREATE USER pgadmin WITH SUPERUSER PASSWORD 'noonecanhackthis'\""
su postgres -c "createdb -O pgadmin CriminalDB"

# Substitute flag placeholder with actual flag
PREPARED_SQL=$(cat /ctf/prepare_db.sql | sed "s/FLAG_PLACEHOLDER/${FLAG:-actf{qu3r7_s7r1ng5_4r3_0u7_70_g37_y0u}}/g")

# Initialize database with flag-injected SQL
echo "$PREPARED_SQL" | su postgres -c "psql CriminalDB"

echo "Database initialized successfully!"

# Start the Node.js application
exec npm start
