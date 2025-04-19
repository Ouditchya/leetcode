SELECT t1.employee_id, t1.name, 
    COUNT(DISTINCT t2.employee_id) AS reports_count, 
    ROUND(AVG(t2.age), 0) AS average_age 
FROM Employees t1
    JOIN Employees t2
        ON t1.employee_id = t2.reports_to
GROUP BY 1, 2
ORDER BY 1
;