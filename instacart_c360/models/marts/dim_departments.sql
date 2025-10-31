select
  department_id,
  department as department_name
from {{ ref('stg_departments') }}
