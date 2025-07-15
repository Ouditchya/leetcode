# Write your MySQL query statement below
WITH CTE_consolidate AS(
    SELECT t1.product_id, t2.product_name,
        SUM(CASE WHEN sale_date BETWEEN '2019-01-01' AND '2019-03-31' THEN 1 ELSE 0 END) AS q1,
        SUM(CASE WHEN sale_date < '2019-01-01' OR sale_date > '2019-03-31' THEN 1 ELSE 0 END) AS q2
    FROM Sales t1
        JOIN Product t2
            ON t1.product_id = t2.product_id
    GROUP BY 1, 2
)
SELECT product_id, product_name
FROM CTE_consolidate
WHERE q1 > 0 AND q2 = 0
;