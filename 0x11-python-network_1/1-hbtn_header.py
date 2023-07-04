#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable: header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    urls = sys.argv[1]
    with urllib.request.urlopen(urls) as resp:
        # html_head = resp.info()
        print(resp.headers['X-Request-Id'])
