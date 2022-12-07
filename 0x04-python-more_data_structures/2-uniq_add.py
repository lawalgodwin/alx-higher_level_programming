#!/usr/bin/python3

def uniq_add(my_list=[]):
    """A fuction that adds all unique numbers in a list

    Args:
        my_list: The list

    Returns:
        Returns the summation
    """

    summation = 0

    unique_list = list(set(my_list))

    for n in unique_list:

        summation = summation + n

    return summation


if __name__ == '__main__':

    uniq_add()
