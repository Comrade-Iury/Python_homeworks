def same_by(characteristic, objects):
    if len(objects) == 0:
        return True

    result = set()
    for obj in objects:
        result.add(characteristic(obj))

    if len(result) == 1:
        return True
    
    return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

print(same_by(lambda x: x % 2, []))