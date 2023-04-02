#!/usr/bin/python3
"""
This is a say_my_name module

It contains the function: say_my_name
It prints out the 1st and last names given
"""


def say_my_name(first_name, last_name=""):
    """This function returns the 1st and last names
    Arg:
        first_name: 1st parameter
        last_name: 2nd parameter
    Return:
        The full name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
