#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Multiply the values in a dictionary by 2

    Args:
        a_dictionary: the dictionary

    Returns:
        a new dictionary containing the multiplication result

    """

    new_dict = {k: 2 * v for (k, v) in a_dictionary.items()}

    return new_dict
