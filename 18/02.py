def make_email(email, name, date, place="Нефтекамске"):
    return (f"To: {email} \n Здравствуйте, {name}! \n Были бы рады видеть вас на встрече начинающих программистов "
            f" в {place}, которая пройдет {date}.")


print(make_email(email="american-boi2023@mail.com", name="Семён", date="22.11.2023"))
print(make_email(email="sergei234567@yandex.ru", name="Сергей Васильевич", place="Уфе", date="22.11.2023"))
