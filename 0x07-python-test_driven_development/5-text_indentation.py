#!/usr/bin/python3
""" Module has a function called text_indentation
prints 2 new line after ".?:" char
"""


def text_indentation(text):
    """ print 2 new line after ".?:" char
    Arg:
        text: 1st para input str
    Return:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    res = text

    for x in ".?:":
        t = res.split(x)
        res = ""
        for y in t:
            y = y.strip(" ")

            if res == "":
                res = y + x
            else:
                res = res + "\n\n" + y + x

    print(res[:-3], end="")
