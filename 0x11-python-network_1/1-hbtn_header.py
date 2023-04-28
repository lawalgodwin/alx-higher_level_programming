#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    headers = dict(res.headers)
    print(headers.get('X-Request-Id', None))
