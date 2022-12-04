#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers
    Args:
        matrix: The matrix to be printed

    Returns:
        returns None
    """
    if not(matrix):
        print("--")
        return

    num_of_rows = len(matrix)

    for row in matrix:
        for col in row:
            if (col == row[-1]):
                print("{:d}".format(col), end='')
            else:
                print("{:d}".format(col), end=" ")
        print()
