#!/usr/bin/python3
"""Module base.
Defines a Base class for other classes in the project.
"""

import json
import os


class Base:
    """Class with:
    Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance.
        Args:
            - id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries.
        Args:
            - list_dictionaries: list of dicts
        Returns: JSON representation of the list
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file.
        Args:
            - list_objs: list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"
        l = []
        s = ''
        with open(filename, 'w+') as f:
            if list_objs is not None:
                for x in list_objs:
                    l_dict = x.to_dictionary()
                    l.append(l_dict)
                s = cls.to_json_string(l)
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            - json_string: string to convert to list
        """

        l = []
        if json_string is not None and json_string != '':
            l = json.loads(json_string)
        return l

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            - dictionary: used as **kwargs
        Returns: instance created
        """

        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l
