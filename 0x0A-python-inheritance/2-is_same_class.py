#!/usr/bin/python3
"""A function called is_same_class"""


def is_same_class(obj, a_class):
    """function that returns True if the object
    is exactly an instance of the specified class
    Arg:
        obj: obj parameter
        a_class: the class to test
    Return:
        True otherwise false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
