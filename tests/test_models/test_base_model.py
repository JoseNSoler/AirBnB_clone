#!/usr/bin/python3
<<<<<<< HEAD
""""""
=======
"""Module /tests/module_test -- BaseModel"""
>>>>>>> 7cc0fb5acdbedaa1b27b464623285ff6f7e51f04
from models.base_model import BaseModel
import uuid
import unittest


class TestBaseModel(unittest.TestCase):
<<<<<<< HEAD
    """ """
=======
    """Test principal for unittest"""
>>>>>>> 7cc0fb5acdbedaa1b27b464623285ff6f7e51f04
    def test_create_instance(self):
        """ Tests for creation of basic BaseModel instances"""

        # Create BaseModel instance.
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 50

        # Test for proper type.
        self.assertEqual(type(base), type(BaseModel()))

        # Test for methods.
        self.assertIn("save", dir(base))
        self.assertIn("to_dict", dir(base))

        # Test if the instance has initial attributes.
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

        # Test for proper return of to_dict()
        self.assertEqual(type(base.to_dict()), type({}))
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

        # Test for properly setting a name attribute.
        self.assertEqual(base.name, "Holberton")
        self.assertEqual(base.my_number, 50)

        # Test if the type of the id is correct.
        version = uuid.UUID(base.id).version
        self.assertEqual(version, 4)

if __name__ == '__main__':
    unittest.main()
