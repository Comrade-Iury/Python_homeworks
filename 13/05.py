classmates_dict = dict()
for _ in range(int(input())):
    info = input().split()
    if info[2] not in classmates_dict:
        classmates_dict[info[2]] = info[0]
    else:
        if classmates_dict[info[2]] < info[0]:
            classmates_dict[info[2]] = classmates_dict[info[2]] + " " + info[0]
        else:
            classmates_dict[info[2]] = info[0] + " " + classmates_dict[info[2]]
months_list = list()
for _ in range(int(input())):
    months_list.append(input())
for month in months_list:
    if month in classmates_dict:
        print(classmates_dict[month])
    else:
        print()