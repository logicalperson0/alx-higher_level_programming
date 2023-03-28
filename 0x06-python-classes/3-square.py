#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """Initializing the square
        arg:
            size: size of square
        Return:
            area of a square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        else:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """This method returns the area
        of a square from the size instantaneous variable
        """
        x = self.__size
        return (x * x)
