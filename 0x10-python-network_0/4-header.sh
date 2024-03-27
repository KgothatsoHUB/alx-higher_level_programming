#!/bin/bash
# This script sends a GET request to a URL with a custom header and displays the body of the response

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Send a GET request to the URL with the custom header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"

