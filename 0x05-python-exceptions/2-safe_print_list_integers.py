#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print a specific number of only integer elements in a list
    Args:
        my_list: The list
        x: The number of numbers to be printed

    Returns:
    The actual number of elements printed
    """

    count = 0

    for i in range(x):

        try:

            print("{:d}".format(my_list[i]), end="")

            count = count + 1

        except (ValueError, TypeError):

            pass

    print()

    return count
