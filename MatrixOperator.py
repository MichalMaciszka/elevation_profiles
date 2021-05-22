from math import sin


class MatrixOperator:

    def __init__(self, index):
        self.d = int(index % 10)
        index /= 10
        self.c = int(index % 10)
        index /= 10
        self.e = int(index % 10)
        index /= 10
        self.f = int(index % 10)
        self.n = 900 + 10 * self.c + self.d

    def create_matrix(self, a1, a2, a3):
        matrix = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == j:
                    row.append(a1)
                elif i - 1 <= j <= i + 1:
                    row.append(a2)
                elif i - 2 <= j <= i + 2:
                    row.append(a3)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

    def create_matrix_a(self):
        return self.create_matrix(self.e + 5, -1, -1)

    def create_vector_b(self):
        b = []
        for i in range(self.n):
            b.append(sin(i * (self.f + 1)))
        return b

    def create_matrix_c(self):
        return self.create_matrix(3, -1, -1)

    def copy_matrix(self, matrix):
        new = []
        for row in matrix:
            new_row = []
            for element in row:
                new_row.append(element)
            new.append(new_row)
        return new

    def matrix_sub(self, matrix1, matrix2):
        tmp = self.copy_matrix(matrix1)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] -= matrix2[i][j]
        return tmp

    def matrix_add(self, matrix1, matrix2):
        tmp = self.copy_matrix(matrix1)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] += matrix2[i][j]
        return tmp

    def matrix_zeros(self, x, y):
        matrix = []
        for i in range(y):
            row = []
            for j in range(x):
                row.append(0)
            matrix.append(row)
        return matrix

    def diagonal_to_square_matrix(self, vector):
        tmp = self.matrix_zeros(len(vector), len(vector))
        for i in range(len(vector)):
            tmp[i][i] = vector[i]
        return tmp
