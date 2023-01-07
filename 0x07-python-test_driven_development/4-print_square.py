#!/usr/bin/python3

""" This module contains a function for printing a square """


def print_square(size):
    """ A function that prints a square """

    i = 1

    if (not isinstance(size, int)) or (size is None):

        raise TypeError("size must be an integer")

    if (type(size) is float) and (size < 0):

        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
        return

    while i <= size:
        print("{}".format("#" * size))

        i += 1
