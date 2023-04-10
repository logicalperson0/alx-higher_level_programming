#!/usr/bin/python3
"""Function is called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is
    an instance of , or if the object is an instance of a class
    inherited from
    Arg:
        obj:object
        a_class: to be tested
    Return:
        True otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
