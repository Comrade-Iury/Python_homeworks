def month_name(num, lang):
    if lang == "en":
        if num == 1:
            num = "January"
        elif num == 2:
            num = "February"
        elif num == 3:
            num = "March"
        elif num == 4:
            num = "April"
        elif num == 5:
            num = "May"
        elif num == 6:
            num = "June"
        elif num == 7:
            num = "July"
        elif num == 8:
            num = "August"
        elif num == 9:
            num = "September"
        elif num == 10:
            num = "October"
        elif num == 11:
            num = "November"
        elif num == 12:
            num = "December"

    if lang == "ru":
        if num == 1:
            num = "Январь"
        elif num == 2:
            num = "Февраль"
        elif num == 3:
            num = "Март"
        elif num == 4:
            num = "Апрель"
        elif num == 5:
            num = "Иай"
        elif num == 6:
            num = "Июнь"
        elif num == 7:
            num = "Июль"
        elif num == 8:
            num = "Август"
        elif num == 9:
            num = "Сентябрь"
        elif num == 10:
            num = "Октябрь"
        elif num == 11:
            num = "Ноябрь"
        elif num == 12:
            num = "Декабрь"

    return num


print(month_name(3, "en"))
print(month_name(3, "ru"))