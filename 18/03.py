def encrypt_caesar(msg, shift=3):
    if shift > 32 or shift < 0:
        return "invalid shift"
    result = ""

    for char in msg:
        char = ord(char)
        if 1040 <= char <= 1071:
            if char + shift > 1071:
                char = char + shift - 32
            else:
                char += shift
        if 1072 <= char <= 1103:
            if char + shift > 1103:
                char = char + shift - 32
            else:
                char += shift
        result += chr(char)
    return result


def decrypt_caesar(msg, shift=3):
    if shift > 32 or shift < 0:
        return "invalid shift"
    result = ""

    for char in msg:
        char = ord(char)
        if 1040 <= char <= 1071:
            if char - shift < 1040:
                char = char - shift + 32
            else:
                char -= shift
        elif 1072 <= char <= 1103:
            if char - shift < 1073:
                char = char - shift + 32
            else:
                char -= shift
        result += chr(char)
    return result


print(encrypt_caesar("Да здравствует салат Цезарь!"))
print(decrypt_caesar("Зг кзугефхецих фгогх Щикгуя!"))

print(encrypt_caesar("И ты, Брут!?", 5))
print(decrypt_caesar("Н ча, Жхшч!?", 5))
