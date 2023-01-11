#!/usr/bin/python3

""" write file module """


def write_file(filename="", text=""):
    """Write a text content to a file"""

    with open(filename, 'w', encoding='utf-8') as file:

        return file.write(text)
