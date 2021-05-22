def copy_matrix(matrix):
    new = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new.append(new_row)
    return new

def matrix_sub(matrix1, matrix2):
    tmp = copy_matrix(matrix1)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            tmp[i][j] -= matrix2[i][j]
    return tmp

def matrix_add(matrix1, matrix2):
    tmp = copy_matrix(matrix1)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            tmp[i][j] += matrix2[i][j]
    return tmp

def matrix_zeros(x, y):
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(0)
        matrix.append(row)
    return matrix

def diagonal_to_square_matrix(vector):
    tmp = matrix_zeros(len(vector), len(vector))
    for i in range(len(vector)):
        tmp[i][i] = vector[i]
    return tmp