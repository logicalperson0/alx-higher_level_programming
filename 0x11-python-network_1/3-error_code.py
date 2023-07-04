#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        urls = sys.argv[1]
        with request.urlopen(urls) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as erred:
        print('Error code: {}'.format(erred.code))
