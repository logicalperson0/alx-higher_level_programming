#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repos = sys.argv[1]
    own = sys.argv[2]
    urls = 'https://api.github.com/repos/{}/{}/commits'.format(own, repos)

    results = get(urls)
    results = results.json()

    try:
        for x in range(0, 10):
            """
            from the url get the sha, for the 1st
            Then, from the url inside commit get the author, and from
            inside author get the name, for the 2nd!
            """
            print("{}: {}".format(results[x].get('sha'),
                                  results[x].get('commit')
                                  .get('author')
                                  .get('name')))
    except Exception:
        pass
