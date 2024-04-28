#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The 2D matrix to rotate.

    Returns:
        None: The matrix is rotated in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


def print_matrix_in_columns(matrix):
    """
    Print the 2D matrix in column-by-column format.

    Args:
        matrix (list of list): The 2D matrix to print.
    """
    for row in matrix:
        print(" ".join(map(str, row)))


# Example usage:
if __name__ == "__main__":
    original_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in original_matrix:
        print(row)

    rotate_2d_matrix(original_matrix)

    print("\nMatrix after rotation (in columns):")
    print_matrix_in_columns(original_matrix)
