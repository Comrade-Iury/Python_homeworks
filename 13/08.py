explanatory_dict = dict()
for _ in range(int(input())):
    new_line = input().split()
    key = new_line.pop(0).lower()
    explanatory_dict[key] = " ".join(new_line)
for _ in range(int(input())):
    new_key = input().lower()
    if new_key in explanatory_dict:
        print(explanatory_dict[new_key])
    else:
        print("Нет в словаре")