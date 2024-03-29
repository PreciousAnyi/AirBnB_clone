#!/usr/bin/python3
"""BaseModel module"""

import uuid
import json
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        from models.engine.file_storage import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of the instance"""
        class_name = self.__class__.__name__
        instance_id = self.id
        attributes = self.__dict__
        return "[{}] ({}) {}".format(class_name,
                                     instance_id, attributes)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        from models.engine.file_storage import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
                of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return json.loads(json.dumps(new_dict, ensure_ascii=False))
