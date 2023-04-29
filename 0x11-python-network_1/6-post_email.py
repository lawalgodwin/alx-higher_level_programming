#!/usr/bin/python3
"""Send data to server using the requests module"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}

    res = requests.post(url, data=data)
    print(res.text)
