#!/usr/bin/python3
"""
This is a print_square module

It contains the function print_square
It prints the number of squares given
"""
def print_square(size):
    """This is the function print_square that returns printed squares
    Arg:
        size: parameter that is sides of the square
    Return:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("ize must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
