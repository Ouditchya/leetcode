WITH CTE_activity AS(
    SELECT player_id, device_id, event_date, games_played,
        DENSE_RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS dk,
        LEAD(event_date, 1) OVER(PARTITION BY player_id ORDER BY event_date) AS next_event_date
    FROM Activity
)
SELECT COALESCE(ROUND(COUNT(DISTINCT x.player_id)/ COUNT(DISTINCT y.player_id), 2), 0) AS fraction
FROM (SELECT DISTINCT player_id FROM CTE_activity WHERE DATEDIFF(next_event_date, event_date) = 1 AND dk = 1) x
JOIN Activity y
ON 1 = 1
;