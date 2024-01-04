letters = "ABCDEFGH"
numbers = "87654321"
count = int(input())
if count > 9:
    print("Wrong input")
else:
    for i in range(count):
        for j in range(count):
            print(letters[j] + numbers[-(count - i)], end=" ")
        print()