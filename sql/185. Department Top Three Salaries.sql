WITH CTE_rank_unique AS(
    SELECT *, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS dk
    FROM Employee
)
,CTE_top_3_unique AS(
    SELECT * FROM CTE_rank_unique WHERE dk <= 3
)
SELECT t2.name AS Department, t1.name AS Employee, t1.salary AS Salary
FROM CTE_top_3_unique t1
    JOIN Department t2
        ON t1.departmentId = t2.id
;