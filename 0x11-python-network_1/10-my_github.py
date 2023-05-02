#!/usr/bin/python3
"""Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API
   to display your id
   requests module must use Basic Auth
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv
url = "https://api.github.com/user"
_, username, token = argv


if __name__ == '__main__':
    res = requests.get(url, auth=HTTPBasicAuth(username, token))
    print(res.json().get("id"))
