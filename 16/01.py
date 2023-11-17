def main():
    pi = 3.14159
    radius = int(input("Enter radius: "))
    print(circle_length(pi, radius))
    print(circle_area(pi, radius))


def circle_length(pi, radius):
    return pi * radius * 2


def circle_area(pi, radius):
    return pi * radius ** 2


main()