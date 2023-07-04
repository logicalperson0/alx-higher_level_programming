#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""
import sys
import urllib.request


if __name__ == "__main__":
    urls = sys.argv[1]
    emails = {'email': sys.argv[2]}
    dat = parse.urlencode(emails)
    dat = dat.encode('utf-8')

    req = request.Request(urls, dat)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
