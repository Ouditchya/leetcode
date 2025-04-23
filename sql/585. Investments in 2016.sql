WITH CTE_uq_city AS(
    SELECT lat, lon, COUNT(DISTINCT pid) AS cnt
    FROM Insurance
    GROUP BY 1, 2
    HAVING cnt = 1
)
,CTE_select AS(
    SELECT DISTINCT t1.lat, t1.lon, t1.tiv_2016
    FROM Insurance t1
        JOIN Insurance t2
            ON t1.tiv_2015 = t2.tiv_2015
                AND t1.pid != t2.pid
    WHERE (t1.lat, t1.lon) IN (SELECT DISTINCT t3.lat, t3.lon FROM CTE_uq_city t3)
        -- AND (t2.lat, t2.lon) IN (SELECT DISTINCT t3.lat, t3.lon FROM CTE_uq_city t3)
)
SELECT ROUND(COALESCE(SUM(tiv_2016), 0), 2) AS tiv_2016
FROM CTE_select
;