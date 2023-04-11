#!/usr/bin/python3
"""Function called write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a
    text file (UTF8) and returns the number of
    char written
    Arg:
        filename: file to write to
        text: txt to write
    Return:
        num of char
    """
    chars = 0

    with open(filename, 'w', encoding='UTF8') as w:
        w.write(text)

    with open(filename, 'r') as r:
        for x in r.read():
            chars += 1

    return (chars)
