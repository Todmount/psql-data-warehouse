#!/bin/bash

# WARNING. Destructive script.
# Will purge all active connections on DB
# And then drop DB and create it

DB_USER="todmount"
DB_SUPERUSER="postgres"
DB_HOST="localhost"
DB_PORT="5432"

echo "WARNING: This will drop and recreate the 'datawarehouse' DB. Continue? (Ctrl+C to cancel)"
for i in 3 2 1
do
  echo "$i..."
  sleep 1
done

# Step 1: drop & recreate DB
psql -U "$DB_SUPERUSER" -h "$DB_HOST" -p "$DB_PORT" -d postgres \
-v user="$DB_USER" \
-f create_db.sql

# Step 2: create schemas inside DB
psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d datawarehouse \
-v user="$DB_USER" \
-f create_schemas.sql
