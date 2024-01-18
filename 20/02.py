students_list = list()
for i in range(int(input())):
    students_list.append([])
    for _ in range(int(input())):
        students_list[i].append(input().strip()[-1])
for i in range(len(students_list)):
    students_list[i] = any(map(lambda x: x == "5", students_list[i]))
if all(students_list):
    print("ДА")
else:
    print("НЕТ")
