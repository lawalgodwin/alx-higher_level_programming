#!/usr/bin/python3
""" A Python script that sends data to a url [POST Request]
Usage: ./2-post_email.py <URL> <email>
Display the uft-8 decoder response
"""

import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
data = {"email": sys.argv[2]}

data = urllib.parse.urlencode(data)
data = data.encode("utf-8")

req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as res:
    print(res.read().decode("utf-8"))
