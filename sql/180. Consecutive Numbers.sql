WITH CTE_Logs AS(
    SELECT id, num as num1,
        LEAD(num, 1) OVER(ORDER BY id) AS num2,
        LEAD(num, 2) OVER(ORDER BY id) AS num3
    FROM Logs
)
SELECT DISTINCT num1 AS ConsecutiveNums
FROM CTE_Logs
WHERE num1 = num2 AND num2 = num3
;