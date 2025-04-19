WITH CTE_Products AS(
    SELECT product_id, new_price as price, change_date,
        DATEDIFF('2019-08-16', change_date) AS date_diff,
        DENSE_RANK() OVER(PARTITION BY product_id ORDER BY DATEDIFF('2019-08-16', change_date)) AS dk
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT DISTINCT p1.product_id, COALESCE(p2.price, 10) AS price
FROM Products p1 
    LEFT JOIN (SELECT * FROM CTE_Products WHERE dk = 1) p2
        ON p1.product_id = p2.product_id
;