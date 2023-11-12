def number_to_words(n):
    ones = n % 10
    tens = n // 10
    hundred = n // 100

    if ones == 1:
        ones = "one"
    elif ones == 2:
        ones = "two"
    elif ones == 3:
        ones = "three"
    elif ones == 4:
        ones = "four"
    elif ones == 5:
        ones = "five"
    elif ones == 6:
        ones = "six"
    elif ones == 7:
        ones = "seven"
    elif ones == 8:
        ones = "eight"
    elif ones == 9:
        ones = "nine"

    if 0 < n < 9:
        print(ones)

    if n == 10:
        print("ten")
    if n == 11:
        print("eleven")
    if n == 12:
        print("twelve")


    if 12 < n < 20:
        if ones == 1:
            ones = ""
        if ones == 2:
            ones = "Две"
        elif ones == 4:
            ones = "Четыр"
        elif ones == 5:
            ones = "Пят"
        elif ones == 6:
            ones = "Шест"
        elif ones == 7:
            ones = "Сем"
        elif ones == 8:
            ones = "Восем"
        elif ones == 9:
            ones = "Девят"
        print(ones + "надцать")
    if n > 20:
        if tens == 0:
            tens = ""
        elif tens == 2:
            tens = "Двадцать"
        elif tens == 3:
            tens = "Тридцать"
        elif tens == 4:
            tens = "Сорок"
        elif tens == 5:
            tens = "Пятьдесят"
        elif tens == 6:
            tens = "Шестьдесят"
        elif tens == 7:
            tens = "Семьдесят"
        elif tens == 8:
            tens = "Восемьдесят"
        elif tens == 9:
            tens = "Девяносто"

        print(tens, ones)
    if n == 0:
        print("Ноль")


number_to_words(0)
number_to_words(6)
number_to_words(13)
number_to_words(25)
number_to_words(51)
number_to_words(900)
number_to_words(478)
