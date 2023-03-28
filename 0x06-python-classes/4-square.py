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
            None
        """
        self.size = size

    @property
    def size(self):
        """Method to retrieve it

        Return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        arg:
            value: set by user for square size
        Return:
            None
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        else:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """This method returns the area
        of a square from the size instantaneous variable
        """
        x = self.__size
        return (x * x)
