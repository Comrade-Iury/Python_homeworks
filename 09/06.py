count = int(input())
num_list = list()
for i in range(count):
    num_list.append(int(input()))
for i in range(count - 1):
    print(num_list[i] + num_list[i + 1])
