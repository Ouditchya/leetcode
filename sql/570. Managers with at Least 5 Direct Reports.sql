WITH CTE_reports AS(
    SELECT managerID, count(*) AS cnt_reports
    FROM Employee
    GROUP BY 1
)
SELECT name
FROM Employee e
JOIN CTE_reports r
ON e.id = r.managerID
WHERE r.cnt_reports >= 5
;