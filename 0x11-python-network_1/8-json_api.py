#!/usr/bin/python3
"""Send payload to server using the requests module 'get' method"""
from sys import argv
import requests


if __name__ == "__main__":
    data = argv[1] if argv[2] else ""
    payload = {"q": data}
    url = 'http://0.0.0.0:5000/search_user'

    res = requests.post(url, data=payload)
    response = res.json()

    if response == {}:
        print('No result')
        return
    if not response:
        print('Not a valid JSON')
        return
    print("[{}] {}".format(res.json().get('id'), res.json().get('name')))
