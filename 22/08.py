from random import choice
lowercase = "abcdefghijkmnpqrstuvwxyz"
uppercase = lowercase.upper()
digits = "23456789"
password_chars = lowercase + uppercase + digits


def generate_password(lenght):
    is_allowed = False
    while not is_allowed:
        allowed_chars = list(password_chars)
        password = ""
        for i in range(lenght):
            rand_char = choice(allowed_chars)
            password += rand_char
            allowed_chars.remove(rand_char)
        if (set(password) & set(lowercase)) and (set(password) & set(uppercase)) and (set(password) & set(digits)):
            is_allowed = True
    return password


def main(amount, lenght):
    result = list()
    for i in range(amount):
        result.append(generate_password(lenght))
    return result
