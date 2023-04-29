#!/usr/bin/python3
"""A python script Handles error code during http request"""

from sys import argv
from urllib import request, error

url = argv[1]


def make_get_request():
    """Make a get request to the server"""
    with request.urlopen(url) as res:
        print(res.read().decode('utf-8'))


if __name__ == '__main__':
    try:
        make_get_request()
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
