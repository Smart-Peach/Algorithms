def matrix_multiply_classic(a, b):
    assert len(a[0]) == len(b)
    res = [[0 for j in range(len(a))] for i in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res


def matrix_addition(a, b, k):
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    res = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] + k * b[i][j]
    return res


def sub_matrix(matrix, width, height, ind1, ind2):
    d = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            d[i][j] = matrix[i + ind1][j + ind2]
    return d


def matrix_cutting(matrix, middle_columns, middle_strings):
    matrix_width = len(matrix[0])
    matrix_height = len(matrix)

    width = matrix_width - middle_columns
    height = matrix_height - middle_strings

    a = sub_matrix(matrix, middle_columns, middle_strings, 0, 0)
    b = sub_matrix(matrix, width, middle_strings, 0, middle_columns)
    c = sub_matrix(matrix, middle_columns, height, middle_strings, 0)
    d = sub_matrix(matrix, width, height, middle_strings, middle_columns)

    return a, b, c, d


def matrix_copying(res, matrix, ind1, ind2):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[i + ind1][j + ind2] = matrix[i][j]


def matrix_gluing(a, b, c, d):
    assert len(a) == len(b)
    assert len(c) == len(d)
    assert len(a[0]) == len(c[0])
    assert len(b[0]) == len(d[0])

    width = len(a[0]) + len(b[0])
    height = len(a) + len(c)

    res = [[0 for j in range(width)] for i in range(height)]

    matrix_copying(res, a, 0, 0)
    matrix_copying(res, b, 0, len(a[0]))
    matrix_copying(res, c, len(a), 0)
    matrix_copying(res, d, len(a), len(a[0]))

    return res


def matrix_multiply_8recursions(x, y):
    assert len(x[0]) == len(y)
    if len(y) == 1:
        return matrix_multiply_classic(x, y)
    middle_strings_x = len(x) // 2
    middle_columns_x = len(x[0]) // 2
    middle_strings_y = len(y) // 2
    middle_columns_y = len(y[0]) // 2

    a, b, c, d = matrix_cutting(x, middle_columns_x, middle_strings_x)
    e, f, g, h = matrix_cutting(y, middle_columns_y, middle_strings_y)

    step1 = matrix_addition(matrix_multiply_8recursions(a, e), matrix_multiply_8recursions(b, g), 1)
    step2 = matrix_addition(matrix_multiply_8recursions(a, f), matrix_multiply_8recursions(b, h), 1)
    step3 = matrix_addition(matrix_multiply_8recursions(c, e), matrix_multiply_8recursions(d, g), 1)
    step4 = matrix_addition(matrix_multiply_8recursions(c, f), matrix_multiply_8recursions(d, h), 1)

    res = matrix_gluing(step1, step2, step3, step4)
    return res


def matrix_multiplication_strassen(x, y):
    assert len(x[0]) == len(y)
    if len(y) == 1:
        return matrix_multiply_classic(x, y)
    middle_strings_x = len(x) // 2
    middle_columns_x = len(x[0]) // 2
    middle_strings_y = len(y) // 2
    middle_columns_y = len(y[0]) // 2

    a, b, c, d = matrix_cutting(x, middle_columns_x, middle_strings_x)
    e, f, g, h = matrix_cutting(y, middle_columns_y, middle_strings_y)

    p1 = matrix_multiplication_strassen(a, matrix_addition(f, h, -1))
    p2 = matrix_multiplication_strassen(matrix_addition(a, b, 1), h)
    p3 = matrix_multiplication_strassen(matrix_addition(c, d, 1), e)
    p4 = matrix_multiplication_strassen(d, matrix_addition(g, e, -1))
    p5 = matrix_multiplication_strassen(matrix_addition(a, d, 1), matrix_addition(e, h, 1))
    p6 = matrix_multiplication_strassen(matrix_addition(b, d, -1), matrix_addition(g, h, 1))
    p7 = matrix_multiplication_strassen(matrix_addition(a, c, -1), matrix_addition(e, f, 1))

    q1 = matrix_addition(matrix_addition(matrix_addition(p5, p4, 1), p2, -1), p6, 1)
    q2 = matrix_addition(p1, p2, 1)
    q3 = matrix_addition(p3, p4, 1)
    q4 = matrix_addition(matrix_addition(matrix_addition(p1, p5, 1), p3, -1), p7, -1)

    res = matrix_gluing(q1, q2, q3, q4)
    return res


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix_multiply_classic(a, a))
print(matrix_multiply_8recursions(a, a))
print(matrix_multiplication_strassen(a, a))
