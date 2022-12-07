#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print the keys and value of a dictionary"""

    keys = sorted(a_dictionary)

    for key in keys:

        print("{:s}: {}".format(key, a_dictionary[key]))


if __name__ == '__main__':

    print_sorted_dictionary()
