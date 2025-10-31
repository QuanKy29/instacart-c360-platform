
  
    

  create  table "instacart"."staging_analytics"."dim_customers__dbt_tmp"
  
  
    as
  
  (
    select distinct
  user_id
from "instacart"."staging_staging"."stg_orders"
  );
  