#!/usr/bin/python3
""" Module for storing the tests for BaseModel instances. """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import uuid
import unittest
import os


class TestFileStorage(unittest.TestCase):
    '''
    TestCase class for testing the FileStorage instances and the storage
    variable.
    '''
    def setUp(self):
        ''' Setup for erasing file.json when starting every test. '''
        # Get Current Working Directory.
        cwd = os.getcwd()
        # Concat. the cwd to the name of the .json file
        file_path = cwd + "/file.json"
        # Try to remove it.
        try:
            os.remove(file_path)
        # Except it is not there.
        except Exception as e:
            pass
        # Reset dictionary of storage.
        models.storage._FileStorage__objects = {}

    def test_file_storage(self):
        ''' Tests for the creation of FileStorage classes. '''
        # Test type of FileStorage.
        self.assertEqual(type(models.storage), type(FileStorage()))

        # Test private attributes.
        self.assertTrue(hasattr(models.storage, "_FileStorage__objects"))
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))

        # Get empty dictionary as there is no .json file.
        no_dicto = models.storage.all()

        # Test for the empty dictionary.
        self.assertFalse(bool(no_dicto))

    def test_FileStorage_no_args(self):
        ''' Tests for creation of FileStorage class. '''
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_JSON_file(self):
        ''' Tests for the file.json. '''
        base = BaseModel()
        base.save()
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))

    def test_all(self):
        '''Test all callback dict '''
        new = BaseModel()
        tempo_dict = models.storage.all()
        self.assertIsInstance(tempo_dict, dict)

        # Test for checking BaseModel.id key in dictionary.
        string_id = "BaseModel" + "." + new.id
        self.assertIn(string_id, tempo_dict.keys())

        # Test for object in the dictionary.
        self.assertTrue(type(tempo_dict[string_id]), BaseModel)

    def test_new(self):
        '''test new instance in objects'''

        base = BaseModel()
        with self.assertRaises(TypeError):
            models.storage.new(base, 1)

    def test_JSON_file(self):
        ''' Tests for the file.json. '''
        base = BaseModel()
        base.save()
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))

if __name__ == '__main__':
    unittest.main()
