#!/usr/bin/python3
"""Function called read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout
    Arg:
        filename: file to read
    Return:
        None
    """
    with open(filename, 'r', encoding='UTF8') as reading:
        r = reading.read()
        print(r, end="")
