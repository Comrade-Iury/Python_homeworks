city_1 = input("Введите город куда поехать в июле")
city_2 = input("Введите город куда поехать в августе")
if (city_1 == "Тула" or city_2 == "Пенза") and city_1 != city_2 and not(city_1 == "Тула" and city_2 =="Пенза"):
	print("да")
else: 
	print("нет")
