#!/usr/bin/python3
"""Test module for all classes"""


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test case for the base class"""

    @classmethod
    def setUpClass(self):
        """Set up the base objects to be tested"""
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base()

    def test_id(self):
        """test for default object id"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 2)


if __name__ == '__main__':
    unittest.main()
