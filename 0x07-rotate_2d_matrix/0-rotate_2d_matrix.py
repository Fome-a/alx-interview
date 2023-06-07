#!/usr/bin/python3
"""function to rotate a matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotate a matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix
