WITH CTE_Activities AS(
    SELECT DISTINCT sell_date, product
    FROM Activities
    ORDER BY 1, 2
)
SELECT sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(product ORDER BY product ASC) AS products
FROM CTE_Activities
GROUP BY 1
ORDER BY 1
;