#!/usr/bin/python3
"""
This script sends an HTTP GET request to khoza.tech and prints the response status code.
"""
import requests

url = 'http://khoza.tech'
response = requests.get(url)
print(f"Response Status Code: {response.status_code}")

