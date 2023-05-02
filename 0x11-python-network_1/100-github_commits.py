#!/usr/bin/python3
""" A Python script that gets the 10 latest commits from a github repo"""
from sys import argv
import requests


if __name__ == "__main__":
    _, reponame, owner = argv
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, reponame)
    res = requests.get(url)
    try:
        first_ten = res.json()[0:10]
        for commit in first_ten:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
