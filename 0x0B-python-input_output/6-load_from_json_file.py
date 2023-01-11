#!/usr/bin/python3

"""A module that loads object from json file"""

import json


def load_from_json_file(filename):
    """ Create object from json file """

    with open(filename, 'r', encoding='utf-8') as file:

        return json.load(file)
