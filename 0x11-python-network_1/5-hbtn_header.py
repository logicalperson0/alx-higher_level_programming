#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    urls = sys.argv[1]
    resp = requests.get(urls)
    print(resp.headers['X-Request-Id'])
