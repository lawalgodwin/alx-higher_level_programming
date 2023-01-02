#!/usr/bin/python3

""" Rectangle Module """


class Rectangle:
    """The blueprint for constucting a Rectangle object"""
    pass

    def __init__(self, width=0, height=0):
        """ Initialise a rectangle object """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter of the width instance attribute """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter of the width instance attribute """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter of the height instance attribute """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter of the height instance attribute """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
