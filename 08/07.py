result = ""
for i in range(int(input())):
    line = input()
    if "кот" in line:
        result = result + f'{i+1} {line.index("кот")+1} \n'
print(result)
