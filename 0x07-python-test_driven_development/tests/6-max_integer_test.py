#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_integer_value(self):
        """Test with only integer value"""

        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-22, -33, -44]), -22)

    def test_empty_value(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_string_value(self):
        """Test with string value"""

        self.assertEqual(max_integer('123454321'), '5')
        self.assertEqual(max_integer(['abc', 'and', 'xyz']), 'xyz')

    def test_none_value(self):
        """Test with None as a value"""

        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mix_value(self):
        """Test using mixed value"""
        with self.assertRaises(TypeError):
            max_integer([2, "not acceptable", 56])


if __name__ == '__main__':
    unittest.main()
