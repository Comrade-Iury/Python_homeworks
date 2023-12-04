numbers = input().split()
borders = input().split()
sum = 0
for i in range(len(numbers)):
    if int(borders[0]) <= i <= int(borders[1]):
        sum += int(numbers[i])
print(sum)