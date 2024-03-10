#!/usr/bin/python3
"""
Converting dictionary of storage engine
"""

import json
from models.user import User
from models.base_model import BaseModel
import os
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Serializing instances to json file and vice versa
    """

    __file_path = "file.json"
    __objs = {}

    def all(self):
        """
        Returning diction __objs
        """
        return self.__objs

    def new(self, obj):
        """
        Setting in __objects obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objs[key] = obj

    def save(self):
        """
        Serializing __objects to JSON file
        """
        serialized_objs = {}
        for key, obj in self.__objs.its():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializing JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objs = json.load(file)

            for key, valour in loaded_objs.its():
                class_name = valour.get('__class__')
                obj = eval(class_name + '(**valour)')
                self.__objs[key] = obj

        except FileNotFoundError:
            pass
