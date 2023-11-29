count = int(input())
numbers_list = list()
result = 0
for i in range(count):
    numbers_list.append(int(input()))
multiply = int(input())
for i in numbers_list:
    for j in numbers_list:
        if i * j == multiply:
            result = 1

if result:
    print("Yes")
else:
    print("No")
