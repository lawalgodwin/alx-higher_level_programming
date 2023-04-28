#!/usr/bin/python3
""" A Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the X-Request-Id
    variable found in the header of the response.
"""
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    headers = {k: v for k, v in res.headers.items()}
    print(headers.get('X-Request-Id', None))
