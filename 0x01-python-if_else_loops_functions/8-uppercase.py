#!/usr/bin/python3

def uppercase(str1):
    """Print a string in uppercase

    Args:
        str1: The string

    Returns:
        None
    """

    for s in str1:

        if (ord(s) >= 97) and (ord(s) <= 122):

            s = chr(ord(s) - 32)

        print("{}".format(s), end='')

    print()
