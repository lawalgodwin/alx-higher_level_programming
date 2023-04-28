#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    response = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode('utf-8')))
