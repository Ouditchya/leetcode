WITH CTE_Sales AS(
    SELECT product_id, year, quantity, price, sale_id,
        DENSE_RANK() OVER(PARTITION BY product_id ORDER BY year) AS rkm
    FROM Sales
)
SELECT product_id, year as first_year, SUM(quantity) AS quantity, price
FROM CTE_Sales
WHERE rkm = 1
GROUP BY 1, 2, 4
; 