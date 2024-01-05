words_list = input().upper().split()
for word in words_list:
    word_splitted = list(word)
    for i in range(len(word_splitted) - 1):
        word_splitted[i] = word_splitted[i] + "-"
    word = "".join(word_splitted)
    print(word, end=" ")
