def solve(*coefficients):
    coefficients = list(coefficients)
    if len(coefficients) > 3 or len(coefficients) == 0:
        return "None"
    if len(coefficients) == 1:
        return 0
    if len(coefficients) == 2:
        return - coefficients[1] / coefficients[0]
    if len(coefficients) == 3:
        a, b, c = coefficients[::]
        d = (b ** 2) - 4 * a * c
        x1 = (-b + d ** 0.5) / (a * 2)
        x2 = (-b - d ** 0.5) / (a * 2)
        return x1, x2


print(sorted(solve(1, -3, 2)))
print(solve(1, -3))
print(solve(-3))
print(solve())
print(solve(1, -3, 2, 5))



