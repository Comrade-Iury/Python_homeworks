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
mouths_list = list()
for _ in range(int(input())):
    mouths_list.append(input())
for mouth in mouths_list:
    if mouth in classmates_dict:
        print(classmates_dict[mouth])
    else:
        print()