#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable: header of the response
"""
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as resp:
    # html_head = resp.read()
    print(resp.headers['X-Request-Id'])
