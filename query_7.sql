SELECT Students.name, Grades.grade
FROM Students
JOIN Grades ON Students.id = Grades.student_id
WHERE Students.group_id = ? AND Grades.subject_id = ?;