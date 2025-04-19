WITH CTE_Products AS(
    SELECT COUNT(*) as cnt_products FROM Product
),
CTE_Customers AS(
    SELECT customer_id, COUNT(DISTINCT product_key) AS cnt_products_purchased
    FROM Customer
    GROUP BY 1
)
SELECT customer_id
FROM CTE_Customers
    JOIN CTE_Products
        ON 1 = 1
WHERE cnt_products_purchased = cnt_products
;