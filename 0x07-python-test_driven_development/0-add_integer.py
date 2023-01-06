# 0-add_integer.py

"""
@author: Godwin Lawal
My Adder module

"""


def add_integer(a, b=98):
    """Add to numbers together

    Agrs:
        a: The first  number (must be an integer)
        b: The second number (This is optional but must be an intteger)

    Returns:
        The result of the addition
    """

    if type(a) not in {int, float} or a is None:
        raise TypeError("a must be an integer")

    if type(b) not in {int, float} or b is None:
        raise TypeError("b must be an integer")

    a, b = (int(a), int(b))

    return (a + b)
