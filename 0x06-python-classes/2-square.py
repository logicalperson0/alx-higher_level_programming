#!/usr/bin/python3
"""defining a Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """Initializing the square
        Arg:
            __size: size of square
        Returns: None
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
