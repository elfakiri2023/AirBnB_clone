#!/usr/bin/python3
"""The class to define FileStorage."""
import json
import os

class FileStorage:
    """The class to define FileStorage."""
    
    __objects = {}
    __file_path = "file.json"

    def save(self):
        """Save the objects to the file."""
        dict_object = FileStorage.__objects
        obj_dict = {obj: dict_object[obj].to_dict() for obj in dict_object.keys()}
        
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def new(self, obj):
        """Add a new object to the storage."""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def reload(self):
        """Reload objects from the json file."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for obj in objdict.values():
                    cls_name = obj.pop("__class__")
                    self.new(eval(cls_name)(**obj))
        
    def all(self):
        """ Return all the objects."""
        return FileStorage.__objects

