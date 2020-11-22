student_attendance = {"Pedro": 96, "João": 100, "Maria": 89}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

print()
print(student_attendance.items())

*head, tail = [1, 2, 3, 4, 5, 6]
print(head)
print(tail)

primeiro, *ultimos = [1, 2, 3, 4, 5, 6]
print(primeiro)
print(ultimos)


students = [
    {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)},
    {'name': 'Amado', 'school': 'Computing', 'grades': (56, 67, 78)},
    {'name': 'Batista', 'school': 'Computing', 'grades': (100, 89, 91)},
    {'name': 'Terezo', 'school': 'Computing', 'grades': (86, 81, 91)}

]


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count


print(average_grade_all_students(students))
