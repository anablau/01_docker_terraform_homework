Homework

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?
ANSWER : 25.3

SOLUTION
docker run -it --entrypoint bash python:3.13

python --version
pip --version

the version of pip in the python:3.13 Docker image you just pulled is 25.3.
So your container environment currently has:

Python: 3.13.11

pip: 25.3

----
Question 2. Understanding Docker networking and docker-compose

db:5432 — Correct (Uses service name + internal port)

postgres:5432 — Correct (Uses container name + internal port)

# Download the Green Taxi data
curl -L -O https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet

# Download the Zone Lookup table
curl -L -O https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

python3 ingest_homework_data.py


On the left sidebar, click the arrow next to Servers > Taxi-DB > Databases > ny_taxi.

Right-click on the ny_taxi database name.

Select Query Tool.
--ANSWER 8007
SELECT 
    COUNT(1) 
FROM 
    green_tripdata_nov
WHERE 
    lpep_pickup_datetime >= '2025-11-01' 
    AND lpep_pickup_datetime < '2025-12-01'
    AND trip_distance <= 1;

--ANSWER: 2025-11-14
	SELECT 
	lpep_pickup_datetime::date AS pickup_day,
	max(trip_distance) as max_trip_distance
	from green_tripdata_nov
	group by 1
	having max(trip_distance)<=100
		order by 2 desc;