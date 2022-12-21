#!/usr/bin/python3
# -*- 4-square.py created by Godwin Lawal -*-

"""Defines a Square"""


class Square:
    """Create the blueprint of a Square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize an instance of a Square

        Args:
            size: The specified size of the square to be created
        """

        self.size = size

        self.position = position

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
    def size(self, value=0):
        """Setter method for the size attribute

        Changes the existing size to a specified new one

        Args:
            value: the new size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter method for the Square object coordinates

        Returns:
            The coordinate of a sqaure object

        """

        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """The setter method for the square coordinate
        Args:
            value(tuple): The new value to replace with. A 2 length tuple
        Returns:
            None
        """

        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square object to the screen"""

        square_size = self.size

        if square_size == 0:

            print()
            return

        for i in range(square_size):

            print(f"{' ' * self.position[0]}{'#' * square_size}")
