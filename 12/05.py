code_lines_list = list()
for _ in range(int(input()[1::])):
    code_line = input()
    if "#" in code_line:
        comment_index = code_line.find("#")
        code_line = code_line[:comment_index:]
    code_line = code_line.rstrip()
    code_lines_list.append(code_line)
for line in code_lines_list:
    print(line)