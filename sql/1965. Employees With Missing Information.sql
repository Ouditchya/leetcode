# Write your MySQL query statement below
WITH CTE_All AS(
    SELECT DISTINCT employee_id FROM Employees
    UNION
    SELECT DISTINCT employee_id FROM Salaries
)
SELECT DISTINCT t1.employee_id 
FROM CTE_All t1
WHERE t1.employee_id NOT IN (SELECT DISTINCT employee_id FROM Employees)
    OR t1.employee_id NOT IN (SELECT DISTINCT employee_id FROM Salaries)
ORDER BY t1.employee_id
;