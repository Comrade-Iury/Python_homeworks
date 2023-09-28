word = input()
char_number = int(input()) - 1
if char_number < len(word):
    print(word[char_number])
else:
    print("Error")

