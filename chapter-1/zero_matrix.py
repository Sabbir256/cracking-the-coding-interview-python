"""
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

def set_zeros(matrix: list[list]) -> None:
    first_col_has_zero: bool = False
    first_row_has_zero: bool = False

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            first_row_has_zero = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    if first_col_has_zero:
        nullify_column(matrix, 0)
    if first_row_has_zero:
        nullify_row(matrix, 0)

    for layer in matrix:
        print(layer)

def nullify_row(matrix: list[list[int]], row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_column(matrix: list[list[int]], col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


if __name__ == '__main__':
    set_zeros([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

