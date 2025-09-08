#!/bin/bash
set -euo pipefail

# WARNING. Destructive script.
# Will purge all active connections on DB
# And then drop DB, create it and populate it with data


ENV_FILE="../../../.env" # hardcoded .env path
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


echo ">> STEP 1: Drop database and terminate all active users"
PGPASSWORD=$DB_SUPERPASSWORD psql -U "$DB_SUPERUSER" -h "$DB_HOST" -d postgres \
-v user="$DB_USER" \
-f sql/create_db.sql
echo ">> Finished STEP 1"


echo ">> STEP 2: Creating bronze, silver, and gold schemas"
PGPASSWORD=$DB_PASSWORD psql -U "$DB_USER" -h "$DB_HOST" -d datawarehouse \
-v user="$DB_USER" \
-f sql/create_schemas.sql \
-f sql/ddl_bronze.sql
echo ">> Finished STEP 2"


echo ">> STEP 3: Load data from CSV files"
#sh bronze_load_helper.sh
#or
PGPASSWORD=$DB_PASSWORD psql -U "$DB_USER" -h "$DB_HOST" -d datawarehouse -f sql/load_bronze.sql
echo ">> Finished STEP 3"
echo "Bronze level initiated!"