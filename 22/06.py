from random import choice
lowercase = "abcdefghijkmnpqrstuvwxyz"
uppercase = lowercase.upper()
digits = "23456789"
password_chars = lowercase + uppercase + digits


def generate_password(lenght):
    is_allowed = False
    while not is_allowed:
        password = ""
        for i in range(lenght):
            password += choice(password_chars)
        if (set(password) & set(lowercase)) and (set(password) & set(uppercase)) and (set(password) & set(digits)):
            is_allowed = True
    return password


def main(amount, lenght):
    result = list()
    for i in range(amount):
        result.append(generate_password(lenght))
    return result
