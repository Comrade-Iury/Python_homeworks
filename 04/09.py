count = int(input())
for i in range(1, count + 1):
    print(" " * (count - i), "*" * ((i * 2) - 1))