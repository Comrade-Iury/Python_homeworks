a = int(input())
b = int(input())
for num in range(a, b+1):
    if not(num % 3) and not(num % 5):
        print("FizzBuzz")
        continue
    if not(num % 3):
        print("Fizz")
        continue
    if not(num % 5):
        print("Buzz")
        continue
    print(num)