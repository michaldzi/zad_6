SELECT Subjects.name
FROM Subjects
JOIN Grades ON Subjects.id = Grades.subject_id
WHERE Grades.student_id = ?;