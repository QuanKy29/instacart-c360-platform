
    
    

select
    aisle_id as unique_field,
    count(*) as n_records

from "instacart"."staging_staging"."stg_aisles"
where aisle_id is not null
group by aisle_id
having count(*) > 1


