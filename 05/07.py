war_with = "Евразия"
peace_with = "Остазия"
for _ in range(int(input())):
    command = input()
    if command == "С кем война?":
        print(war_with)
        continue
    if command == "С кем мир?":
        print(peace_with)
        continue
    if command == "Меняем":
        war_with, peace_with = peace_with, war_with
