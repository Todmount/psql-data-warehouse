/*
=============================================================
Create Schemas
=============================================================
Simple script to create schemas according to medallion model.
It's for use with `create_bronze.sh`
*/
CREATE SCHEMA IF NOT EXISTS bronze AUTHORIZATION :"user";
CREATE SCHEMA IF NOT EXISTS silver AUTHORIZATION :"user";
CREATE SCHEMA IF NOT EXISTS gold AUTHORIZATION :"user";