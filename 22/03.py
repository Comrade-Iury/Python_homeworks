from random import choice
password_chars = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def generate_password(lenght):
    password = ""
    for i in range(lenght):
        password += choice(password_chars)
    return password


def main(amount, lenght):
    result = list()
    for i in range(amount):
        result.append(generate_password(lenght))
    return result
