called_once = set()
called_twice = set()
repeat_count = 0
for _ in range(int(input())):
    name = input()
    if name not in called_once:
        called_once.add(name)
    else:
        called_twice.add(name)
        repeat_count += 1


print(repeat_count + len(called_twice))