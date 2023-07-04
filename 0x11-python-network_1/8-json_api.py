#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    urls = "http://0.0.0.0:5000/search_user"
    var = {'q': ""}

    if len(sys.argv) > 1:
        var['q'] = sys.argv[1]
    else:
        ""

    resp = requests.post(urls, data=var)

    try:
        res = resp.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
