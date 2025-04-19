WITH CTE_Employee AS(
    SELECT employee_id, department_id, primary_flag,
        DENSE_RANK() OVER(PARTITION BY employee_id ORDER BY primary_flag) as dk
    FROM Employee
)
SELECT employee_id, department_id
FROM CTE_Employee
WHERE dk = 1
;