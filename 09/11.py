white_list = list()
search_queries = list()
for _ in range(int(input())):
    white_list.append(input())
for _ in range(int(input())):
    search_queries.append(input())

for query in search_queries:
    if query in white_list:
        print(query)
