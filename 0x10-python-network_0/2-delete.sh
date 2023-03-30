#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first argument and display response body
curl -sX DELETE "$1"
