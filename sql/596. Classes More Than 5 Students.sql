SELECT DISTINCT class
FROM (
SELECT class, COUNT(DISTINCT student) AS cnt
FROM Courses
GROUP BY class
HAVING cnt >= 5
) t
;