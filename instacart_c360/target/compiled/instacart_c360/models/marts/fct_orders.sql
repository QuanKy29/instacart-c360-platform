-- Gộp 2 bảng chi tiết sản phẩm theo order (prior + train)
select
  o.order_id,
  o.user_id,
  op.product_id,
  op.add_to_cart_order,
  op.reordered,
  o.order_dow,
  o.order_hour_of_day,
  o.days_since_prior_order
from "instacart"."staging_staging"."stg_orders" o
join "instacart"."staging_staging"."stg_order_products_prior" op
  on op.order_id = o.order_id

union all

select
  o.order_id,
  o.user_id,
  op.product_id,
  op.add_to_cart_order,
  op.reordered,
  o.order_dow,
  o.order_hour_of_day,
  o.days_since_prior_order
from "instacart"."staging_staging"."stg_orders" o
join "instacart"."staging_staging"."stg_order_products_train" op
  on op.order_id = o.order_id