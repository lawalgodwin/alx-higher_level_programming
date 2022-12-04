#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """A function that prints all integers of a list
    Args:
        my_list: The list
    Returns:
        Returns None
    """
    for i in range(len(my_list)):
        print("{0:d}".format(my_list[i]))
