from random import choice
password_chars = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def generate_password(lenght):
    allowed_chars = list(password_chars)
    password = ""
    for i in range(lenght):
        rand_char = choice(allowed_chars)
        password += rand_char
        allowed_chars.remove(rand_char)
    return password


def main(amount, lenght):
    result = list()
    for i in range(amount):
        result.append(generate_password(lenght))
    return result
