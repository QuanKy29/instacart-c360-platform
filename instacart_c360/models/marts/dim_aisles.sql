select
  aisle_id,
  aisle as aisle_name
from {{ ref('stg_aisles') }}
