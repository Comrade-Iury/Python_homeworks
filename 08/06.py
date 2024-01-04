max_lenght = int(input())
headlines_list = list()
for _ in range(int(input())):
    headlines_list.append(input())

for headline in headlines_list:
    if len(headline) > max_lenght:
        print(headline[:max_lenght - 3:] + "...")
    else:
        print(headline)
