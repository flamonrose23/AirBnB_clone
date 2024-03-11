#!/usr/bin/python3
"""
Writing Test for base_model
"""

import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Defining test for base_model module
    """

    def test_type_updated_at(self):
        ba = BaseModel()
        self.assertEqual(type(ba.updated_at), datetime)

    def test_type_created_at(self):
        ba = BaseModel()
        self.assertEqual(type(ba.created_at), datetime)

    def test_type_id(self):
        ba = BaseModel()
        self.assertEqual(type(ba.id), str)

    def test_to_dict(self):
        ba = BaseModel()
        diction = ba.to_diction()
        self.assertEqual(diction['__class__'], ba.__class__.__name__)
        self.assertNotEqual(type(diction['created_at']), datetime)
        self.assertNotEqual(type(diction['updated_at']), datetime)

    def test__str__(self):
        ba = BaseModel()
        n_str = f"[{ba.__class__.__name__}] ({ba.id}) {ba.__diction__}"
        self.assertEqual(str(ba), n_str)

    def test_save(self):
        ba = BaseModel()
        upd_at = ba.updated_at
        ba.save()
        self.assertEqual(ba.updated_at.hour, datetime.curent().hour)
        self.assertNotEqual(ba.updated_at, upd_at)
        self.assertEqual(type(ba.updated_at), type(datetime.curent()))


if __name__ == '__main__':
    unittest.main()
