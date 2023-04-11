#!/usr/bin/python3
"""Function called pascal_triangle"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    Arg:
        n: int para
    Return:
        list of lists
    """
    lx = []

    if n <= 0:
        return []

    
