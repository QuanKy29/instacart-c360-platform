
  create view "instacart"."staging_staging"."stg_departments__dbt_tmp"
    
    
  as (
    select department_id, department from raw.departments
  );