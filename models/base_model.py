#!/usr/bin/python3

"""Class to define our the BaseModel."""

import uuid
import models
from datetime import datetime


class BaseModel:
    """Our BaseModel class defines all methods for other classes."""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        sets the 'id', 'created_at', and 'updated_at' in the BaseModel.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        value = datetime.strptime(value, self.DATE_FORMAT)
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Saves the BaseModel instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        _dict = self.__dict__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, _dict)

    def to_dict(self):
        """Converts the BaseModel instance to a dictionary."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
