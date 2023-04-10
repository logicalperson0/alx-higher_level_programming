#!/usr/bin/python3
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
