from sys import stdin
words_list = list()
sum_list = list()
words_dict = dict()
for line in stdin:
    words_list.append(line.strip())
for word in words_list:
    word_sum = 0
    for char in word:
        word_sum += ord(char.upper()) - ord("A") + 1
    sum_list.append(word_sum)
for i in range(len(words_list)):
    words_dict[words_list[i]] = sum_list[i]
words_dict = sorted(sorted(words_dict.items(), key=lambda elem: elem[0]), key=lambda elem: elem[1])
for item in words_dict:
    print(item[0])
