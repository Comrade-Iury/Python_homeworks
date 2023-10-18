login = input("Type login: ")
email = input("Type email: ")

if "@" in login:
    print("Wrong login!")
elif not("@" in email):
    print("Wrong email!")
else:
    print("Great!")