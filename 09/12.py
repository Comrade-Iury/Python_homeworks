actual_summ = 0
problems = list()
positions_list = list()
first_line = input().split()
positions_number, summ = first_line[0], first_line[1]
for line in range(int(positions_number)):
    new_line = input().split()
    new_line[1] = new_line[1][1::]
    new_line[2] = new_line[2][1::]
    positions_list.append(new_line)

for position in positions_list:
    if int(position[0]) * int(position[1]) != int(position[2]):
        problems.append(positions_list.index(position) + 1)
    actual_summ += int(position[0]) * int(position[1])

if int(summ) - actual_summ:
    print(int(summ) - actual_summ)
    print(*problems)
else:
    print(0)
