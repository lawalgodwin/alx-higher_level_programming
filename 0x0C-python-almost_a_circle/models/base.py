#!/usr/bin/python3

"""The base class for all subsequent classes"""

import json

from os.path import exists


class Base:
    """The base class blueprint"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The base class constructor"""
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if not all((isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to a json file the list of objects
           save empty list if no list_objs otherwise
           save the list of jsonstring generated from list_objs
        """

        list_dict = []

        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as fd:

            if list_objs is None or len(list_objs) == 0 or list_objs == []:
                fd.write('[]')

            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(list_dict)

                fd.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """get the dictionary representation of the json string
           returns empty list if no json_string otherwise
           returns a list of dictionary
        """

        if not json_string or json_string == []:

            return list()

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from a dictionary"""

        newobj = None

        if dictionary and dictionary != {}:

            if cls.__name__ == 'Rectangle':
                newobj = cls(3, 5)
            else:
                newobj = cls(5)

        newobj.update(**dictionary)

        return newobj

    @classmethod
    def load_from_file(cls):
        """Load json string list from file, convert and create obj list"""

        filename = f"{cls.__name__}.json"

        list_obj = []

        if not exists(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as fd:

            json_str = fd.read()

        list_dict = cls.from_json_string(json_str)

        for d in list_dict:
            list_obj.append(cls.create(**d))

        return list_obj
