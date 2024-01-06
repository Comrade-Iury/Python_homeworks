rpn_list = input().split()
numbers_list = list()

for symbol in rpn_list:
    if symbol.isnumeric():
        numbers_list.append(int(symbol))
        continue
    if symbol == "+":
        result = int(numbers_list[-2]) + int(numbers_list[-1])
    elif symbol == "-":
        result = int(numbers_list[-2]) - int(numbers_list[-1])
    elif symbol == "*":
        result = int(numbers_list[-2]) * int(numbers_list[-1])
    numbers_list.pop()
    numbers_list.pop()
    numbers_list.append(result)

print(*numbers_list)

