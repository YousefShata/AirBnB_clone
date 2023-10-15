#!/usr/bin/python3

"""unittest for base model"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test base model """

    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.new_odj = BaseModel()

    def test_init(self):
        """ test instantiation type"""
        self.assertEqual(type(self.new_odj.id), str)
        self.assertEqual(type(self.new_odj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_odj.created_at), datetime.datetime)

    def test_save(self):
        """ test save method"""
        curr_time = self.new_odj.updated_at
        self.new_odj.save
        self.assertEqual(curr_time, self.new_odj.updated_at)
        """ test with arg"""
        with self.assertRaises(TypeError):
            self.new_odj.save(304)

    def test_to_dict(self):
        """test to_dict method"""
        self.new_odj.name = "bnb"
        self.new_odj.num = 10

        new_dic = self.new_odj.to_dict()
        self.assertEqual(type(new_dic['num']), int)
        self.assertEqual(type(new_dic['name']), str)
        self.assertEqual(type(new_dic['__class__']), str)
        self.assertEqual(new_dic['__class__'], 'BaseModel')
        self.assertEqual(type(new_dic['updated_at']), str)
        self.assertEqual(type(new_dic['id']), str)
        self.assertEqual(type(new_dic['created_at']), str)
        """ test with arg"""
        with self.assertRaises(TypeError):
            self.new_odj.to_dict('str')

    def init_with_invalid_dates(self):
        """Test initialization with invalid date"""
        invalid_dict = {
            'id': '123',
            'created_at': '2021-08-07T15:30:51.120690',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }

        invalid_dict['created_at'] = "INVALID DATE"
        with self.assertRaises(ValueError):
            inst = BaseModel(**invalid_dict)

        invalid_dict['updated_at'] = 2023
        with self.assertRaises(TypeError):
            inst = BaseModel(**invalid_dict)


if __name__ == '__main__':
    unittest.main()
