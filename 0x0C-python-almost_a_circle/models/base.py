#!/usr/bin/python3

"""The base class for all subsequent classes"""


class Base:
    """The base class blueprint"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The base class constructor"""
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
