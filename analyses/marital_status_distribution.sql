-- analyses/marital_status_distribution.sql
-- Purpose: See what values exist in bronze.crm_cust_info
-- Helps decide if we need transformations

select
    upper(trim(cst_marital_status)) as marital_status_clean,
    count(*) as row_count
from {{ source('bronze','crm_cust_info') }}
group by 1
order by row_count desc;
