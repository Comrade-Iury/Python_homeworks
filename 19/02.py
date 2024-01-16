def simple_map(transformation, values):
    for i in range(len(values)):
        values[i] = transformation(values[i])
    return values
