sign = ""
number_max = 1000
number_min = 0
number_last = 0
print('NumberGuesser the Game \n Think of a number in range from 1 to 1000. \n Print just "<", ">" or "=".')

for ix in range(10):
    number_last = (number_max + number_min) // 2
    sign = input("Is your number " + str(number_last) + "? ")
    if sign == "=":
        break
    elif sign == "<":
        number_max = number_last
    elif sign == ">":
        number_min = number_last

if sign == "=":
    print("Game over, your number is " + str(number_last) + "!")
else:
    print("Sorry, but I can`t guess your number in 10 steps!")
input()
