def simple_map(transformation, values):
    for i in range(len(values)):
        values[i] = transformation(values[i])
    return values


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))