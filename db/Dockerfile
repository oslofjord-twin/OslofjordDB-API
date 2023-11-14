FROM postgis/postgis:16-3.4

# Set environment variables
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgrespassword

# Create a directory to hold scripts
RUN mkdir /scripts
COPY scripts/create_tables.sql /scripts/create_tables.sql
COPY scripts/load_data.sql /scripts/load_data.sql

# Run SQL scripts on startup
# COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d/
RUN echo "psql -d $POSTGRES_DB -U $POSTGRES_USER -f /scripts/create_tables.sql" >> docker-entrypoint-initdb.d/init-user-db.sh
RUN echo "psql -d $POSTGRES_DB -U $POSTGRES_USER -f /scripts/load_data.sql" >> docker-entrypoint-initdb.d/init-user-db.sh

# Expose port
EXPOSE 5432
