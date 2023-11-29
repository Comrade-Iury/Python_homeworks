soldiers = list()
for _ in range(int(input())):
    soldiers.append(input())

punish_number = int(input())
repeat_number = int(input())
shift = 1

for _ in range(repeat_number):
    shift = 1
    for i in range(1, len(soldiers) + 1):
        if i % punish_number == 0:
            soldiers.remove(soldiers[i-shift])
            shift += 1

for i in soldiers:
    print(i)