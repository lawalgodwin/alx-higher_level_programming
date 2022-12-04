#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """A function that prints all integers of a list
    Args:
        my_list: The list
    Returns:
        Returns None
    """
    for i in my_list:
        print("{:d}".format(i))
