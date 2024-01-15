def solve(coefficients):
    if len(coefficients) == 1:
        return {0}
    for i in range(len(coefficients)):
        coefficients[i] = int(coefficients[i])
    if len(coefficients) == 2:
        return {- coefficients[1] / coefficients[0]}
    if len(coefficients) == 3:
        a, b, c = coefficients[::]
        d = (b ** 2) - 4 * a * c
        x1 = (-b + d ** 0.5) / (a * 2)
        x2 = (-b - d ** 0.5) / (a * 2)
        return {x1, x2}


print(*solve(input("Введите коэффициенты уравнения через пробел: ").split()))

