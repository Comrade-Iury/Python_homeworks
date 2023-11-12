def find_mountain(heightsMap):
    for row in heightsMap:
        for column in row:




a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])