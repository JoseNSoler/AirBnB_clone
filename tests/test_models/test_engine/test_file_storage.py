#!/usr/bin/python3
""" Module for storing the tests for BaseModel instances. """
from models.base_model import BaseModel
import models
import uuid
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    TestCase class for testing the FileStorage instances and the storage
    variable.
    """
    def setUp(self):
        """ Setup for erasing file.json when starting every test. """
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

    def test_file_storage(self):
        """ Tests for the creation of FileStorage classes. """
        # Get empty dictionary as there is no .json file.
        models.storage.reload()
        no_dicto = models.storage.all()
        # Test for the empty dictionary.
        self.assertTrue(bool(no_dicto))

if __name__ == '__main__':
    unittest.main()
