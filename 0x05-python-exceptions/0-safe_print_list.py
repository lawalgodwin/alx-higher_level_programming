#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print a specific number of elements in a list
    Args:
        my_list: The list
        x: The number of numbers to be printed

    Returns:
    The actual number of elements printed
    """

    count = 0
    
    for i in range(x):

        try:

            print(f"{my_list[i]}", end="")

            count = count + 1

        except IndexError:

            break

    print()

    return count
