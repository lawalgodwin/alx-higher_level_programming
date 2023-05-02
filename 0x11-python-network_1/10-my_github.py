#!/usr/bin/python3
""" A Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
   Use Basic Auth to access the id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    _, username, token = argv
    auth = HTTPBasicAuth(username, token)
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
