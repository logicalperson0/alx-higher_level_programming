#!/usr/bin/python3
"""
 script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    urls = "https://api.github.com/use"
    resp = auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])

    results = get(urls, auth=resp)
    results = results.json()
    print(results.get("id"))
