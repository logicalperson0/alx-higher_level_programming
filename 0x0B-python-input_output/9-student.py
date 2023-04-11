#!/usr/bin/python3
"""Class called student"""


class Student():
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of student
        Arg:
            first_name: 1st para
            last_name: 2nd para
            age: 3rd para
        Return:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        of a Student
        Return:
            dict repr
        """
        return (self.__dict__)
