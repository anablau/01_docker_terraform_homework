Homework 1: Docker, SQL and Terraform

**Data Engineering Zoomcamp 2026** **Due date:** 27 January 2026  


---


## Question 1: What's the version of pip in the python:3.13 image?  


**Explanation:** The official `python:3.13` Docker image comes with **pip version 25.3** preinstalled.  


**Command used to check:** ```bash

docker run -it --rm --entrypoint bash python:3.13 -c "

python --version

pip --version

"

Answer: ``` 25.3



---


## Question 2: Hostname and port pgAdmin should use to connect to Postgres  


**Explanation:** Inside a Docker Compose network, containers communicate via service names.  

If the database service is named `db` and uses the default Postgres port `5432`,  

pgAdmin should connect using:


Hostname: db Port: 5432



**Answer:** ```

db:5432

Question 3: Number of trips in November 2025 with trip_distance <= 1 mile

SQL Query: ```sql SELECT COUNT(1) FROM green_tripdata_nov WHERE lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01' AND trip_distance <= 1;



**Explanation:** This query counts the number of trips where `trip_distance` is less than or equal to 1 mile during November 2025.  


**Answer:** ```

8,007

Question 4: Pickup day with the longest trip distance (<100 miles)

SQL Query: ```sql SELECT lpep_pickup_datetime::date AS pickup_day, MAX(trip_distance) AS max_trip_distance FROM green_tripdata_nov GROUP BY 1 HAVING MAX(trip_distance) <= 100 ORDER BY 2 DESC;



**Explanation:** This query finds the day with the maximum trip distance, filtering out outliers over 100 miles.  


**Answer:** ```

2025-11-14

Question 5: Pickup zone with the largest total_amount on November 18, 2025

SQL Query: ```sql SELECT b."Zone" AS pickup_zone, SUM(total_amount) AS total_sum FROM green_tripdata_nov a LEFT JOIN zones b ON a."PULocationID" = b."LocationID" WHERE lpep_pickup_datetime::date = '2025-11-18' GROUP BY 1 ORDER BY 2 DESC;



**Explanation:** We join trip records with the zone lookup table to group by pickup zone and find the zone with the highest total fare amount.  


**Answer:** ```

East Harlem North

Question 6: For pickups in 'East Harlem North', drop-off zone with the largest tip

SQL Query: ```sql SELECT c."Zone" AS drop_off_zone, MAX(tip_amount) AS max_tip FROM green_tripdata_nov a LEFT JOIN zones b ON a."PULocationID" = b."LocationID" LEFT JOIN zones c ON a."DOLocationID" = c."LocationID" WHERE b."Zone" = 'East Harlem North' AND lpep_pickup_datetime::date BETWEEN '2025-11-01' AND '2025-11-30' GROUP BY 1 ORDER BY 2 DESC;



**Explanation:** This query identifies the drop-off zone where passengers from 'East Harlem North' tipped the most in November 2025.  


**Answer:** ```

Yorkville West

Question 7: Terraform workflow

Explanation: The standard Terraform workflow follows three main steps:


Bash


1) terraform init                 # Initializes plugins and sets up backend

2) terraform apply -auto-approve  # Creates or updates infrastructure

3) terraform destroy              # Removes all resources

Answer: ``` terraform init, terraform apply -auto-approve, terraform destroy



---


## Summary of Answers


| Question | Answer |

|----------|--------|

| 1        | 25.3   |

| 2        | db:5432 |

| 3        | 8,007  |

| 4        | 2025-11-14 |

| 5        | East Harlem North |

| 6        | Yorkville West |

| 7        | terraform init, terraform apply -auto-approve, terraform destroy |


---


✅ **End of Homework 1**





# Homework 1: Docker, SQL and Terraform

**Data Engineering Zoomcamp 2026**  

**Due date:** 27 January 2026  


---


## Question 1: What's the version of pip in the python:3.13 image?  


**Explanation:**  

The official `python:3.13` Docker image comes with **pip version 25.3** preinstalled.  


**Command used to check:**  

\`\`\`bash

docker run -it --rm --entrypoint bash python:3.13 -c "

python --version

pip --version

"

\`\`\`


**Answer:**  

\`\`\`

25.3

\`\`\`


---


## Question 2: Hostname and port pgAdmin should use to connect to Postgres  


**Explanation:**  

Inside a Docker Compose network, containers communicate via service names.  

If the database service is named `db` and uses the default Postgres port `5432`,  

pgAdmin should connect using:


\`\`\`

Hostname: db

Port: 5432

\`\`\`


**Answer:**  

\`\`\`

db:5432

\`\`\`


---


## Question 3: Number of trips in November 2025 with trip_distance <= 1 mile  


**SQL Query:**  

\`\`\`sql

SELECT COUNT(1)

FROM green_tripdata_nov

WHERE lpep_pickup_datetime >= '2025-11-01'

  AND lpep_pickup_datetime < '2025-12-01'

  AND trip_distance <= 1;

\`\`\`


**Explanation:**  

This query counts the number of trips where `trip_distance` is less than or equal to 1 mile during November 2025.  


**Answer:**  

\`\`\`

8,007

\`\`\`


---


## Question 4: Pickup day with the longest trip distance (<100 miles)  


**SQL Query:**  

\`\`\`sql

SELECT 

    lpep_pickup_datetime::date AS pickup_day,

    MAX(trip_distance) AS max_trip_distance

FROM green_tripdata_nov

GROUP BY 1

HAVING MAX(trip_distance) <= 100

ORDER BY 2 DESC;

\`\`\`


**Explanation:**  

This query finds the day with the maximum trip distance, filtering out outliers over 100 miles.  


**Answer:**  

\`\`\`

2025-11-14

\`\`\`


---


## Question 5: Pickup zone with the largest total_amount on November 18, 2025  


**SQL Query:**  

\`\`\`sql

SELECT 

    b."Zone" AS pickup_zone,

    SUM(total_amount) AS total_sum

FROM green_tripdata_nov a

LEFT JOIN zones b

    ON a."PULocationID" = b."LocationID"

WHERE lpep_pickup_datetime::date = '2025-11-18'

GROUP BY 1

ORDER BY 2 DESC;

\`\`\`


**Explanation:**  

We join trip records with the zone lookup table to group by pickup zone and find the zone with the highest total fare amount.  


**Answer:**  

\`\`\`

East Harlem North

\`\`\`


---


## Question 6: For pickups in 'East Harlem North', drop-off zone with the largest tip  


**SQL Query:**  

\`\`\`sql

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

\`\`\`


**Explanation:**  

This query identifies the drop-off zone where passengers from 'East Harlem North' tipped the most in November 2025.  


**Answer:**  

\`\`\`

Yorkville West

\`\`\`


---


## Question 7: Terraform workflow  


**Explanation:**  

The standard Terraform workflow follows three main steps:


\`\`\`bash

1) terraform init                  # Initializes plugins and sets up backend

2) terraform apply -auto-approve  # Creates or updates infrastructure

3) terraform destroy               # Removes all resources

\`\`\`


**Answer:**  

\`\`\`

terraform init, terraform apply -auto-approve, terraform destroy

\`\`\`


---


## Summary of Answers


| Question | Answer |

|----------|--------|

| 1        | 25.3   |

| 2        | db:5432 |

| 3        | 8,007  |

| 4        | 2025-11-14 |

| 5        | East Harlem North |

| 6        | Yorkville West |

| 7        | terraform init, terraform apply -auto-approve, terraform destroy |


---


✅ **End of Homework 1** 
