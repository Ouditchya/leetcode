SELECT id,
CASE WHEN id % 2 = 1 THEN COALESCE(LEAD(student, 1) OVER(ORDER BY id), student)
     WHEN id % 2 = 0 THEN LAG(student, 1) OVER(ORDER BY id)
    END AS student
FROM Seat
;