#!/usr/bin/python3
"""Function called load_from_json_file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file
    Arg:
        filename: file to read
    Return:
        None
    """
    with open(filename, 'r') as x:
        return json.load(x)
