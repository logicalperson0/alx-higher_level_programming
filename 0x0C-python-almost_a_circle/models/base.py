#!/usr/bin/python3
"""
Class called Base
this is the base class from which
all other class in this package
inherit from
"""

import json
import pathlib


class Base:
    """The base class of the package
    has 1 private attr
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor
        Arg:
            id: 1st parameter public attr
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list_dictionaries
        Arg:
            list_dictionaries: dict parameter
        Return:
            Json
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        Arg:
            list_objs: list
        """
        file_n = "{}.json". format(cls.__name__)
        li = []

        if list_objs is not None:
            for x in range(len(list_objs)):
                li.append(list_objs[x].to_dictionary())

        di = cls.to_json_string(li)

        with open(file_n, "w") as files:
            files.write(di)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        Arg:
            json_string: json parameter
        Return:
            dictionary
        """
        if json_string is None or json_string == "":
            return ([])

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Arg:
            dictionary: double ptr to dict parameter
        Return:
            mock
        """
        if cls.__name__ == "Square":
            mock = cls(3)
        elif cls.__name__ == "Rectangle":
            mock = cls(3, 3)
        mock.update(**dictionary)

        return (mock)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Return:
            instances from a file
        """
        file_n = "{}.json". format(cls.__name__)
        if pathlib.Path(file_n).exists() is False:
            return ([])

        with open(file_n, "r") as jsons_f:
            li = jsons_f.read()
        lis = cls.from_json_string(li)
        arr = []

        for x in range(len(lis)):
            arr.append(cls.create(**lis[x]))

        return (arr)
