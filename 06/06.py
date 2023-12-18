books_in_library = set()

library_count = int(input())
list_count = int(input())

for _ in range(library_count):
    books_in_library.add(input())
for _ in range(list_count):
    if input() in books_in_library:
        print("YES")
    else:
        print("NO")

