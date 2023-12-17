# мне кажется, что либо в формулировке задания, либо в тесте есть ошибка. Решение удовлетворяет тесту.
index_number = -1
summ = 0
while True:
    index_number += 1
    summ += int(input())
    if summ >= 10:
        print(index_number)
        break
