#!/usr/bin/python3
"""Function called to_json_string"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation
    of an object (string)
    Arg:
        my_obj: str
    Return:
        json repr
    """
    return (json.dumps(my_obj))
