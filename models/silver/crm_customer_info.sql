{{- config(schema='silver') -}}

with deduped as (
    select *,
           row_number() over (partition by cst_id order by cst_create_date desc) as flag_last
    from {{ source('bronze','crm_cust_info') }}
)

select
    cst_id as customer_id,
    cst_key as customer_key,
    trim(cst_firstname) as first_name,
    trim(cst_lastname) as last_name,

    case
        when upper(trim(cst_marital_status)) = 'M' then 'Married'
        when upper(trim(cst_marital_status)) = 'S' then 'Single'
        else 'n/a'
    end as marital_status,

    case
        when upper(trim(cst_gndr)) = 'F' then 'Female'
        when upper(trim(cst_gndr)) = 'M' then 'Male'
        else 'n/a'
    end as gender,

    cst_create_date as created_at,
    {{ current_timestamp() }} as dwh_load_date
from deduped
where flag_last = 1 and cst_id is not null
