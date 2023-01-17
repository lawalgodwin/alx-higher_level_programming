#!/usr/bin/python3

"""My pylist module"""


class MyList(list):
    """ My PyList class """

    def print_sorted(self):
        """Print the content in ascending order"""

        sorted_list = sorted(self)

        print(repr(sorted_list))
