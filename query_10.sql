SELECT Subjects.name
FROM Subjects
JOIN Grades ON Subjects.id = Grades.subject_id
WHERE Subjects.teacher_id = ? AND Grades.student_id = ?;