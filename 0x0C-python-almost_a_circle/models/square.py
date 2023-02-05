#!/usr/bin/python3

"""The Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The square object blueprint"""

    def __init__(self, size, x=0, y=0, id=None):
        """The sqaure object constructor"""

        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """Return human-readable format for the square"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")

    @property
    def size(self):
        """Get the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size attribute to a new value"""
        self.width = value
        self.height = value
