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
        self.rec2 = Rectangle(10, 30, 0, 0)
        self.rec3 = Rectangle(8, 7, 0, 0, 12)

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

    def testArea(self):
        """Test case for rectangle area fuction"""

        self.assertEqual(self.rec.area(), 200)
        self.assertEqual(self.rec2.area(), 300)
        self.assertEqual(self.rec3.area(), 56)

    def testUpdate(self):
        """Test for the update method"""
        self.rec2.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.rec2), '[Rectangle] (89) 4/5 - 2/3')
        self.assertEqual(str(self.rec), '[Rectangle] (1) 0/0 - 10/20')


if __name__ == '__main__':
    unittest.main()
