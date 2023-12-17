cat_is_here = False
for _ in range(int(input())):
    word = input()
    if "Кот" in word or "кот" in word:
        cat_is_here = True
if cat_is_here:
    print("МЯУ")
else:
    print("НЕТ")
