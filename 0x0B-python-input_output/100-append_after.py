#!/usr/bin/python3
"""Function called append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file
     after each line containing a specific string
     Arg:
        filename: file
        search_string: search though
        new_string: to be appended to file
    Return:
        None
    """
    lx = []
    with open(filename, 'r') as r:
        while True:
            x = r.readline()
            if search_string in x :
                lx += [new_string]

            lx += [x]

    with open(filename, 'a') as w:
        w.writelines(lx)
