#!/usr/bin/python3
"""Class for the rectangle"""


class Rectangle:
    """ This is the rectangle class"""
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method to get area of rectangle
        Return:
            area from width and height values
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """To get thr perimeter of a rectangle
        Return:
            perimeter
        """
        x = self.__width
        y = self.__height
        if x == 0 or y == 0:
            return 0
        return ((2 * x) + (2 * y))

    def __str__(self):
        """Method that returns the Rectangle #
        Return:
            str of the rectangle
        """
        v = ""
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return v
        for i in range(h):
            for j in range(w):
                v += "#"
            v += "\n"

        return v[:-1]

    def __repr__(self):
        """Representation of the rectangle
        Return:
            repr of the rectangle
        """
        w = self.__width
        h = self.__height
        return ("Rectangle({:d}, {:d})".format(w, h))

    def __del__(self):
        """Deletion of a instance of class rectangle
        Return:
            None
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
