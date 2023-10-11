#!/usr/bin/python3
"""
This is the Base Model for all other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel Class which will be inharited
    """

    def __init__(self):
        """
        Initiate instances attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Representing the object
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        save the instance data
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        dic = self.__dict__
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic
