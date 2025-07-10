# Write your MySQL query statement below
WITH CTE_nbClient AS(
    SELECT DISTINCT users_id AS client_id
    FROM Users 
    WHERE banned = "No" AND role = "client"
),
CTE_nbDriver AS(
    SELECT DISTINCT users_id AS driver_id
    FROM Users 
    WHERE banned = "No" AND role = "driver"
)
SELECT request_at AS Day,
    ROUND(SUM(CASE WHEN x.status LIKE '%cancel%' THEN 1 ELSE 0 END)/ COUNT(DISTINCT id), 2) AS "Cancellation Rate"
FROM Trips x
WHERE x.request_at BETWEEN "2013-10-01" and "2013-10-03"
    AND x.client_id IN (SELECT a.client_id FROM CTE_nbClient a)
    AND x.driver_id IN (SELECT b.driver_id FROM CTE_nbDriver b)
GROUP BY 1
;