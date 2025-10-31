
  
    

  create  table "instacart"."staging_analytics"."dim_aisles__dbt_tmp"
  
  
    as
  
  (
    select
  aisle_id,
  aisle as aisle_name
from "instacart"."staging_staging"."stg_aisles"
  );
  