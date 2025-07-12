# Write your MySQL query statement below
WITH CTE_combined AS(
    SELECT DISTINCT 
        sale_id, sale_date, quantity, price,
        t1.product_id, product_name, category,
        CASE WHEN MONTH(sale_date) IN (1, 2, 12) THEN "Winter"
             WHEN MONTH(sale_date) IN (3, 4, 5) THEN "Spring"
             WHEN MONTH(sale_date) IN (6, 7, 8) THEN "Summer"
             WHEN MONTH(sale_date) IN (9, 10, 11) THEN "Fall"
            END AS season
    FROM sales t1
        JOIN products t2
            ON t1.product_id = t2.product_id
),
CTE_Summary AS(
    SELECT season, category, 
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS total_revenue
    FROM CTE_combined
    GROUP BY season, category
),
CTE_Rank_Summary AS(
    SELECT *,
        RANK() OVER(PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS rk
    FROM CTE_Summary
)
SELECT season, category, total_quantity, total_revenue
FROM CTE_Rank_Summary
WHERE rk = 1
ORDER BY season
;