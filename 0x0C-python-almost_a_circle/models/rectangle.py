#!/usr/bin/python3
"""Class called rectangle
inheritance from Base"""


from models.base import Base


class Rectangle(Base):
    """Class called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        Arg:
            width: 1st parameter
            height: 2nd parameter
            x: 3rd para
            y: 4th para
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle
        Return:
            area
        """
        return (self.__width * self.__height)

    def display(self):
        """prints with char # rectangle instance
        Return:
            None
        """
        wi = self.__width
        he = self.__height
        
        for down in range(self.__y):
            print()
        for j in range(he):
            for side in range(self.__x):
                print(" ", end="")
            for i in range(wi):
                print("#", end="")
            print()

    def __str__(self):
        """override the str method
        Return:
            None
        """
        ig = "({}) ". format(self.id)
        xy = "{}/{} ". format(self.__x, self.__y)
        wh = "{}/{}". format(self.__width, self.__height)

        return ("[Rectangle] " + ig + xy + "-" + " " + wh)

    def update(self, *args, **kwargs):
        """assigns an arg to each attr
        Arg:
            args: parameter
        """
        if len(args) != 0:
            for x, arg in enumerate(args):
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.__width = arg
                elif x == 2:
                    self.__height = arg
                elif x == 3:
                    self.__x = arg
                elif x == 4:
                    self.__y = arg

        else:
            for kwarg in kwargs.keys():
                if kwarg == 'id':
                    self.id = kwargs['id']
                elif kwarg == 'width':
                    self.__width = kwargs['width']
                elif kwarg == 'height':
                    self.__height = kwargs['height']
                elif kwarg == 'x':
                    self.__x = kwargs['x']
                elif kwarg == 'y':
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """returns dict repr of class rectangle
        Return:
            a dictionary
        """
        di = {}
        di['x'] = self.x
        di['y'] = self.y
        di['id'] = self.id
        di['height'] = self.height
        di['width'] = self.width

        return (di)
