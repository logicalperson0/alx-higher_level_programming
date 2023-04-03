#!/usr/bin/python3
"""Class for the rectangle"""


class Rectangle:
    """ This is the rectangle class"""
    def __init__(self, width=0, height=0):
        """This is where the width and height
        are init
        Arg:
            width: 1st parameter
            height: 2nd parameter
        Return:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to get width
        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set width
        Arg:
            value: 1st parameter for width
        Return:
            none
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """method to get height
        Return:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height
        Arg:
            value: 1st parameter for height
        Return:
            none
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
