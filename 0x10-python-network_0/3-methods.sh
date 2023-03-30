#!/bin/bash
# A  Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sIL "$1" | grep -i "Allow" | cut -d " " -f 2-
