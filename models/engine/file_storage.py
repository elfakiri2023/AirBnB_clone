#!/usr/bin/python3
"""The class to define FileStorage."""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

class FileStorage:
    """The class to define FileStorage."""

    __objects = {}
    __file_path = "file.json"

    def save(self):
        """Save the objects to the file."""
        d_object = FileStorage.__objects
        obj_dict = {obj: d_object[obj].to_dict() for obj in d_object.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def new(self, obj):
        """Add a new object to the storage."""
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def reload(self):
        """Reload objects from the file."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for obj in objdict.values():
                    cls_name = obj.pop("__class__")
                    self.new(eval(cls_name)(**obj))

    def all(self):
        return FileStorage.__objects
