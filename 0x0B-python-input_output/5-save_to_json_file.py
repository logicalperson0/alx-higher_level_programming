#!/usr/bin/python3
"""Function called save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object
    to a text file, using a JSON representation
    Arg:
        my_obj: object
        filename: file to write into
    Return:
        None
    """
    with open(filename, 'w') as x:
        x.write(json.dumps(my_obj))
