#!/usr/bin/python3

""" Rectangle Module """


class Rectangle:
    """The blueprint for constucting a Rectangle object"""
    pass

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialise a rectangle object """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a human-readable representation
        of a rectngle object
        """
        r = ''

        i = 1

        if self.width == 0 or self.height == 0:
            return ""

        while (i <= self.height):
            if i == self.height:
                r += "{}".format(self.print_symbol * self.width)
                break

            r += "{}\n".format(self.print_symbol * self.width)
            i += 1
        return r

    def __repr__(self):
        """Returns the code representation
        of a rectangle constructor
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Show custom display on deleting a reactangle"""

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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

    def area(self):
        """public method that returns the calculated area"""
        return (self.width * self.height)

    def perimeter(self):
        """Public instance method that returns the perimeter"""

        if self.width == 0 or self.height == 0:
            return (0)
        return 2 * (self.width + self.height)
