houses_1 = set()
houses_2 = set()

while True:
    house = input()
    if house == "":
        break
    houses_1.add(house)
while True:
    house = input()
    if house == "":
        break
    houses_2.add(house)
if houses_1 & houses_2:
    print(houses_1 & houses_2)
else:
    print("Empty")
