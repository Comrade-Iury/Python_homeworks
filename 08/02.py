word_1 = input()
word_2 = input()
bulls = cows = 0
for char in word_2[::]:
    if char in word_1:
       cows += 1
for i in range(len(word_1)):
    if word_1[i] == word_2[i]:
        bulls += 1
        cows -= 1
print(bulls, cows)
