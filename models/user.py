#!/usr/bin/python3
"""
Writing class inheritating from BaseModel of User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Creating class user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
