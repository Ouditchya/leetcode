WITH CTE_transactions AS(
    SELECT customer_id, v.visit_id, 
        COUNT(DISTINCT transaction_id) AS CNT_transactions
    FROM Visits v
        LEFT JOIN Transactions t
            ON v.visit_id = t.visit_id
    GROUP BY customer_id, v.visit_id
)
SELECT customer_id, COUNT(DISTINCT visit_id) as count_no_trans
FROM CTE_transactions
WHERE CNT_transactions = 0
GROUP BY customer_id
;