#!/usr/bin/python3
"""A class that inherits from list which
has a method print_sorted that prints 
the list but sorted
"""


class MyList(list):
    """A class that has a method called
    print_sorted that prints the list
    but sorted
    """
    def print_sorted(self):
        """Method that prints the list but
        sorted
        Return:
            sorted list
        """
        sorting = self.copy()
        sorting.sort(reverse=False)
        print(sorting)
