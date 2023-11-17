def main():
    print("Enter p and q from x^2 + px + q = 0:")
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(larger_root(p, q))
    print(smaller_root(p, q))


def larger_root(p, q):
    a, b, c = 1, p, q
    return (- b + discriminant(a, b, c) ** (1 / 2)) / 2


def smaller_root(p, q):
    a, b, c = 1, p, q
    return (- b - discriminant(a, b, c) ** (1 / 2)) / 2


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


main()

