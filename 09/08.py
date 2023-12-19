soup_list = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
soup_number = 0
for i in range(int(input())):
    print(soup_list[soup_number])
    soup_number += 1
    if soup_number > 4:
        soup_number = 0