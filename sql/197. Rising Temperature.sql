WITH CTE_weather AS(
    SELECT DISTINCT id, recordDate, 
        LAG(recordDate, 1) OVER(ORDER BY recordDate) as recordDate_prev,
        temperature, 
        LAG(temperature, 1) OVER(ORDER BY recordDate) as temperature_prev
    FROM Weather
)
SELECT id
FROM CTE_weather
WHERE temperature > temperature_prev
AND DATEDIFF(recordDate, recordDate_prev) = 1
;