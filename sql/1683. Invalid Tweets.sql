SELECT DISTINCT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;