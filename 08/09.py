log_lines = list()
for _ in range(int(input())):
    new_line = input()
    if new_line[:4:] == "####":
        continue
    elif new_line[:2:] == "%%":
        new_line = new_line[2::]
    log_lines.append(new_line)

for line in log_lines:
    print(line)