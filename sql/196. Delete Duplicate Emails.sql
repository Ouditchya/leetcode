WITH CTE_dups AS(
    SELECT id, email, DENSE_RANK() OVER(PARTITION BY email ORDER BY id) AS dk
    FROM Person
)
DELETE FROM Person p WHERE p.id IN (SELECT d.id FROM CTE_dups d WHERE dk > 1)
;