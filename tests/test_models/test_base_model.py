#!/usr/bin/python3

"""unittest to test  base model"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """tests for base model"""
    def setUp(self) -> None:
        """setup method"""
        pass

    def test_base(self):
        """test inputs for base model"""
        new_model = BaseModel()
        new_model.name = "bnb"
        new_model.num = 00
        self.assertEqual([new_model.name, new_model.num], ["bnb, 00"])

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass


if __name__ == "__main__":
    unittest.main()
