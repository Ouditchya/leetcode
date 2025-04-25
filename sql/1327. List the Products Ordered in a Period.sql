WITH CTE_feb20_sales AS(
    SELECT product_id, SUM(unit) AS total_units
    FROM Orders
    WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY 1
    HAVING total_units >= 100
)
SELECT t2.product_name, t1.total_units AS unit
FROM CTE_feb20_sales t1
    JOIN Products t2
        ON t1.product_id = t2.product_id
;