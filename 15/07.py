def find_mountain(heights_map):
    max_height = 0
    for row in heights_map:
        for column in row:
            if column > max_height:
                max_height = column
    i, j = 0, 0
    for row in heights_map:
        for column in row:
            if column == max_height:
                return [i, j]
            j += 1
        i += 1
        j = 0


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])

