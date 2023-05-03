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

    def __eq__(self, another):
        """This method overloads the eq method"""
        return self.area() == another.area()

    def __lt__(self, another):
        """This method overloads the lt method"""
        return self.area() < another.area()

    def __le__(self, another):
        """This method overloads the le method"""
        return (self.area() <= another.area())

    def __ne__(self, another):
        """This method overloads the ne method"""
        return (self.area() != another.area())

    def __ge__(self, another):
        """This method overloads the ge method"""
        return (self.area() >= another.area())

    def __gt__(self, another):
        """This method overloads the gt method"""
        return (self.area() > another.area())
