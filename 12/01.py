result = ""
for i in range(int(input())):
    new_string = input()
    if "кот" in new_string:
        result += f"{i + 1} {new_string.find('кот') + 1} \n"
print(result)
