WITH CTE_Activity AS(
    SELECT machine_id, process_id, activity_type, timestamp as end,
        LAG(timestamp, 1) OVER(PARTITION BY machine_id, process_id ORDER BY timestamp) AS start
    FROM Activity
),
CTE_Process AS(
    SELECT machine_id, process_id, (end - start) as process_duration
    FROM CTE_Activity
    WHERE activity_type = 'end'
)
SELECT machine_id, ROUND(SUM(process_duration)/ COUNT(DISTINCT process_id), 3) AS processing_time
FROM CTE_Process
GROUP BY machine_id
;