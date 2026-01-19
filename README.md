#!/bin/bash
# ============================================================
# Homework 1: Docker, SQL and Terraform
# Data Engineering Zoomcamp 2026
# Due date: 27 January 2026
# ============================================================

echo "============================================================"
echo "Homework 1: Docker, SQL and Terraform"
echo "Data Engineering Zoomcamp 2026"
echo "Due date: 27 January 2026"
echo "============================================================"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 1: What's the version of pip in the python:3.13 image?"
echo "============================================================"

# Pull and run the python:3.13 image and check Python and pip versions
echo "Running docker command to check versions..."
docker run -it --rm --entrypoint bash python:3.13 -c "
python --version
pip --version
"

echo
echo "Explanation:"
echo "The official python:3.13 image comes with pip version 25.3 preinstalled."
echo
echo "Answer 1: pip version 25.3"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 2: Hostname and port pgAdmin should use to connect to Postgres"
echo "============================================================"

echo "Explanation:"
echo "Inside a Docker Compose network, containers communicate via service names."
echo "If the database service is named 'db' and uses the default Postgres port 5432,"
echo "pgAdmin should connect using hostname 'db' and port '5432'."
echo
echo "Answer 2: db:5432"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 3: Number of trips in November 2025 with trip_distance <= 1 mile"
echo "============================================================"

echo "SQL Query:"
cat <<'SQL'
SELECT COUNT(1)
FROM green_tripdata_nov
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
SQL

echo
echo "Explanation:"
echo "This query counts the number of trips where trip_distance is less than or equal to 1 mile during November 2025."
echo
echo "Answer 3: 8,007"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 4: Pickup day with the longest trip distance (<100 miles)"
echo "============================================================"

echo "SQL Query:"
cat <<'SQL'
SELECT 
    lpep_pickup_datetime::date AS pickup_day,
    MAX(trip_distance) AS max_trip_distance
FROM green_tripdata_nov
GROUP BY 1
HAVING MAX(trip_distance) <= 100
ORDER BY 2 DESC;
SQL

echo
echo "Explanation:"
echo "This query finds the day with the maximum trip distance, filtering out outliers over 100 miles."
echo
echo "Answer 4: 2025-11-14"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 5: Pickup zone with the largest total_amount on November 18, 2025"
echo "============================================================"

echo "SQL Query:"
cat <<'SQL'
SELECT 
    b."Zone" AS pickup_zone,
    SUM(total_amount) AS total_sum
FROM green_tripdata_nov a
LEFT JOIN zones b
    ON a."PULocationID" = b."LocationID"
WHERE lpep_pickup_datetime::date = '2025-11-18'
GROUP BY 1
ORDER BY 2 DESC;
SQL

echo
echo "Explanation:"
echo "We join trip records with the zone lookup table to group by pickup zone and find the zone with the highest total fare amount."
echo
echo "Answer 5: East Harlem North"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 6: For pickups in 'East Harlem North', drop-off zone with the largest tip"
echo "============================================================"

echo "SQL Query:"
cat <<'SQL'
SELECT 
    c."Zone" AS drop_off_zone,
    MAX(tip_amount) AS max_tip
FROM green_tripdata_nov a
LEFT JOIN zones b
    ON a."PULocationID" = b."LocationID"
LEFT JOIN zones c
    ON a."DOLocationID" = c."LocationID"
WHERE b."Zone" = 'East Harlem North'
  AND lpep_pickup_datetime::date BETWEEN '2025-11-01' AND '2025-11-30'
GROUP BY 1
ORDER BY 2 DESC;
SQL

echo
echo "Explanation:"
echo "This query identifies the drop-off zone where passengers from 'East Harlem North' tipped the most in November 2025."
echo
echo "Answer 6: Yorkville West"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Question 7: Terraform workflow"
echo "============================================================"

echo "Explanation:"
echo "The standard Terraform workflow follows three main steps:"
echo
echo "1) terraform init              # Initializes plugins and sets up backend"
echo "2) terraform apply -auto-approve  # Creates or updates infrastructure"
echo "3) terraform destroy            # Removes all resources"
echo
echo "Answer 7: terraform init, terraform apply -auto-approve, terraform destroy"
echo

# ------------------------------------------------------------
echo "============================================================"
echo "Summary of Answers"
echo "============================================================"

echo "1: 25.3"
echo "2: db:5432"
echo "3: 8,007"
echo "4: 2025-11-14"
echo "5: East Harlem North"
echo "6: Yorkville West"
echo "7: terraform init, terraform apply -auto-approve, terraform destroy"

echo
echo "==================== End of Homework 1 ===================="
echo
