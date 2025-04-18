SELECT contest_id, ROUND((COUNT(DISTINCT a.user_id)/ CNT_users) * 100, 2) AS percentage
FROM Register a
    JOIN (SELECT COUNT(DISTINCT user_id) AS CNT_users FROM Users) b
        ON 1 = 1
GROUP BY 1
ORDER BY 2 DESC, 1 ASC
;