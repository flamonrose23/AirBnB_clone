#!/usr/bin/python3
"""
Writing Test for Amenity model
"""

import os
import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Defing test for Amenity class
    """

    def test_type_updated_at(self):
        a = Amenity()
        self.assertEqual(type(a.updated_at), datetime)

    def test_type_created_at(self):
        a = Amenity()
        self.assertEqual(type(a.created_at), datetime)

    def test_type_id(self):
        a = Amenity()
        self.assertEqual(type(a.id), str)

    def test_name(self):
        a = Amenity()
        self.assertEqual(type(a.name), str)


if __name__ == '__main__':
    unittest.main()
