#!/usr/bin/python3
"""
This module is called 'matrix_divided'

It contains 1 function called 'matrix_divided'
It divides all elements in the matrix
"""


def matrix_divided(matrix, div):
    """This is the function that returns the division of 2 lists
    Args:
        matrix: matrix is 1st parameter
        div: 2nd parameter which divides the matrix
    Return:
        the divided elements of the matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)

    m = len(matrix[0])
    if len(matrix) == 0:
        raise TypeError(msg)
    if m == 0:
        raise TypeError(msg)

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for x in matrix:
        if len(x) is not m:
            raise TypeError("Each row of the matrix must have the same size")
        if type(x) is not list:
            raise TypeError(msg)

        for e in x:
            if type(e) is not int and type(e) is not float:
                raise TypeError(msg)

    nw = list(map(lambda z: list(map(lambda j: round(j / div, 2), z)), matrix))

    return (nw)
