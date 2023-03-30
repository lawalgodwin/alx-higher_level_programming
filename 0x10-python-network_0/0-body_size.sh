#!/bin/bash
# A Bash script that takes in a URL, sends a request to that 
# URL, and displays the size of the body of the response

if [[ $# -lt 1 ]]; then
  exit 1
fi

URL=$1

curl -sI "$URL" | grep -i Content-Length | grep -Eo "[0-9]+"
