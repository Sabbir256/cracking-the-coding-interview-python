"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(matrix: list[list]) -> bool:
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    rows: int = len(matrix)

    for layer in range(rows // 2):
        first: int = layer
        last: int = rows - 1 - layer

        for i in range(first, last):
            offset: int = i - first
            top: int = matrix[first][i] # save top

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    for layer in matrix:
        print(layer)
    return True


if __name__ == '__main__':
    assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) is True
    assert rotate_matrix([[]]) is False

# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
