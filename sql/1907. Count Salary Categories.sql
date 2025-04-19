WITH CTE_temp AS(
    SELECT 'Low Salary' AS category UNION
    SELECT 'Average Salary' AS category UNION
    SELECT 'High Salary' AS category
),
CTE_Accounts AS(
    SELECT
        CASE WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
            END AS category,
        COUNT(DISTINCT account_id) AS accounts_count
    FROM Accounts
    GROUP BY 1
)
SELECT t1.category, COALESCE(t2.accounts_count, 0) AS accounts_count
FROM CTE_temp t1
    LEFT JOIN CTE_Accounts t2
        ON t1.category = t2.category
;