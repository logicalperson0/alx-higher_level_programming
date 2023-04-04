#!/usr/bin/python3
"""

This is a class where
prevents user from dynamically creating
new intance att.

"""


class LockedClass:
    """ This class has not intance or
    class attributes
    """
    __slots__ = ['first_name']
