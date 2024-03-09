#!/usr/bin/python3
"""File storage module"""

import json
from os.path import exists


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
        """
        Deserializes the JSON file to the dictionary of objects.
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    deserialized_obj = json.loads(file)
                    for key, obj_dict in deserialized_obj.items():
                        class_name, obj_id = key.split('.')
                        obj_cls = eval(class_name)
                        obj_instance = obj_cls(**obj_dict)
                        FileStorage.__objects[key] = obj_instance
                except Exception as error:
                    pass
