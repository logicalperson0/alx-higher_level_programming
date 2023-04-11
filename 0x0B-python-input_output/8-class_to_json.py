#!/usr/bin/python3
"""Function called class_to_json"""


def class_to_json(obj):
    """function that returns the dictionary description
    Arg:
        obj: object
    Return:
        dict form of object
    """
    return obj.__dict__
