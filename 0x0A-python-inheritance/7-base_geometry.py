#!/usr/bin/python3
"""Class called BaseGeometry"""


class BaseGeometry():
    """A class based on geometry
    Return:
        Exception
    """
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
        self.name = name

        if type(value) is not int:
            raise TypeError("{:s} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0". format(name))

        self.value = value
