#!/usr/bin/python3
# -*- 1-square.py created by Godwin Lawal -*-

"""Defines a Square"""


class Square:
    """Create the blueprint of a Square object."""

    def __init__(self, size):
        """Initialize an instance of a Square

        Args:
            size: The specified size of the square to be created
        """

        self.__size = size
