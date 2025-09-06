/*
===============================================================================
Stored Procedure: Load Bronze Layer (Source -> Bronze)
===============================================================================
Script Purpose:
    This stored procedure loads data into the 'bronze' schema from external CSV files.
    It performs the following actions:
    - Truncates the bronze tables before loading data.
    - Uses the `COPY` command to load data from csv Files to bronze tables.

Parameters:
    None.
	  This stored procedure does not accept any parameters or return any values.

Usage Example:
    CALL bronze.load_bronze;

Note:
    The procedure will work only if files are stored on the server
    and the user has the role `pg_read_server_files`.
    In another case kindly use the `load_bronze.sh`
    that uses client-side behavior
If you want to see the time it takes, please read PostgreSQL documents on how to enable logging
===============================================================================
*/

CREATE OR REPLACE PROCEDURE bronze.load_bronze_layer()
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE '====================';
    RAISE NOTICE 'Loading Bronze Layer';
    RAISE NOTICE '====================';

    RAISE NOTICE '------------------';
    RAISE NOTICE 'Loading CRM Tables';
    RAISE NOTICE '------------------';

    RAISE NOTICE '>> Loading bronze.crm_cust_info';
    TRUNCATE bronze.crm_cust_info;
--     LOCK TABLE bronze.crm_cust_info IN SHARE MODE; -- redundant
    COPY bronze.crm_cust_info
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_crm/cust_info.csv'
    DELIMITER ',' CSV HEADER;

    RAISE NOTICE '>> Loading bronze.crm_prd_info';
    TRUNCATE bronze.crm_prd_info;
    COPY bronze.crm_prd_info
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_crm/prd_info.csv'
    DELIMITER ',' CSV HEADER;

    RAISE NOTICE '>> Loading bronze.crm_sales_details';
    TRUNCATE bronze.crm_sales_details;
    COPY bronze.crm_sales_details
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_crm/sales_details.csv'
    DELIMITER ',' CSV HEADER;

    RAISE NOTICE '------------------';
    RAISE NOTICE 'Loading ERP Tables';
    RAISE NOTICE '------------------';

    RAISE NOTICE '>> Loading bronze.erp_cust_az12';
    TRUNCATE bronze.erp_cust_az12;
    COPY bronze.erp_cust_az12
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_erp/CUST_AZ12.csv'
    DELIMITER ',' CSV HEADER;

    RAISE NOTICE '>> Loading bronze.erp_loc_a101';
    TRUNCATE bronze.erp_loc_a101;
    COPY bronze.erp_loc_a101
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_erp/LOC_A101.csv'
    DELIMITER ',' CSV HEADER;

    RAISE NOTICE '>> Loading bronze.erp_px_cat_g1v2';
    TRUNCATE bronze.erp_px_cat_g1v2;
    COPY bronze.erp_px_cat_g1v2
    FROM '/var/lib/postgresql/projects/psql_data_warehouse/datasets/source_erp/PX_CAT_G1V2.csv'
    DELIMITER ',' CSV HEADER;
END;
$$;
