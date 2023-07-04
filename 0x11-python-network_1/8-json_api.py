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
        val['q'] = sys.argv[1]

    try:
        resp = requests.post(urls, data=var)
        res = resp.json()
        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
