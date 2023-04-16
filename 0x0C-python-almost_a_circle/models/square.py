#!/usr/bin/python3
"""Class called square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square
        Arg:
            size: 1st para
            x: 2nd para
            y: 3rd para
            id: 4th para
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override the str method"""
        ig = "({}) ". format(self.id)
        xy = "{}/{} ". format(self.x, self.y)
        si = "{}". format(self.width)

        return("[Square] " + ig + xy + "- " + si)

    @property
    def size(self):
        """Getter for size"""
        return (self.height)

    @size.setter
    def size(self, res):
        """Setter for size"""

        self.width = res
        self.height = res

    def update(self, *args, **kwargs):
        """assigns attr
        Arg:
            args: assigns attr
            kwargs: assigns attr by key, value
        """
        if len(args) != 0:
            for x, arg in enumerate(args):
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
        else:
            for kwarg in kwargs.keys():
                if kwarg == 'id':
                    self.id = kwargs['id']
                elif kwarg == 'size':
                    self.width = kwargs['size']
                elif kwarg == 'x':
                    self.x = kwargs['x']
                elif kwarg == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """returns a dict of class square
        Return:
            a dictionary
        """
        di = {}
        di['id'] = self.id
        di['x'] = self.x
        di['size'] = self.height
        di['y'] = self.y

        return (di)
