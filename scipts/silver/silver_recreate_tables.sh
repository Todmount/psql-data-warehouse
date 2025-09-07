#!/bin/bash

# Details

DB_USER="todmount"
DB_HOST="localhost"
DB_PORT="5432"

psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d datawarehouse << EOF
\i silver_recreate_tables.sql
EOF