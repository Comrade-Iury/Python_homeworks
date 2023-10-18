num_1 = float(input())
num_2 = float(input())
symbol = input()

if symbol == "-":
    print(num_1 - num_2)
elif symbol == "+":
    print(num_1 + num_2)
elif symbol == "/" and num_2 != 0:
    print(num_1 / num_2)
elif symbol == "*":
    print(num_1 * num_2)
else:
    print("88888")