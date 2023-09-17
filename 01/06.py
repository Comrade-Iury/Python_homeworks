answer1 = input('Вы студент?')
answer2 = input('Едите ли вы сырки каждый день?')

student = ("да" in answer1)
cheese = ("да" in answer2)
notstudent = ("нет" in answer1)
notcheese = ("нет" in answer2)

if student:
    if cheese:
        print("Вы счастливый студент!")
    elif notcheese:
        print("Продолжайте учиться, и удача улыбнётся вам!")
elif notstudent:
    if cheese:
        print("Вы счастливый человек!")
    elif notcheese:
        print("У вас ещё всё впереди, главное - не останавливаться!")
else:
    print('Недопустимый ответ, вводите только "да" или "нет". ')

