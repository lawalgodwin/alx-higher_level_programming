#!/usr/bin/python3
"""Send data to server using the requests module"""
from sys import argv
import requests


if __name__ == "__main__":
    data = argv[1] if argv[1] else ""
    payload = {"q": data}
    url = 'http://0.0.0.0:5000/search_user'

    res = requests.get(url, params=payload)
    if res.content and res.json():
        print("[{}] {}".format(res.json()['id'], res.json()['name']))
    elif not res.json():
        print("Not a valid JSON")
    else:
        print('No result')
