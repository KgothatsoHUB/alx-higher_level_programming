#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Send a request to the URL and capture the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$status_code"

