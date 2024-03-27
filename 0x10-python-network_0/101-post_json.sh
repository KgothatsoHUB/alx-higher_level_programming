#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 khoza.tech my_json_0.json"
    exit 1
fi

# Validate JSON file using a JSON validator
jsonlint --quiet "$2"
if [ $? -eq 0 ]; then
    # JSON file is valid, send POST request and display response body
    response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1")

    if [ -z "$response" ]; then
        echo "Empty response or error"
    else
        echo "Response Body:"
        echo "$response"
    fi
    exit 0
else
    # JSON file is not valid
    echo "Not a valid JSON"
    exit 1
fi
