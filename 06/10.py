canteen_menu = set()

for _ in range(int(input())):
    canteen_menu.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        canteen_menu.discard(input())

for dish in canteen_menu:
    print(dish)