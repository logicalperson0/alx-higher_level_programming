#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the square
        arg:
            size: size of square
        Return:
            None
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """This prints in stdout the square with char: #

        Returns:
            None
        """
        s = self.__size
        p = self.__position
        if s == 0:
            print()
        else:
            for x in range(p[1]):
                print()
            for v in range(s):
                for i in range(p[0]):
                    print(" ", end="")
                for j in range(s):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Getter for position
        REturn:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position
        arg:
            value: set to position the square from start
        Return:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """This is setting the str method to custum"""
        s = self.size
        p = self.position
        if s == 0:
            return ""

        same = ''
        for x in range(p[1]):
            same += '\n'

        for x in range(s):
            for y in range(p[0]):
                same += " "
            for z in range(s):
                same += "#"
            same += "\n"

        return (same[:-1])
