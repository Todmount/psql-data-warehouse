/*
=============================================================
Create Schemas
=============================================================
Simple script to create schemas according to medallion model.
It's for use with `create_bronze.sh`
*/
CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;