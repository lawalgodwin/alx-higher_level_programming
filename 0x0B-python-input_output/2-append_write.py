#!/usr/bin/python3

"""Append write module"""


def append_write(filename="", text=""):
    """Append text content to a text file"""

    with open(filename, 'a', encoding='utf-8') as file:

        return file.write(text)
