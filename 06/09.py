fridge_food = set()
ingredients = set()
can_do_recipes = set()
for _ in range(int(input())):
    fridge_food.add(input())
for _ in range(int(input())):
    recipe_name = input()
    for _ in range(int(input())):
        ingredients.add(input())
    if ingredients <= fridge_food:
        can_do_recipes.add(recipe_name)
    ingredients.clear()

for recipe in can_do_recipes:
    print(recipe)