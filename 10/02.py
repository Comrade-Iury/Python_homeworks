count = int(input())
students_list = []
for i in range(count):
    students_list.append(input().split("\t"))
for i in students_list:
    print("\t".join(i))
print("\n")
for i in students_list:
    if int(i[1]) >= 4:
        print("\t".join(i))
