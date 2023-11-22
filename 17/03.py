temp = [0, -1, 10, 7, -5]
print(id(temp))

temp.sort()                 # .sort() сортитует список
new_temp = sorted(temp)     # sorted(arr) создаёт новый отсортированный список

print(temp)
print(new_temp)             # писки выглядят одинаково

print(id(temp))
print(id(new_temp))         # адрес второго списка изменился
