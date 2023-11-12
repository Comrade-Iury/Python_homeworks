def average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


print(average([1, 2, 3, 4, 5]))
print(average([-5, 2]))
print(average([]))