summ = 0
for i in range(1, int(input()) + 1):
    if i % 2 != 0:
        summ += int(input())
    else:
        summ -= int(input())
print(summ)