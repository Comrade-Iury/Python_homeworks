lists_count = int(input())
first_list = set()
for _ in range(int(input())):
    first_list.add(input())
for lists in range(lists_count - 1):
    new_list = set()
    for _ in range(int(input())):
        new_list.add(input())
    first_list = first_list & new_list
    new_list.clear()

for student in first_list:
    print(student)
