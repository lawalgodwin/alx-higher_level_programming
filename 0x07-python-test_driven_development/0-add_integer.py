#!/usr/bin/python3

"""
@author: Godwin Lawal
Integer addition module

"""


def add_integer(a, b=98):
    """Add to numbers together
    returns the result of the addition
    """

    if type(a) not in {int, float} or a is None:
        raise TypeError("a must be an integer")

    if type(b) not in {int, float} or b is None:
        raise TypeError("b must be an integer")

    a, b = (int(a), int(b))

    return (a + b)
