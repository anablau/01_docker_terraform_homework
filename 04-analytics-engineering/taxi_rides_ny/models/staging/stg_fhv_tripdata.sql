{{ config(materialized='view') }}

with tripdata as 
(
  select *
  from {{ source('raw', 'fhv_tripdata') }}
  -- Requirement: Filter out records where dispatching_base_num IS NULL
  where dispatching_base_num is not null
)
select
    -- identifiers
    dispatching_base_num,
    cast(pulocationid as integer) as pickup_location_id,
    cast(dolocationid as integer) as dropoff_location_id,

    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    
    -- additional info
    sr_flag
from tripdata