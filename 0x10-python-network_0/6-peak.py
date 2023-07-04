#!/usr/bin/python3
"""Finds a peak in list_of_integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in list_of_integers
    """
    if list_of_integers == []:
        return None
    return (max(list_of_integers))
    # return (0, (len(list_of_integers) - 1), )
