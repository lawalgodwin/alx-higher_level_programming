#!/usr/bin/python3
""" A Python script fetches the value of a header
    Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    headers = {k: v for k, v in res.headers.items()}
    print(headers.get('X-Request-Id', None))
