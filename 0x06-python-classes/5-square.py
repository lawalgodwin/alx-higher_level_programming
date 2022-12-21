#!/usr/bin/python3
# -*- 4-square.py created by Godwin Lawal -*-

"""Defines a Square"""


class Square:
    """Create the blueprint of a Square object."""

    def __init__(self, size=0):
        """Initialize an instance of a Square

        Args:
            size: The specified size of the square to be created
        """

        self.size = size

    def area(self):
        """Get the area of a square object from a public method
        Returns:
            The calculated area
        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter  method for the size attribute

        Returns:
            The size of the created square object
        """
        return self.__size

    @size.setter
    def size(self, size=0):
        """Setter method for the size attribute

        Changes the existing size to a specified new one

        Args:
            size: the new size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def my_print(self):
        """Print the square object to the screen"""

        square_size = self.size

        if square_size == 0:

            print()
            return

        for i in range(square_size):

            for j in range(square_size):

                print("#", end="")
            print()

        return
