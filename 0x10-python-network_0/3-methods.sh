#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Send an OPTIONS request to the URL and extract the Allow header to get accepted methods
allowed_methods=$(curl -si "$1" | grep -i '^Allow:' | awk '{print $2}')

# Print the extracted HTTP methods
echo "$allowed_methods"

