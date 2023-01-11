#!/usr/bin/python3

"""A module containing a function that saves an object to .json file"""


import json


def save_to_json_file(my_obj, filename):
    """Save an object to .json file"""

    with open(filename, 'w', encoding='utf-8') as file:

        json.dump(my_obj, file)
