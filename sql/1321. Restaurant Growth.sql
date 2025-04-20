WITH CTE_Amount AS(
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY 1
),
CTE_Customer AS(
    SELECT visited_on,
        DENSE_RANK() OVER(ORDER BY visited_on) AS dk,
        SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM CTE_Amount
)
SELECT visited_on, amount, average_amount
FROM CTE_Customer
WHERE dk >= 7
ORDER BY 1
;