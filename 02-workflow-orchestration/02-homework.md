# Homework 2: Kestra Orchestrator
**Data Engineering Zoomcamp 2026** **Due date:** 03 February 2026  

---

## Question 1: Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?  

**Explanation:** 
The upload_to_gcs logs, the raw byte count was 134,481,400 bytes. When you convert those bytes into binary Megabytes (MiB) by dividing by 1,024 twice (134,481,400 / 1024 / 1024), it equals exactly 128.25, which rounds to the course answer of 128.3 MiB. 

**Answer: 128.3 MiB**  
---

## Question 2: What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

**Explanation:** 
Kestra uses a process called rendering to turn template code into actual text. In your flow, the filename variable is constructed like this:

{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv

Sticking those parts together in order gives you the final string: green_tripdata_2020-04.csv.


**Answer: green_tripdata_2020-04.csv.** 

## Question 3: How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

**Explanation:** 
Process: 1. Executed a Backfill in Kestra for the yellow taxi type covering the date range 2020-01-01 to 2020-12-31. 2. Verified the data was loaded into the yellow_tripdata table. 3. Ran the following SQL query to get the total count:

**SQL Query:** 
```
SELECT count(*) 
FROM public.yellow_tripdata 
WHERE filename LIKE 'yellow_tripdata_2020%;
```
**Answer:24,648,499**


## Question 4: How many rows are there for the Green Taxi data for all CSV files in the year 2020?

**Explanation:**
Performed a Backfill in Kestra for the green taxi type for the entire year of 2020 (2020-01-01 to 2020-12-31). 2. Once all 12 executions were successful, I queried the database to aggregate the total rows across those files. 3. Used the following SQL query to verify the count:

**SQL Query:**  
```
SELECT count(*) 
FROM public.green_tripdata 
WHERE filename LIKE 'green_tripdata_2020%;
```

**Answer:1,734,051**

## Question 5: How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

**Explanation:** 
Executed the Kestra flow manually via backfill for taxi: yellow, year: 2021, and month: 03. Verified the successful upload to the database. 3. Ran the following SQL query to isolate that specific month's data:

**SQL Query:**  
```
SELECT count(*) 
FROM public.yellow_tripdata 
WHERE filename = 'yellow_tripdata_2021-03.csv';
```

**Answer:1,925,152** 

## Question 6: How would you configure the timezone to New York in a Schedule trigger?

**Explanation:** 
Add a timezone property set to America/New_York.This ensures the schedule follows the local time of the data source (NYC) rather than the default UTC. 

**Answer:Add a timezone property set to America/New_York in the Schedule trigger configuration**

---
## Summary of Answers

| Question | Answer |
|----------|--------|
| 1        | 128.3 MiB |
| 2        | `green_tripdata_2020-04.csv` |
| 3        | 24,648,499 |
| 4        | 1,734,051 |
| 5        | 1,925,152 |
| 6        | Add a `timezone` property set to `America/New_York` in the Schedule trigger configuration |

---

✅ **End of Homework 2**
