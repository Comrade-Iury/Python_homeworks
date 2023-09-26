students = set()
students_count = int(input()) + int(input())

for _ in range(students_count):
    new_student = {input()}
    if new_student <= students:
        students = students - new_student
        new_student.pop()
    else:
        students = students | new_student

if students:
    print(len(students))
else:
    print("No")
