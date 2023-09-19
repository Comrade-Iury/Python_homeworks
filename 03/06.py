check = 0
while check == 0:
    password_1 = input("Enter your password: ")
    password_2 = input("Enter same password again: ")
    if len(password_1) < 8:
        print("Your password is too short.")
    elif "123" in password_1:
        print("Your password is too simple.")
    elif password_1 != password_2:
        print("Second password is not the same!")
    else:
        check = 1
print("Your password saved!")
