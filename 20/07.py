import sys

code_list = list()
comment_dict = dict()
for line in sys.stdin:
    code_list.append(line)
for i in range(len(code_list)):
    if code_list[i].strip()[0] == "#":
        comment_dict[i] = code_list[i].strip()[1::].strip()
for num in comment_dict:
    print(f"line {num + 1}: {comment_dict[num]}")
