def mirror(arr):
    mirrored_part = arr.copy()
    mirrored_part.reverse()
    arr.extend(mirrored_part)
