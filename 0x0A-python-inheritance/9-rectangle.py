#!/usr/bin/python3
"""Class called Rectangle"""


bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This Instantiation with width and height
        Arg:
            width: width of rectangle
            height: height of rectangle
        Return:
            None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """implements the area of a rectangle
        Return:
            area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """prints the str of the rect
        Return:
            str of rectangle
        """
        return ("[Rectangle] {}/{}". format(self.__width, self.__height))
