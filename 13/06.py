words_list = input().split()
words_dict = dict()
for word in words_list:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1
    print(words_dict[word], end=" ")
