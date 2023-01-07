#!/usr/bin/python3

""" Matrix division module """


def matrix_divided(matrix, div):
    """Divide elements of a matrix by a divisor
    Args:
        matrix: the matrix
        div: The divisor
    Returns:
        a new matrix with elements rounded to 2dp at most
    """

    new_matrix = []

    typerror = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in {int, float}:
        raise TypeError(r"div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (matrix is None) or (len(matrix) == 0) or (len(matrix[0]) == 0):
        raise TypeError(typerror)

    for i in range(len(matrix) - 1):

        if not isinstance(matrix[i], list):
            raise TypeError(typerror)

    for row in matrix:
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:

        new_row = []

        for col in row:

            if type(col) not in {int, float}:

                raise TypeError(typerror)

            new_row.append(round(col/div, 2))

        new_matrix.append(new_row)

    return (new_matrix)
