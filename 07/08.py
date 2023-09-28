number = int(input())
while number <= 1000000000:
    number *= int(str(number)[0])
    if str(number)[0] == "1":
        break
print(number)
