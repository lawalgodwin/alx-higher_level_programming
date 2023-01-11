#!/usr/bin/python3

"""JSON string to dictionary converter module"""

import json


def from_json_string(my_str):
    """Convert JSON to dictionary and return the result"""

    return json.loads(my_str)
