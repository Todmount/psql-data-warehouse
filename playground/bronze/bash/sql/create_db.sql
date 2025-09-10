/*
=============================================================
Create Database
=============================================================
Script Purpose:
    This script creates a new database named 'DataWarehouse' after checking if it already exists.
    If the database exists, it is dropped and recreated. Additionally, the script sets up three schemas
    within the database: 'bronze', 'silver', and 'gold'.

WARNING:
    Running this script will drop the entire 'DataWarehouse' database if it exists.
    All data in the database will be permanently deleted. Proceed with caution
    and ensure you have proper backups before running this script.
*/

-- Terminate connections to the target DB (except yourself)
ROLLBACK;
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'datawarehouse'
  AND pid <> pg_backend_pid();


-- Drop the database if it exists
DROP DATABASE IF EXISTS datawarehouse;


-- Create the new database
CREATE DATABASE datawarehouse
    WITH OWNER = :"user"
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;