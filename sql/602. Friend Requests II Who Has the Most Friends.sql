WITH CTE_requester AS(
    SELECT requester_id as id, COUNT(DISTINCT accepter_id) as num
    FROM RequestAccepted
    GROUP BY 1
),
CTE_accepter AS(
    SELECT accepter_id as id, COUNT(DISTINCT requester_id) as num
    FROM RequestAccepted
    GROUP BY 1
),
CTE_both AS(
    SELECT * FROM CTE_requester UNION ALL
    SELECT * FROM CTE_accepter
),
CTE_total AS(
    SELECT id, SUM(num) as num
    FROM CTE_both
    GROUP BY 1
)
SELECT * FROM CTE_total ORDER BY 2 DESC LIMIT 1
;