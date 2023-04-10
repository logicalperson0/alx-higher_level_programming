#!/usr/bin/python3
"""Function called inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    Arg:
        obj: object
        a_class: to be tested
    Return:
        True otherwise false
    """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
