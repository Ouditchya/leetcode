WITH CTE_Exams AS(
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY 1, 2
),
CTE_Enroll AS(
    SELECT student_id, student_name, subject_name
    FROM Students
        CROSS JOIN Subjects
)
SELECT DISTINCT s.student_id, s.student_name, s.subject_name, COALESCE(e.attended_exams, 0) AS attended_exams
FROM CTE_Enroll s
LEFT JOIN CTE_Exams e
ON s.student_id = e.student_id
AND s.subject_name = e.subject_name
ORDER BY s.student_id, s.subject_name
;