WITH CTE_manager AS(
    SELECT DISTINCT t1.manager_id
    FROM Employees t1
        JOIN Employees t2
            ON t1.manager_id = t2.employee_id
)
SELECT t1.employee_id
FROM Employees t1
WHERE t1.manager_id NOT IN (SELECT DISTINCT manager_id FROM CTE_manager)
AND t1.salary < 30000
ORDER BY 1
;