#!/usr/bin/python3

""" File Reader module """


def read_file(filename=""):
    """Read and print file"""
    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:

            print(line)
