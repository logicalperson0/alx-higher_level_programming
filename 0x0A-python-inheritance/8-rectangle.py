#!/usr/bin/python3
"""Class called BaseGeometry"""


class BaseGeometry():
    """A class based on geometry
    """
    def __init__(self, width, height):
        """This Instantiation with width and height
        Arg:
            width: width of rectangle
            height: height of rectangle
        Return:
            None
        """
        if integer_validator(name, width):
            self.__width = width

    def area(self):
        e = "area() is not implemented"
        raise Exception(e)

    def integer_validator(self, name, value):
        """function that validates value
        Arg:
            name: string
            value: int
        Return:
            None
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
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
