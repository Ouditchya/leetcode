# Write your MySQL query statement below
SELECT DISTINCT t2.user_id AS buyer_id, t2.join_date, COALESCE(t1.orders_in_2019, 0) AS orders_in_2019
FROM (
SELECT buyer_id, COUNT(DISTINCT CASE WHEN YEAR(order_date) = 2019 THEN order_id END) AS orders_in_2019
FROM Orders
GROUP BY buyer_id
) t1
    RIGHT JOIN Users t2
        ON t1.buyer_id = t2.user_id
;