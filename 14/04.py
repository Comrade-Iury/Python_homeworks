def who_are_you_and_hello():
    right_name = False
    while not right_name:
        name = input()
        if name[0].isupper() and name[2::].islower() and name.isalpha():
            print(f"Привет, {name}!")
            right_name = True
