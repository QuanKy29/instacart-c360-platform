
  
    

  create  table "instacart"."staging_analytics"."dim_departments__dbt_tmp"
  
  
    as
  
  (
    select
  department_id,
  department as department_name
from "instacart"."staging_staging"."stg_departments"
  );
  