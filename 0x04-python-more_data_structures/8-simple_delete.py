#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """delete a given key in a dictionary

    Args:
        a_dictionary: The dictionary
        key: The specific key
    Returns:
        The updated dictionary
    """
    if key in a_dictionary:

        del a_dictionary[key]

        return a_dictionary

    return a_dictionary
