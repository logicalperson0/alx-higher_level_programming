#!/usr/bin/python3
"""This function is called append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the
     end of a text file (UTF8) and returns num of char
     Arg:
        filename: file to be appended
        text: txt to append
    Return: num of char
    """
    chars = 0
    with open(filename, 'a', encoding='UTF8') as app:
        loop = app.write(text)

        for x in range(loop):
            chars += 1

        return chars
