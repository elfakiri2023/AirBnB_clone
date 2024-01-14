import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    This class contains unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test case by creating an instance
        of the BaseModel class.
        """
        self.base_model = BaseModel()

    def test_init_method(self):
        """
        Test the initialization method of the BaseModel class.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_init_method_with_arguments(self):
        """
        Test the initialization method of the BaseModel
        class with arguments.
        """
        obj_dict = {
            'id': 'test_id',
            'created_at': '2022-01-14T12:00:00.000000',
            'updated_at': '2022-01-14T13:00:00.000000',
            'other_attribute': 'value'
        }

        with patch.dict(self.base_model.__dict__, obj_dict):
            new_base_model = BaseModel(**obj_dict)
            self.assertEqual(new_base_model.id, obj_dict['id'])
            self.assertEqual(new_base_model.created_at,
                             datetime.strptime(obj_dict['created_at'],
                                               BaseModel.DATE_FORMAT))
            self.assertEqual(new_base_model.updated_at,
                             datetime.strptime(obj_dict['updated_at'],
                                               BaseModel.DATE_FORMAT))

    def test_save_method(self):
        """
        Test the save method of the BaseModel class.
        """
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at,
                            self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        """
        Test the str method of the BaseModel class.
        """
        str_representation = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__,
                      str_representation)
        self.assertIn(str(self.base_model.id), str_representation)


if __name__ == "__main__":
    unittest.main()
