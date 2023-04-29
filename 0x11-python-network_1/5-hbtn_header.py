#!/usr/bin/python3
"""A script that get a http response header X-Request-Id value
Usage: ./5-hbtn_header.py <URL>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
