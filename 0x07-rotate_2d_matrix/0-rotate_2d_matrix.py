#!/usr/bin/python3
"""
Rotate 2D Matrix

Rotates a 2D matrix 90 degrees clockwise in-place.


"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The input 2D matrix.

    Returns:
        None
    """
    # Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
