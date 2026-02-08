# Homework 3: BigQuery Data Warehousing

**Data Engineering Zoomcamp 2026**  
**Due date:** 24 February 2026

---

## Question 1: What is count of records for the 2024 Yellow Taxi Data?

**Explanation:** To get the total record count, a simple COUNT(*) query is run against the native BigQuery table containing the 2024 Yellow Taxi data.

**SQL Query:**
```sql
SELECT count(*) 
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular`;
```

**Answer:** 20,332,093

---

## Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables. What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

**Explanation:** BigQuery handles metadata differently for managed vs. unmanaged storage. For the External Table, BigQuery does not have pre-calculated metadata for the files in GCS, resulting in an estimate of 0 MB. For the Native Table, BigQuery's columnar storage tracks exactly how much data is in the PULocationID column, leading to an estimate of 155.12 MB.

**SQL Query:**
```sql
-- External Table (Estimated: 0 MB)
SELECT COUNT(DISTINCT PULocationID) 
FROM `dtc-de-course-484508.trips_data_all.external_yellow_tripdata`;

-- Native Table (Estimated: 155.12 MB)
SELECT COUNT(DISTINCT PULocationID) 
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular`;
```

**Answer:** 0 MB for the External Table and 155.12 MB for the Native Table

---

## Question 3: Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated bytes different?

**Explanation:** BigQuery uses Columnar Storage. Each column is stored separately. Selecting one column (PULocationID) scans only the data blocks for that specific column (~155 MB). Adding a second column (DOLocationID) requires BigQuery to read a second set of data blocks, doubling the amount of data processed (~310 MB).

**SQL Query:**
```sql
-- Single column scan
SELECT PULocationID 
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular`;

-- Two column scan
SELECT PULocationID, DOLocationID 
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular`;
```

**Answer:** BigQuery is a columnar database, and it proxies out the query to the relevant columns. Therefore, the more columns you include in your selection, the more data BigQuery must scan.

---

## Question 4: How many records have a fare_amount of 0?

**Explanation:** This query filters the dataset to count only rows where the fare_amount column is exactly 0.

**SQL Query:**
```sql
SELECT count(*) 
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular` 
WHERE fare_amount = 0;
```

**Answer:** 8,333

---

## Question 5: What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID?

**Explanation:** To optimize for time-based filtering and sorting by a specific ID, the table should be Partitioned by the datetime column (to skip unnecessary days of data) and Clustered by the VendorID (to collocate and pre-sort data within those partitions).

**SQL Query:**
```sql
CREATE OR REPLACE TABLE `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_partitioned_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `dtc-de-course-484508.trips_data_all.external_yellow_tripdata`;
```

**Answer:** Partition by tpep_dropoff_datetime and Cluster on VendorID

---

## Question 6: Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive). What is the estimated bytes for the regular table vs the partitioned table?

**Explanation:** On the Regular Table, BigQuery must scan the entire dataset to find the March dates (~310.24 MB). On the Partitioned Table, BigQuery uses "Partition Pruning" to only read the data blocks for those specific 15 days in March, drastically reducing the scan size (~26.84 MB).

**SQL Query:**
```sql
-- Query on Regular Table
SELECT DISTINCT(VendorID)
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_regular`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

-- Query on Partitioned Table
SELECT DISTINCT(VendorID)
FROM `dtc-de-course-484508.trips_data_all.yellow_tripdata_2024_partitioned_clustered`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```

**Answer:** 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

---

## Question 7: Where is the data stored in the External Table you created?

**Explanation:** External tables in BigQuery do not ingest data into managed storage. Instead, they act as a schema layer that points to files stored externally. In this case, the Parquet files reside in a Cloud Storage bucket.

**Answer:** GCP Bucket

---

## Question 8: It is best practice in Big Query to always cluster your data?

**Explanation:** Clustering is not recommended for tables smaller than 1 GB. The metadata overhead for maintaining clusters on small datasets can actually reduce performance without providing any cost-saving benefits.

**Answer:** False
