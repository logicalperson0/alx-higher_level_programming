#!/usr/bin/python3
"""Function called from_json_string"""


import json


def from_json_string(my_str):
    """function that returns an object
    represented by a JSON string
    Arg:
        my_str: string
    Return:
        python obj
    """
    return (json.loads(my_str))
