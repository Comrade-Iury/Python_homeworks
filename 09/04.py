count = int(input())
line_list = list()
num_list = list()
for i in range(count):
    line_list.append(input())
count = int(input())
for i in range(count):
    num_list.append(int(input()))
for i in num_list:
    print(line_list[i - 1])
