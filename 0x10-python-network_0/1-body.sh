#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response (200 status code only)

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL, get the status code and response body
response=$(curl -s -w "%{http_code} %{size_download}" -o /dev/null "$1")

# Extract the status code and response body
status_code=$(echo "$response" | awk '{print $1}')
body_size=$(echo "$response" | awk '{print $2}')

# Check if the status code is 200 (OK) and display the response body
if [ "$status_code" -eq 200 ]; then
    curl -s "$1"
fi

