import json

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")
    print("-" * 30)