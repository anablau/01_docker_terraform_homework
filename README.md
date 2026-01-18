#!/bin/bash
# Homework 1: Docker, SQL and Terraform
# Data Engineering Zoomcamp 2026
# Due date: 27 January 2026

echo "---------------------------"
echo "Question 1: What's the version of pip in the python:3.13 image?"
echo "---------------------------"

# Pull and run python:3.13 image and check versions
docker run -it --rm --entrypoint bash python:3.13 -c "
python --version
pip --version
"

# Answer
echo "Answer 1: 25.3"
echo

echo "---------------------------"
echo "Question 2: Hostname and port pgAdmin should use to connect to Postgres"
echo "---------------------------"

echo "Explanation: Inside Docker Compose, use the service name 'db' and internal port 5432"
echo "Answer 2: db:5432"
echo

echo "---------------------------"
echo "Question 3: Number of trips in November 2025 with trip_distance <= 1 mile"
echo "---------------------------"

# SQL query to count trips
echo "SQL:"
echo \"\"\"
SELECT COUNT(1)
FROM green_tripdata_nov
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
\"\"\"

# Answer
echo "Answer 3: 8,007"
echo

echo "---------------------------"
echo "Question 4: Pickup day with longest trip distance (<100 miles)"
echo "---------------------------"

# SQL query to find longest trip day
echo "SQL:"
echo \"\"\"
SELECT 
    lpep_pickup_datetime::date AS pickup_day,
    MAX(trip_distance) AS max_trip_distance
FROM green_tripdata_nov
GROUP BY 1
HAVING MAX(trip_distance) <= 100
ORDER BY 2 DESC;
\"\"\"

# Answer
echo "Answer 4: 2025-11-14"
echo

echo "---------------------------"
echo "Question 5: Pickup zone with largest total_amount on 2025-11-18"
echo "---------------------------"

# SQL query
echo "SQL:"
echo \"\"\"
SELECT 
    b.\"Zone\" AS pickup_zone,
    SUM(total_amount) AS total_sum
FROM green_tripdata_nov a
LEFT JOIN zones b
    ON a.\"PULocationID\" = b.\"LocationID\"
WHERE lpep_pickup_datetime::date = '2025-11-18'
GROUP BY 1
ORDER BY 2 DESC;
\"\"\"

# Answer
echo "Answer 5: East Harlem North"
echo

echo "---------------------------"
echo "Question 6: For pickups in 'East Harlem North', drop-off zone with largest tip"
echo "---------------------------"

# SQL query
echo "SQL:"
echo \"\"\"
SELECT 
    c.\"Zone\" AS drop_off_zone,
    MAX(tip_amount) AS max_tip
FROM green_tripdata_nov a
LEFT JOIN zones b
    ON a.\"PULocationID\" = b.\"LocationID\"
LEFT JOIN zones c
    ON a.\"DOLocationID\" = c.\"LocationID\"
WHERE b.\"Zone\" = 'East Harlem North'
  AND lpep_pickup_datetime::date BETWEEN '2025-11-01' AND '2025-11-30'
GROUP BY 1
ORDER BY 2 DESC;
\"\"\"

# Answer
echo "Answer 6: Yorkville West"
echo

echo "---------------------------"
echo "Question 7: Terraform workflow"
echo "---------------------------"

echo "Correct sequence:"
echo "1) terraform init"
echo "2) terraform apply -auto-approve"
echo "3) terraform destroy"

echo "Answer 7: terraform init, terraform apply -auto-approve, terraform destroy"
echo

echo "---------------------------"
echo "Summary of Answers"
echo "---------------------------"
echo "1: 25.3"
echo "2: db:5432"
echo "3: 8,007"
echo "4: 2025-11-14"
echo "5: East Harlem North"
echo "6: Yorkville West"
echo "7: terraform init, terraform apply -auto-approve, terraform destroy"
