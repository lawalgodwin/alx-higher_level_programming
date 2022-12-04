#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list, in reverse order
    Args:
        my_list: the list
    Returns:
        Returns None
    """

    my_list.reverse()

    for item in my_list:
        print("{:d}".format(item))
