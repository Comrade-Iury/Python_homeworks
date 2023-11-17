people = dict()
for i in range(int(input())):
    number, name = input().split(" ")
    if name not in people:
        people[name] = number
    else:
        people[name] += " " + str(number)

for i in range(int(input())):
    print(people.get(input(), "Нет в телефонной книге."))