WITH CTE_counts AS(
    SELECT user_id, 
        COUNT(DISTINCT CASE WHEN action = 'timeout' THEN time_stamp END) AS cnt_timeout,
        COUNT(DISTINCT CASE WHEN action = 'confirmed' THEN time_stamp END) AS cnt_confirmed
    FROM Confirmations
    GROUP BY 1
)
SELECT s.user_id,
    ROUND(COALESCE(cnt_confirmed/ (cnt_confirmed + cnt_timeout), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN CTE_counts c
ON s.user_id = c.user_id
;