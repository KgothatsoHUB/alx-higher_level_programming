#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body in bytes

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Send a request to the URL and count the size of the response body in bytes
curl -s "$1" | wc -c

