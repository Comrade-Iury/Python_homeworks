word_1 = input()
word_2 = input()
bulls = cows = 0
for char_1 in word_1[::]:
    for char_2 in word_2[::]:
        if char_1 == char_2:
            bulls += 1
            char_1 = ""
            char_2 = ""
    else:
        continue
print(word_1, word_2,  bulls)
