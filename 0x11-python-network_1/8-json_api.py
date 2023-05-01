#!/usr/bin/python3
"""Send payload to server using the requests module"""
from sys import argv
import requests


if __name__ == "__main__":
    data = argv[1] if len(argv) == 2 else ""
    payload = {"q": data}
    url = 'http://0.0.0.0:5000/search_user'

    res = requests.post(url, data=payload)
    response = res.json()

    if response == {}:
        print('No result')
    elif not response:
        print('Not a valid JSON')
    else:
        print("[{}] {}".format(response.get('id'), response.get('name')))
