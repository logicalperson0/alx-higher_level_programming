#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    urls = requests.get(sys.argv[1])
    if urls.status_code >= 400:
        print("Error code: {}".format(urls.status_code))
    else:
        print(urls.text)
