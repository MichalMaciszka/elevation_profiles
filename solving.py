import vector, matrix

def lu_factor(a, b):
        m = len(a)

        matrix_a = matrix.copy_matrix(a)
        matrix_l = matrix.diagonal_to_square_matrix(vector.vector_ones(m))
        matrix_u = matrix.matrix_zeros(m, m)

        vector_b = vector.vector_operator.copy_vector(b)
        vector_x = vector.vector_ones(m)
        vector_y = vector.vector_zeros(m)

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