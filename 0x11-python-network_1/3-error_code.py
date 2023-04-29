#!/usr/bin/python3
"""
A python script Handles error code during http request
"""

from urllib import request, error
from sys import argv


def make_get_request():
    """make an http get request to the server"""
    url = argv[1]

    with request.urlopen(url) as res:
        print(res.read().decode('utf-8'))


if __name__ == '__main__':
    try:
        make_get_request()
    except error.HTTPError as e:
        print('Error code:', e.code)
