import sys

num_list = list()
for line in sys.stdin:
    num_list.append(int(line))
if num_list:
    print(sum(num_list) / len(num_list))
else:
    print(-1)
