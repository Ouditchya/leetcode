SELECT p.project_id, ROUND(SUM(e.experience_years)/ COUNT(DISTINCT p.employee_id), 2) AS average_years
FROM Project p
    JOIN Employee e
        ON p.employee_id = e.employee_id
GROUP BY 1
;