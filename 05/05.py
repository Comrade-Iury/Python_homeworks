cat_is_here = False
order_number = 0
while True:
    order_number += 1
    word = input()
    if "Кот" in word or "кот" in word:
        cat_is_here = True
        break
    if word == "СТОП":
        break
if cat_is_here:
    print(order_number)
else:
    print("-1")
