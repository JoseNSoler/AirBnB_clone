#!/usr/bin/python3
"""Module test /tests/models/engine -- FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os


class TestFileStorage_instantiation(unittest.TestCase):
    """ """
    x = storage()
        

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    
    def test_FileStorage_no_args(self):
        """ Tests for creation of basic BaseModel instances"""
        # Create BaseModel instance.
        self.assertEqual(type(FileStorage()), FileStorage)
    
    def test_JSON_file(self):
        """ Tests for the file.json. """
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))
    
    def test_all(self):
        '''Test all callback dict '''
        new = BaseModel()
        tempo_dict = storage.all()
        self.assertIsInstance(tempo_dict, dict)
    
if __name__ == '__main__':
    unittest.main()
