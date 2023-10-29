count = int(input())
search_list = list()
for i in range(count):
    search_list.append(input())
request = input()
for i in search_list:
    if request in i:
        print(i)

