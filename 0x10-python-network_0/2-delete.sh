#!/bin/bash
# This script sends a DELETE request to a URL and displays the body of the response

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Send a DELETE request to the URL and display the body of the response
response=$(curl -s -X DELETE "$1")
echo "$response"

