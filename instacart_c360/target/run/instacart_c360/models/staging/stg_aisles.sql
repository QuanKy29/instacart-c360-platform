
  create view "instacart"."staging_staging"."stg_aisles__dbt_tmp"
    
    
  as (
    select aisle_id, aisle from raw.aisles
  );