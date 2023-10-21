num = int(input())
check = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        check += i
if check == num + 1:
    print("\n Yes")
else:
    print("\n No")


