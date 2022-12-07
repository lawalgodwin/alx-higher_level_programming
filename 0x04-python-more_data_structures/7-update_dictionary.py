#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Update a dictionary with a given key and value

    Args:
        a_dictionary: The dictionary
        key: The specific key
        value: the specific value
    Returns:
        The updated dictionary
    """
    if key in a_dictionary:

        a_dictionary[key] = value

        return a_dictionary

    a_dictionary[key] = value

    return a_dictionary


if __name__ == '__main__':

    update_dictionary()
