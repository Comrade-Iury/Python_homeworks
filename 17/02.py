def count_food(indexes):
    sum = 0
    for i in indexes:
        sum += daily_food[i - 1]
    return sum


daily_food = [0, 150, 150]
print(count_food([1]))

print(count_food([2, 3]))