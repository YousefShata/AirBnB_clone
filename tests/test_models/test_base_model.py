#!/usr/bin/python3

"""unittest for base model"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test base model """
    def test_initialization_with_kwargs(self):
        """test initialization with kwargs"""
        obj_id = "some_id"
        created_at = "2023-10-14T10:30:00"
        updated_at = "2023-10-14T11:30:00"

        kwargs = {
            "id": obj_id,
            "created_at": created_at,
            "updated_at": updated_at
        }

        obj = BaseModel(**kwargs)

        self.assertEqual(obj.id, obj_id)
        self.assertEqual(obj.created_at, datetime.fromisoformat(created_at))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(updated_at))

    def test_initialization_without_kwargs(self):
        """test initialization with args"""
        obj = BaseModel()

        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """test save method"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        updated_updated_at = obj.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_to_dict_returns_dict(self):
        """test to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
