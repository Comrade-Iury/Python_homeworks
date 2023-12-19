number_list = list()
for _ in range(int(input())):
    number_list.append(int(input()))
first_num = int(input())
last_num = int(input())
now_num = 0
sum = 0
for num in number_list:
    now_num += 1
    if first_num <= now_num <= last_num:
        sum += num
print(sum)