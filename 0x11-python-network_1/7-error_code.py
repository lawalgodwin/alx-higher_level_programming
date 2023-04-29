#!/usr/bin/python3
"""Handle Http error using the requests module"""
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == "__main__":
    url = argv[1]

    try:
        res = requests.get(url)
        print(res.text)
    except HTTPError as e:
        print(type(e))
