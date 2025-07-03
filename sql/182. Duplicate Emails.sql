# Write your MySQL query statement below
WITH CTE_Duplicates AS(
    SELECT email, COUNT(id) as cnt
    FROM Person
    GROUP BY 1
)
SELECT email FROM CTE_Duplicates WHERE cnt > 1
;