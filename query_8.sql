SELECT AVG(Grades.grade) as avg_grade
FROM Grades
JOIN Subjects ON Grades.subject_id = Subjects.id
WHERE Subjects.teacher_id = ? AND Subjects.id = ?;