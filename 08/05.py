advices_list = list()
for i in range(int(input())):
    advices_list.append(input())
for advice in advices_list:
    check = advice[0] + advice[1]
    if check.lower() == "не":
        print(advice[3::])
    else:
        print(advice)

