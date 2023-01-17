#!/usr/bin/python3

"""A module containing a function for testing types
   Returns true or false
"""

def is_same_class(obj, a_class):
    """Checks if an Object is an instance of a_class"""

    return type(obj) == a_class
