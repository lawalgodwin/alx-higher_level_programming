#!/usr/bin/python3
# -*- 2-square.py created by Godwin Lawal -*-

"""Defines a Square"""


class Square:
    """Create the blueprint of a Square object."""

    def __init__(self, size=0):
        """Initialize an instance of a Square

        Args:
            size: The specified size of the square to be created
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Get the area of a square object from a public method
        Returns:
            The calculated area
        """

        return (self.__size * self.__size)
