import random
def make_bingo():
    bingo_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(5):
        for j in range(5):
            bingo_matrix[i][j] = random.randint(1, 75)
    bingo_matrix[2][2] = 0
    for i in range(len(bingo_matrix)):
        bingo_matrix[i] = tuple(bingo_matrix[i])
    return tuple(bingo_matrix)
