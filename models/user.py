#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates the user module"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
