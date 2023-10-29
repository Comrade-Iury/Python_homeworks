word_min = input()
word_max = ""
while True:
    word_new = input()
    if word_new == "stop" or word_new == "стоп":
        break
    elif len(word_new) < len(word_min):
        word_min = word_new
    elif len(word_new) > len(word_max):
        word_max = word_new
if set(word_min) < set(word_max):
    print("Yes")
else:
    print("No")

