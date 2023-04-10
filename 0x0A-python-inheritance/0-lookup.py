#!/usr/bin/python3
"""This is a method to list out all
methods and attributes"""


def lookup(obj):
    """This method returns list of
    available attributes and methods
    of an object
    Arg:
        obj: obj of the method
    Return:
        list of object
    """
    return (dir(obj))
