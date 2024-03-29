#!/usr/bin/python3
"""State Module"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
