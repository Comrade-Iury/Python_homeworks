NAME = ""
VACATION_DATES = ""


def setup_profile(name, vacation_dates):
    global NAME, VACATION_DATES
    NAME, VACATION_DATES = name, vacation_dates


def print_application_for_leave():
    print(f"Заявление на отпуск в период {VACATION_DATES}. {NAME}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {NAME}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {VACATION_DATES} моим заместителем назначается {to_whom}. {NAME}")


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")