#!/usr/bin/python3
"""File storage module"""

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a
    JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets a new object in the dictionary of objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary of objects to a JSON file.
        """
        with open(FileStorage.__file_path, "w") as file:
            serialized_obj = {key: obj.to_dict() for key, obj
                              in FileStorage.__objects.items()}
            json.dump(serialized_obj, file)

    def reload(self):
        """Deserialize the JSON file __file_path
        to __objects, if it exists."""
        if exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj_cls = globals()[class_name]
                        obj_instance = obj_cls(**value)
                        FileStorage.__objects[key] = obj_instance
            except FileNotFoundError:
                pass


storage = FileStorage()
