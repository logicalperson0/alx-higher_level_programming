#!/usr/bin/python3
"""
This is a add integer function

It adds 2 int numbers
"""


def add_integer(a, b=98):
    """this adds 2 int numbers
    Arg:
        a: can be int or float first parameter
        b: can be int or float second parameter
    Return:
        Addition of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    c = a + b

    return (c)
