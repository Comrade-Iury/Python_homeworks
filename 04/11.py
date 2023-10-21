count = int(input())
average = int(input())
print(0)
for i in range(count - 1):
    number = int(input())
    average = (average + number) / 2
    if number == average:
        print(0)
    elif number < average:
        print("<")
    elif number > average:
        print(">")


