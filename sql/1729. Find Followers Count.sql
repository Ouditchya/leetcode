SELECT user_id, COALESCE(COUNT(DISTINCT follower_id), 0) AS followers_count
FROM Followers
GROUP BY 1
ORDER BY 1
;