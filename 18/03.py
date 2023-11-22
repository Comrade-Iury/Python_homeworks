def encrypt_caesar(msg, shift=3):
    result = ""
    msg = msg[::]

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


def decrypt_caesar(msg, shift=-3):
    result = ""
    msg = msg[::]

    for char in msg:
        char = ord(char)
        if 1040 <= char <= 1071:
            if char + shift < 1040:
                char = char + shift + 32
            else:
                char += shift
        if 1072 <= char <= 1103:
            if char + shift < 1072:
                char = char + shift + 32
            else:
                char += shift
        result += chr(char)
    return result


print(encrypt_caesar("Да здравствует салат Цезарь!"))
print(decrypt_caesar("Зг кзугефхецих фгогх Щикгуя!"))