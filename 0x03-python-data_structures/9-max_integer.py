#!/usr/bin/python3

def max_integer(my_list=[]):
    """Get the max integer in a list
    Args:
        my_list: The list

    Returns:
        The maximum integer in a list
    """

    if (len(my_list) == 0):
        return None

    max_num = my_list[0]

    for n in my_list:
        if max_num < n:
            max_num = n

    return (max_num)
