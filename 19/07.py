def same_by(characteristic, objects):
    result = set()
    for obj in objects:
        result.add(characteristic(obj))
    if len(result) == 1 or len(result) == 0:
        return True
    return False
