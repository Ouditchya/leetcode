SELECT MAX(num) AS num
FROM (
SELECT num, COUNT(*) AS cnt
FROM MyNumbers
GROUP BY 1
HAVING cnt = 1
) t
;