result = list()
for _ in range(int(input())):
    result.append(input())

for _ in range(len(result) - 1):
    for i in range(len(result) - 1):
        if len(result[i]) < len(result[i+1]):
            continue
        if len(result[i]) > len(result[i+1]):
            save = result[i]
            result[i] = result[i+1]
            result[i+1] = save
            continue
        if result[i] > result[i+1]:
            save = result[i]
            result[i] = result[i + 1]
            result[i + 1] = save

print(result)
