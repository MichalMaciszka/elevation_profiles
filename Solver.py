import time


class Solver:
    def __init__(self, a, b, matrix_operator, vector_operator):
        self.a = a
        self.b = b
        self.matrix_operator = matrix_operator
        self.vector_operator = vector_operator

    def dot_product(self, a, b):
        copy_a = self.matrix_operator.copy_matrix(a)
        copy_b = self.vector_operator.copy_vector(b)
        m = len(copy_a)
        n = len(copy_a[0])
        c = self.vector_operator.vector_zeros(m)

        for i in range(m):
            for j in range(n):
                c[i] += copy_a[i][j] * copy_b[j]
        return c

    def lu_factor(self):
        start_time = time.time()
        m = len(self.a)

        matrix_a = self.matrix_operator.copy_matrix(self.a)
        matrix_l = self.matrix_operator.diagonal_to_square_matrix(self.vector_operator.vector_ones(m))
        matrix_u = self.matrix_operator.matrix_zeros(m, m)

        vector_b = self.vector_operator.copy_vector(self.b)
        vector_x = self.vector_operator.vector_ones(m)
        vector_y = self.vector_operator.vector_zeros(m)

        # pivot
        for k in range(m):
            max_row = k
            max_val = abs(matrix_a[k][k])
            for i in range(k + 1, m):
                if abs(matrix_a[i][k]) > max_val:
                    max_row = i
                    max_val = matrix_a[i][k]
            if max_row != k:
                matrix_a[k], matrix_a[max_row] = matrix_a[max_row], matrix_a[k]

        # LUx = b
        for i in range(m):
            for j in range(i + 1):
                matrix_u[j][i] += matrix_a[j][i]
                for k in range(j):
                    matrix_u[j][i] -= matrix_l[j][k] * matrix_u[k][i]
            for j in range(i + 1, m):
                for k in range(i):
                    matrix_l[j][i] -= matrix_l[j][k] * matrix_u[k][i]
                matrix_l[j][i] += matrix_a[j][i]
                matrix_l[j][i] /= matrix_u[i][i]

        # Ly = b
        for i in range(m):
            val = vector_b[i]
            for j in range(i):
                val -= matrix_l[i][j] * vector_y[j]
            vector_y[i] = val / matrix_l[i][i]

        # Ux = y
        for i in range(m - 1, -1, -1):
            val = vector_y[i]
            for j in range(i + 1, m):
                val -= matrix_u[i][j] * vector_x[j]
            vector_x[i] = val / matrix_u[i][i]

        residuum = self.vector_operator.vectors_sub(self.dot_product(matrix_a, vector_x), vector_b)
        norm = self.vector_operator.norm(residuum)
        t = time.time() - start_time
        print("-----LU-----")
        print("time: ", t)
        print("Norma z residuum: ", norm)
        # print(vector_x)
        print()
        return vector_x
