SELECT Groups.name, AVG(Grades.grade) as avg_grade
FROM Groups
JOIN Students ON Groups.id = Students.group_id
JOIN Grades ON Students.id = Grades.student_id
WHERE Grades.subject_id = ?
GROUP BY Groups.id;