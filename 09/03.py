count = int(input())
search_list = list()
for i in range(count):
    search_list.append(input())
count = int(input()) - 1
for i in search_list:
    print(i[count])
