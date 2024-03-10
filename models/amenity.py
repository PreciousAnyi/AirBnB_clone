#!/usr/bin/python3
"""Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
