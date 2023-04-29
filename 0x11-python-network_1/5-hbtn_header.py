#!/usr/bin/python3
"""A script the get a http response header X-Request-Id value """

from sys import argv
import requests

url = argv[1]


if __name__ == '__main__':
    res = requests.get(url)

    print(res.headers.get('X-Request-Id'))
