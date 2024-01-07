excluded_char = input()
words_list = input().split()
excluded_words_list = list()
for word in words_list:
    if excluded_char in word.lower():
        excluded_words_list.append(word)

print(*excluded_words_list)