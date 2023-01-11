#!/usr/bin/python3

"""My pylist module"""


class MyList(list):
    """ My PyList class """

    def __init__(self):
        """initialiser or constructor"""
        super().__init__(self)

    def print_sorted(self):
        """Print the content in ascending order"""

        sorted_list = sorted(self)

        print(repr(sorted_list))
