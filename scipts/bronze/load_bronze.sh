#!/bin/bash
#===============================================================================
#Stored Procedure: Load Bronze Layer (Source -> Bronze)
#===============================================================================
#Script Purpose:
#    This stored procedure loads data into the 'bronze' schema from external CSV files.
#    It performs the following actions:
#    - Truncates the bronze tables before loading data.
#    - Uses the `\copy` command to load data from csv Files to bronze tables.
#
DB_USER="todmount"
DB_HOST="localhost"
DB_PORT="5432"


# Uncomment `\timing` if you need time info
psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d datawarehouse << EOF
-- \timing
BEGIN;
  \echo ====================
  \echo Loading Bronze Layer
  \echo ====================

  \echo ------------------
  \echo Loading CRM Tables
  \echo ------------------
  \echo >> Loading bronze.crm_cust_info
  TRUNCATE bronze.crm_cust_info;
  \copy bronze.crm_cust_info FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_crm/cust_info.csv' \
  delimiter ',' csv header;

  \echo >> Loading bronze.crm_prd_info
  TRUNCATE bronze.crm_prd_info;
  \copy bronze.crm_prd_info FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_crm/prd_info.csv' \
  delimiter ',' csv header;

  \echo >> Loading bronze.crm_sales_details
  TRUNCATE bronze.crm_sales_details;
  \copy bronze.crm_sales_details FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_crm/sales_details.csv' \
  delimiter ',' csv header;

  \echo ------------------
  \echo Loading ERP Tables
  \echo ------------------
  \echo >> Loading bronze.erp_cust_az12
  TRUNCATE bronze.erp_cust_az12;
  \copy bronze.erp_cust_az12 FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_erp/CUST_AZ12.csv' \
  delimiter ',' csv header;

  \echo >> Loading bronze.erp_loc_a101
  TRUNCATE bronze.erp_loc_a101;
  \copy bronze.erp_loc_a101 FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_erp/LOC_A101.csv' \
  delimiter ',' csv header;

  \echo >> Loading bronze.erp_px_cat_g1v2
  TRUNCATE bronze.erp_px_cat_g1v2;
  \copy bronze.erp_px_cat_g1v2 FROM '/home/todmount/Projects/simple-data-warehouse/datasets/source_erp/PX_CAT_G1V2.csv' \
  delimiter ',' csv header;
\echo >> Finished loading bronze level
COMMIT;

EOF