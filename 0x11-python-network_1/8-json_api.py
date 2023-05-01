#!/usr/bin/python3
"""Send payload to server using the requests module"""
from sys import argv
import requests


if __name__ == "__main__":
    data = argv[1] if len(argv) == 2 else ""
    payload = {"q": data}
    url = 'http://0.0.0.0:5000/search_user'

    res = requests.post(url, data=payload)
    try:
        response = res.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
