#!/usr/bin/python3
"""This is a class where
prevents user from dynamically creating
new intance att.
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """This init does not have
        any attributes
        Return:
        None
        """
        pass
