#!/usr/bin/python3

"""The reactangle class module"""
from models.base import Base


class Rectangle(Base):
    """The rectangle object blueprint"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle class constructor"""
        super().__init__(id)

        self.width = width

        self.height = height

        self.x = x

        self.y = y

    def __str__(self):
        """Get a human readable representation of a rec object"""
        s = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return (s)

    @property
    def width(self):
        """Getter of the width instance attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter of the width instance attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the height instance attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter of the height instance attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the x instance attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """setter of the x instance attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the y instance attribute"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """setter of the y instance attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get the area of the rectangle object"""
        return (self.width * self.height)

    def display(self):
        """Print the rectangle object to the stdout"""
        w = "#" * self.width
        i = 1
        while (i <= self.height):
            print(w, end='')
            print()
            i += 1
