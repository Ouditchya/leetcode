WITH CTE_orders AS(
    SELECT *,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as dk
    FROM Delivery
)
,CTE_immediate_orders AS(
    SELECT * FROM CTE_orders
    WHERE dk = 1 AND order_date = customer_pref_delivery_date
)
SELECT ROUND((COUNT(DISTINCT x.customer_id)/ COUNT(DISTINCT y.customer_id)) * 100, 2) AS immediate_percentage
FROM CTE_immediate_orders x
JOIN Delivery y
-- (SELECT DISTINCT delivery_id FROM Delivery WHERE order_date = customer_pref_delivery_date) y
ON 1 = 1
;