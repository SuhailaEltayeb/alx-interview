#!/usr/bin/python3
"""
Solving Rotate 2D matrix Dialemme
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate 2D matrix

    Args:
        matrix: 2D matrix
    """
    n = len(matrix)

    for x in range(n):
        for y in range(x, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for row in matrix:
        row.reverse()
