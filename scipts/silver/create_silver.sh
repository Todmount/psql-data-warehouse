#!/bin/bash

# WARNING: Destructive script.
# Will drop and recreate all tables on silver schema
# Then transform (clean) and insert data into them

ENV_FILE="../../.env" # hardcoded .env path
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
else
    echo ".env file not found at $ENV_FILE"
    exit 1
fi


echo "WARNING: This will drop and recreate the 'datawarehouse' DB. Continue? (Ctrl+C to cancel)"
for i in 3 2 1
do
  echo "$i..."
  sleep 1
done


PGPASSWORD=$DB_PASSWORD psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d datawarehouse << EOF
\echo ">> STEP 1. Dropping tables and recreating..."
\i ddl_silver.sql
\echo ">> Finish STEP 1"
\echo "-------------------------------------------------"
\echo ">> STEP 2. Transforming and inserting the data..."
\i silver_etl.sql
\echo ">> Finish STEP 2"
EOF