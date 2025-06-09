# Write your MySQL query statement below
WITH CTE_Product AS(
    SELECT DISTINCT T1.user_id, T2.category
    FROM ProductPurchases T1
        JOIN ProductInfo T2
            ON T1.product_id = T2.product_id
),
CTE_Pairs AS(
    SELECT DISTINCT T1.category AS category1, T2.category AS category2, T1.user_id
    FROM CTE_Product T1
        JOIN CTE_Product T2
            ON T1.user_id = T2.user_id
                AND T1.category < T2.category
)
SELECT category1, category2, COUNT(DISTINCT user_id) AS customer_count
FROM CTE_Pairs
GROUP BY category1, category2
HAVING customer_count >= 3
ORDER BY customer_count DESC, category1, category2
;