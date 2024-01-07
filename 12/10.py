words = input()
count = 0
for char in words:
    if char != " " and char != "\t":
        count += 1
print(count)