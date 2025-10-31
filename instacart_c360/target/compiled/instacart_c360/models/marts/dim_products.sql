select
  p.product_id,
  p.product_name,
  p.aisle_id,
  p.department_id
from "instacart"."staging_staging"."stg_products" p
left join "instacart"."staging_staging"."stg_aisles" a
  on a.aisle_id = p.aisle_id
left join "instacart"."staging_staging"."stg_departments" d
  on d.department_id = p.department_id