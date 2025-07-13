# Write your MySQL query statement below
WITH CTE_orders AS(
    SELECT customer_number, COUNT(order_number) AS cnt_orders
    FROM Orders
    GROUP BY 1
)
SELECT customer_number
FROM CTE_orders
WHERE cnt_orders = (SELECT MAX(cnt_orders) FROM CTE_orders)
;