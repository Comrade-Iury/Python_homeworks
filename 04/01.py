days = 0
temp = float(input("Вводите максимальную температуру за день: "))
while temp < 22:
    days += 1
    temp = float(input())
else:
    print(days//7)
