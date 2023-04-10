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

        super().__init__(self.__size, self.__size)

    def area(self):
        """area of a square
        Return:
            area
        """
        a = super().area()
        return (a)
