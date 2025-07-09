# Write your MySQL query statement below
WITH CTE_Emp AS(
    SELECT d.name AS Department, e.name AS Employee, e.salary,
        RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS rk
    FROM Employee e
        JOIN Department d
            ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM CTE_Emp
WHERE rk = 1
;