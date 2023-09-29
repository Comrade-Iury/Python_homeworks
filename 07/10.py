step = int(input())
phrase = input()
for char in phrase:
    new_char = ord(char) + step
    if ord(char) < 1040 or ord(char) > 1103:
        print(char, end="")
    elif 1072 <= ord(char) <= 1103:
        if new_char > 1103:
            print(chr(1072 + (new_char - 1104)), end="")
        else:
            print(chr(new_char), end="")
    else:
        if new_char > 1071:
            print(chr(1040 + (new_char - 1072)), end="")
        else:
            print(chr(new_char), end="")
