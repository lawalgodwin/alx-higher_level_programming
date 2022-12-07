#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """A function that sqaures the elements of a given matrix

    Args:
        matrix: The matrix

    Returns:
        Returns a new matrix with the result.
    """
    new_matrix = []

    for i in range(len(matrix)):

        new_matrix.append(list(map(lambda x: x**2, matrix[i])))

    return new_matrix


if __name__ == '__main__':

    square_matrix_simple()
