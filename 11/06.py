items = int(input())
recipe = list()
for ix in range(items):
    recipe.append(input())
[recipe.remove(ix) for ix in recipe if "лук" in ix]

print(str(recipe))
