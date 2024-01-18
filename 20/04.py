import sys

code_list = list()
for line in sys.stdin:
    code_list.append(line)

print(sum(map(lambda l: int(l.strip()[0] == "#"), code_list)))