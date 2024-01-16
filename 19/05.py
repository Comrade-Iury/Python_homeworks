def ask_password(login, password, success, failure):
    login, password = login.lower(), password.lower()
    vowels = "aeiuyo"
    consonants = "bcdfghjklmnpqrstvwxz"
    errors = list()
    number_of_vowels = 0
    login_consonants, password_consonants = list(), list()
    for char in password:
        if char in vowels:
            number_of_vowels += 1
        else:
            password_consonants.append(char)
    if number_of_vowels != 3:
        errors.append(1)
    for char in login:
        if char in consonants:
            login_consonants.append(char)
    if login_consonants != password_consonants:
        errors.append(2)

    if errors:
        if sum(errors) == 1:
            failure(login, "Wrong number of vowels")
        elif sum(errors) == 2:
            failure(login, "Wrong consonants")
        else:
            failure(login, "Everything is wrong")
    else:
        success(login)


def right_password(login):
    print(f"Привет, {login}!")


def wrong_password(login, error_message):
    print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error_message.upper()}.")


def main(login, password):
    ask_password(login, password, right_password, wrong_password)
