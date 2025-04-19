WITH CTE_Queue AS(
    SELECT *, SUM(weight) OVER(ORDER BY turn ASC) AS sum_weight
    FROM Queue
)
SELECT DISTINCT person_name
FROM CTE_Queue
WHERE sum_weight <= 1000
ORDER BY sum_weight DESC
LIMIT 1
;