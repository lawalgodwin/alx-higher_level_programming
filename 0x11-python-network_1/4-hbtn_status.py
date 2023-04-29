#!/usr/bin/python3
""" A python script that makes an http get request to a url """

import requests

res = requests.get('https://alx-intranet.hbtn.io/status')
body = res.content
print("Body response:")
print('\t- type: {}'.format(type(res.text)))
print('\t- content: {}'.format(body.decode('utf-8')))
