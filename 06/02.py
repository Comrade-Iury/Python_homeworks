cities = set()
count = int(input("Count of cities: "))
print("Input names of cities: \r")
for _ in range(count):
    cities.add(input())
new_city = {input("New city: ")}
if new_city < cities:
    print("Try another")
else:
    print("Ok")
