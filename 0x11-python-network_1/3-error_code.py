#!/usr/bin/python3
"""A python script Handles error code during http request"""

from sys import argv
from urllib import request, error

url = argv[1]
try:
    with request.urlopen(url) as res:
        print(res.read().decode('utf-8'))
except error.HTTPError as e:
    print("Error code: {}".format(e.code))
