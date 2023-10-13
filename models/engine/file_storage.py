#!/usr/bin/python3
"""
File storage model for serialize and deserialize JSON files
"""
import json
from os import path


class FileStorage:
    """
    FireStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the object file
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        set a new object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize to json
        """
        with open(FileStorage.__file_path, "w") as Myfile:
            Myfile.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        Deserialize from json
        """
        if (path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as Myfile:
                data = Myfile.read()
                FileStorage.__objects = json.loads(data)
