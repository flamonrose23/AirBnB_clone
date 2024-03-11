#!/usr/bin/python3
"""
Writing Test for city class
"""

import unittest
import os
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Defining test for city
    """

    def test_type_updated_at(self):
        ct = City()
        self.assertEqual(type(ct.updated_at), datetime)

    def test_type_created_at(self):
        ct = City()
        self.assertEqual(type(ct.created_at), datetime)

    def test_type_id(self):
        ct = City()
        self.assertEqual(type(ct.id), str)

    def test_name(self):
        ct = City()
        self.assertEqual(type(ct.name), str)

    def test_state_id(self):
        ct = City()
        self.assertEqual(type(ct.state_id), str)


if __name__ == '__main__':
    unittest.main()
