import unittest
import os
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test class for FileStorage.
    """

    def setUp(self):
        """
        Set up method called before each test.
        """
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        FileStorage.__file_path = self.file_path

    def tearDown(self):
        """
        Tear down method called after each test.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_and_reload(self):
        """
        Test saving and reloading objects.
        """
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        self.file_storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("BaseModel.{}".format(test_obj.id), new_storage.all())

    def test_new_method(self):
        """
        Test the new method for adding objects to storage.
        """
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        self.assertIn("BaseModel.{}".format(test_obj.id),
                      self.file_storage.all())

    def test_all_method(self):
        """
        Test the all method to retrieve all objects.
        """
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        all_objects = self.file_storage.all()
        self.assertIn("BaseModel.{}".format(test_obj.id), all_objects)


if __name__ == "__main__":
    unittest.main()
