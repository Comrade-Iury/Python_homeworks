word = input()
new_word = input()
while word[-1] == new_word[0]:
    word = new_word
    new_word = input()
else:
    print(new_word)
