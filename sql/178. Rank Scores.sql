# Write your MySQL query statement below
SELECT score, rk as "rank" FROM(
SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS rk
FROM Scores
) t
ORDER BY 2
;