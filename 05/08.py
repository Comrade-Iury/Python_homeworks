word_with_cat = set()
word = ""
order_number = 0
while word != "СТОП":
    order_number += 1
    word = input()
    if "Кот" in word or "кот" in word:
        word_with_cat.add(order_number)
if word_with_cat:
    print(len(word_with_cat), min(word_with_cat))
else:
    print("0 -1")
