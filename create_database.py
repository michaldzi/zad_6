import sqlite3
from faker import Faker
import random
from datetime import datetime


fake = Faker()


conn = sqlite3.connect("university.db")
cursor = conn.cursor()


cursor.execute(
    """
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES Groups(id)
)
"""
)

cursor.execute(
    """
CREATE TABLE Groups (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
)

cursor.execute(
    """
CREATE TABLE Teachers (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
)

cursor.execute(
    """
CREATE TABLE Subjects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES Teachers(id)
)
"""
)

cursor.execute(
    """
CREATE TABLE Grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE,
    FOREIGN KEY(student_id) REFERENCES Students(id),
    FOREIGN KEY(subject_id) REFERENCES Subjects(id)
)
"""
)


groups = ["Group A", "Group B", "Group C"]
teachers = [fake.name() for _ in range(4)]
subjects = [
    "Math",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "English",
    "Art",
]


for group in groups:
    cursor.execute("INSERT INTO Groups (name) VALUES (?)", (group,))


for teacher in teachers:
    cursor.execute("INSERT INTO Teachers (name) VALUES (?)", (teacher,))


teacher_ids = [row[0] for row in cursor.execute("SELECT id FROM Teachers")]
for subject in subjects:
    cursor.execute(
        "INSERT INTO Subjects (name, teacher_id) VALUES (?, ?)",
        (subject, random.choice(teacher_ids)),
    )


group_ids = [row[0] for row in cursor.execute("SELECT id FROM Groups")]
for _ in range(50):
    cursor.execute(
        "INSERT INTO Students (name, group_id) VALUES (?, ?)",
        (fake.name(), random.choice(group_ids)),
    )


student_ids = [row[0] for row in cursor.execute("SELECT id FROM Students")]
subject_ids = [row[0] for row in cursor.execute("SELECT id FROM Subjects")]

for student_id in student_ids:
    for _ in range(random.randint(10, 20)):
        cursor.execute(
            "INSERT INTO Grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
            (
                student_id,
                random.choice(subject_ids),
                random.randint(1, 5),
                fake.date_this_year(),
            ),
        )


conn.commit()


conn.close()
