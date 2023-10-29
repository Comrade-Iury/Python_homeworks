count = int(input())
search_mirror_list = [0] * count
search_list = list()
request_list = list()
for i in range(count):
    search_list.append(input())
count = int(input())
for i in range(count):
    request_list.append(input())
count = 0
for i in search_list:
    for j in request_list:
        if j in i:
            search_mirror_list[count] += 1
    count += 1
for i in range(len(search_list)):
    if search_mirror_list[i] == len(request_list):
        print(search_list[i])
