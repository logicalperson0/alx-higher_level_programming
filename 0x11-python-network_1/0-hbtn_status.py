#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    html_resp = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(html_resp)))
    print("\t- content: {}".format(html_resp))
    print("\t- utf8 content: {}".format(html_resp.decode("utf-8")))
