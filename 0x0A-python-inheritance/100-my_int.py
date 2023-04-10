#!/usr/bin/python3
"""Class is called MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __ne__(self, inverse):
        """Method that is != operator
        Arg:
            inverse: int para
        Return:
            inverse of !=
        """
        return True

    def __eq__(self, inverse):
        """Method that is == operator
        Arg:
            inverse: int para
        Return:
            inverse of ==
        """
        return False
