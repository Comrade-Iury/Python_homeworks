def swap(first, second):
    first_copy = first[:]
    second_copy = second[:]
    for i in range(len(first)):
        if len(second) <= len(first):
            if i < len(second):
                second[i] = first_copy[i]
            else:
                second[i].append(first_copy[i])
        else:
            second[i] = first_copy[i]
    for i in range(len(second)):
        if len(first) <= len(second):
            if i < len(first):
                first[i] = second_copy[i]
            else:
                first.append(second_copy[i])
        else:
            first[i] = second_copy[i]
    while len(first) > len(second_copy):
        first.remove(first[-1])
    while len(second) > len(first_copy):
        second.remove(second[-1])
