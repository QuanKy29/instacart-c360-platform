
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select aisle_id
from "instacart"."staging_staging"."stg_products"
where aisle_id is null



  
  
      
    ) dbt_internal_test