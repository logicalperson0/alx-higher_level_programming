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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student
        Return:
            dict repr
        """
        di = dict()
        se = self.__dict__

        if type(attrs) is list:
            for x in attrs:
                if type(x) is not str:
                    return se

                if x in se:
                    di[x] = se[x]
            return di

        return se

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Arg:
            json: dict
        Return:
            None
        """
        se = self.__dict__
        for x in json:
            se[x] = json[x]
