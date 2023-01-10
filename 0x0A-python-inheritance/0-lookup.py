#!/usr/bin/python3

"""A simple fuction that gives the details of an object"""


def lookup(obj):
    """Returns the att. and methods of an object"""

    return list(dir(obj))
