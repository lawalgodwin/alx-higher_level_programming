#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """A two tuples and return a tuple containing the result
    Args:
        tuple_a: The first tuple
        tuple_b: The second tuple
    Returns:
        Returns a tuple containing the result
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        tuple_b = tuple_b[0], 0

    result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

    return (result)
