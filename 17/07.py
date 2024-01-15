def transpose(matrix):
    copied_matrix = list()
    for i in range(len(matrix)):
        copied_matrix.append([])
        for j in range(len(matrix)):
            copied_matrix[i].append(matrix[i][j])

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix[j][i] = copied_matrix[i][j]
