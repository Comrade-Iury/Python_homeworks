students_1 = set()
students_2 = set()

students_count = int(input()) + int(input()) + int(input())

for _ in range(students_count):
    new_student = {input()}
    if not(new_student <= students_1):
        students_1 = students_1 | new_student
        new_student.pop()
    elif not(new_student <= students_2):
        students_2 = students_2 | new_student
        new_student.pop()
    else:
        students_2 = students_2 - new_student
        new_student.pop()

if students_2:
    print(len(students_2))
else:
    print("No")
