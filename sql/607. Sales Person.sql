# Write your MySQL query statement below
WITH CTE_consolidate AS(
    SELECT t1.name,
        SUM(CASE WHEN t3.name = "RED" THEN 1 ELSE 0 END) AS query
    FROM SalesPerson t1
        LEFT JOIN Orders t2
            ON t1.sales_id = t2.sales_id
        LEFT JOIN Company t3
            ON t2.com_id = t3.com_id
    GROUP BY t1.name
)
SELECT name FROM CTE_consolidate
WHERE query = 0
;