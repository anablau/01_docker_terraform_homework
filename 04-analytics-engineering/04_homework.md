# 📝 Homework Answers

---

## Question 1: dbt Lineage and Execution

- **Query:** `dbt run --select int_trips_unioned`
- **Result:** `int_trips_unioned` only
- **Logic:** Without graph operators (like `+`), dbt only builds the specific model named.

---

## Question 2: dbt Tests

- **Scenario:** A new value `6` appears in a column with an `accepted_values` test.
- **Result:** dbt will **fail** the test, returning a non-zero exit code
- **Logic:** Tests that return rows are considered failures, and dbt exits with **Code 1**.

---

## Question 3: Total Record Count

- **Query:** `SELECT count(*) FROM prod.fct_monthly_zone_revenue`
- **Result:** `12,998`
- **Note:** This may vary slightly based on specific dataset versions.

---

## Question 4: Best Performing Zone (2020)

- **Highest Revenue Zone:** East Harlem South

```sql
SELECT pickup_zone, SUM(revenue_monthly_total_amount) AS rev
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY 1
ORDER BY rev DESC
LIMIT 1;
```

---

## Question 5: October 2019 Green Taxi Trips

- **Total Trips:** `421,509`

```sql
SELECT SUM(total_monthly_trips)
FROM prod.fct_monthly_zone_revenue
WHERE service_type = 'Green'
  AND EXTRACT(YEAR FROM revenue_month) = 2019
  AND EXTRACT(MONTH FROM revenue_month) = 10;
```

---

## Question 6: FHV Staging Model Count

- **Total Records:** `43,244,693`
- **Logic:** This count excludes records where `dispatching_base_num` is NULL.
