SELECT teacher_id, COALESCE(COUNT(DISTINCT subject_id), 0) AS cnt
FROM Teacher
GROUP BY teacher_id
;