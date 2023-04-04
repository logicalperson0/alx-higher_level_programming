#!/usr/bin/python3
"""

This is a class where
prevents user from dynamically creating
new intance att.

"""


class LockedClass:
    __slots__ = ['first_name']
