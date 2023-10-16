#!/usr/bin/python3
"""test user class"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models.base_model
import models.user
import inspect
import datetime


class TestUser(unittest.TestCase):
    """ class to test user class """
    def setUp(self):
        """set up method"""
        self.new_obj = User()

    def check_attributes(self):
        """ check for attributes """
        user = User()
        user.f_name = "bnb"
        user.l_name = "bnb"
        user.email = "bnb@email.com"
        user.password = "root"
        self.assertEqual(user.f_name, "bnb")
        self.assertEqual(user.l_name, "bnb")
        self.assertEqual(user.email, "bnb@email.com")
        self.assertEqual(user.password, "root")
        self.assertTrue(hasattr(User, "f_name"))
        self.assertTrue(hasattr(User, "l_name"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "email"))
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.f_name), str)
        self.assertEqual(type(User.l_name), str)
        self.assertEqual(type(User.password), str)

    def test_init_user(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_user(self):
        """ test User.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_city(self):
        """ test User.to_dict() """
        self.new_obj.f_name = "bnb"
        self.new_obj.l_name = "bnb"
        self.new_obj.email = "jonas@example.com"
        self.new_obj.password = "root"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['f_name']), str)
        self.assertEqual(dict_['f_name'], "bnb")
        self.assertEqual(dict_['l_name'], "bnb")
        self.assertEqual(dict_['email'], "jonas@example.com")
        self.assertEqual(dict_['password'], "root")
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "User")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')


if __name__ == '__main__':
    unittest.main()
