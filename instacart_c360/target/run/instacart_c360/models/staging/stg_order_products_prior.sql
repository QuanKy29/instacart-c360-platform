
  create view "instacart"."staging_staging"."stg_order_products_prior__dbt_tmp"
    
    
  as (
    select order_id, product_id, add_to_cart_order, reordered from raw.order_products_prior
  );