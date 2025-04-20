# Write your MySQL query statement below
WITH CTE_user AS(
    SELECT t1.user_id, t2.name, COUNT(DISTINCT t1.movie_id) AS cnt_movie_review
    FROM MovieRating t1
        JOIN Users t2
            ON t1.user_id = t2.user_id
    GROUP BY 1, 2
),
CTE_user_rank AS(
    SELECT *, DENSE_RANK() OVER(ORDER BY cnt_movie_review DESC, name ASC) AS dk
    FROM CTE_user
),
CTE_movie AS(
    SELECT t1.movie_id, t2.title, AVG(rating) AS avg_rating
    FROM MovieRating t1
        JOIN Movies t2
            ON t1.movie_id = t2.movie_id
    WHERE t1.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY 1, 2
),
CTE_movie_rank AS(
    SELECT *, DENSE_RANK() OVER(ORDER BY avg_rating DESC, title ASC) AS dk
    FROM CTE_movie
)
SELECT name AS results FROM CTE_user_rank WHERE dk = 1
UNION ALL
SELECT title AS results FROM CTE_movie_rank WHERE dk = 1
;