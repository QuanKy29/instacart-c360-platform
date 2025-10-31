select
  p.product_id,
  p.product_name,
  p.aisle_id,
  p.department_id
from {{ ref('stg_products') }} p
left join {{ ref('stg_aisles') }} a
  on a.aisle_id = p.aisle_id
left join {{ ref('stg_departments') }} d
  on d.department_id = p.department_id
