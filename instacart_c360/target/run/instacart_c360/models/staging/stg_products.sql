
  create view "instacart"."staging_staging"."stg_products__dbt_tmp"
    
    
  as (
    select product_id,product_name,aisle_id,department_id from raw.products
  );