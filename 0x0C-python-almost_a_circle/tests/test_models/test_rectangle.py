#!/usr/bin/python3
"""Test casses for the rectangle module"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle objects"""

    @classmethod
    def setUpClass(self):
        """Set up the reactangle object to be tested"""

        self.rec = Rectangle(10, 20)

    def testIsBaseSubclass(self):
        """Test if the object inherits from the base class"""
        self.assertIsInstance(self.rec, Base)

    def testCreateWithNoArgs(self):
        """Test object creation with no argument"""

        with self.assertRaises(TypeError) as e:
            Rectangle()

    def testCreateWithOneArg(self):
        """Test craeting with just one arg"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10)


if __name__ == '__main__':
    unittest.main()
