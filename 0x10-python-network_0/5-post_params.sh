#!/bin/bash
# This script sends a POST request with parameters to a URL and displays the response body

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 khoza.tech"
    exit 1
fi

# Define the POST parameters
email="kgothikhoza@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with parameters to the URL and display the response body
curl -s -X POST -d "email=$email&subject=$subject" "$1"

