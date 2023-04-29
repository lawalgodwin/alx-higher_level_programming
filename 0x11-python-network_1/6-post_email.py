#!/usr/bin/python3
"""Send data to server using the requests module"""

from sys import argv
import requests

url = argv[1]
raw_data = argv[2]

if __name__ == '__main__':

    res = requests.post(url, {'email': raw_data})
    print(res.text)
