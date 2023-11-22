def matrix(n: int = 1, m: int = None, a=0):
    if m is None:
        m = n
    result = list()
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(a)
    return result


print(matrix())
print(matrix(2))
print(matrix(3, 2))
print(matrix(4, 5, 9))

rows = matrix()
for row in rows:
    print(*row)

rows = matrix(2, 3, "flop")
for row in rows:
    print(*row)