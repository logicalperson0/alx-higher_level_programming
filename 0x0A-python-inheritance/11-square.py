#!/usr/bin/python3
"""Class called Square"""


sq = __import__('9-rectangle').Rectangle


class Square(sq):
    """Square that inherits from Rectangle subclass"""

    def __init__(self, size):
        """method to Instantiation size
        Arg:
            size: 1st para
        Return:
            None
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of a square
        Return:
            area
        """
        return (self.__size ** 2)

    def __str__(self):
        """Returns str of square
        Return:
            str of sq
        """
        return ("[Square] {}/{}". format(self.__size, self.__size))
