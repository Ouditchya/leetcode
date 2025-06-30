# Write your MySQL query statement below
WITH CTE_combined AS(
    SELECT T1.id, T1.name AS Customers, COUNT(T2.id) AS cnt
    FROM Customers T1
        LEFT JOIN Orders T2
            ON T1.id = T2.customerId
    GROUP BY T1.id, T1.name
)
SELECT Customers FROM CTE_combined
WHERE cnt = 0
;