import vector
import matrix


def dot_product(a, b):
    copy_a = matrix.copy_matrix(a)
    copy_b = vector.copy_vector(b)
    m = len(copy_a)
    n = len(copy_a[0])
    c = vector.vector_zeros(m)

    for i in range(m):
        for j in range(n):
            c[i] += copy_a[i][j] * copy_b[j]
    return c


def lu_factor(a, b):
    m = len(a)

    matrix_a = matrix.copy_matrix(a)
    matrix_l = matrix.diagonal_to_square_matrix(vector.vector_ones(m))
    matrix_u = matrix.matrix_zeros(m, m)

    vector_b = vector.copy_vector(b)
    vector_x = vector.vector_ones(m)
    vector_y = vector.vector_zeros(m)

    # pivot
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(matrix_a[i][j]))
        if j != row:
            matrix_a[j], matrix_a[row] = matrix_a[row], matrix_a[j]
            vector_b[j], vector_b[row] = vector_b[row], vector_b[j]

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

    # residuum = vector.vectors_sub(dot_product(matrix_a, vector_x), vector_b)
    # norm = vector.norm(residuum)
    # print("-----LU-----")
    # print("Norma z residuum: ", norm)
    # print(vector_x)
    # print()
    return vector_x
