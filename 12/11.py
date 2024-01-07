rounds_list = list()
done_rounds_list = list()
for n in range(int(input())):
    rounds_list.append(input().split())

for i in range(len(rounds_list)):
    done_rounds_list.append(list())
    while len(rounds_list[i]) > 1:
        done_rounds_list[i].append(max(rounds_list[i][0], rounds_list[i][-1]))
        rounds_list[i].remove(max(rounds_list[i][0], rounds_list[i][-1]))
    else:
        done_rounds_list[i].append(rounds_list[i][0])
for game in done_rounds_list:
    if game != sorted(game, reverse=True):
        done_rounds_list[done_rounds_list.index(game)] = "НЕТ"
for game in done_rounds_list:
    if game == "НЕТ":
        print("НЕТ")
    else:
        print(*game)