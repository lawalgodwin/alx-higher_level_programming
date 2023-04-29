#!/usr/bin/python3
"""A script the get a http response header X-Request-Id value """

from sys import argv
import requests

url = argv[1]

res = requests.get(url)
headers = res.headers
print(headers['X-Request-Id'])
