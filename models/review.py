#!/usr/bin/python3
"""
Writing class inheritating from BaseModel
Review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defining class of Review
    """

    place_id = ""
    user_id = ""
    text = ""
