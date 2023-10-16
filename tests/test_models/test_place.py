#!/usr/bin/python3
"""test place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import models.base_model
import models.place
import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """set up method"""
        self.new_obj = Place()

    def test_init_place(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_place(self):
        """ test State.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)

        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_place(self):
        """ test BaseModel.to_dict() """
        self.new_obj.name = "bnb"
        dict_ = self.new_obj.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict_['name']), str)
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "Place")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)

        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')


if __name__ == '__main__':
    unittest.main()
