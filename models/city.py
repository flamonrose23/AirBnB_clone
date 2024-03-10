#!/usr/bin/python3
"""
Writing class inheritating from BaseModel
City module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Creating class city
    """

    state_id = ""
    name = ""
