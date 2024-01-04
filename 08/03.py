allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234566789_"
login = input()
for char in login:
    if char not in allowed_chars:
        print("Неверный символ:", char )
        break
else:
    print("OK")