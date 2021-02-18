#!/usr/bin/python3
""" Module for storing the tests for BaseModel instances. """
from models.city import City
import models
import uuid
import unittest
import os
from datetime import datetime


class TestCity_instance(unittest.TestCase):
    '''
    TestCase class for testing the FileStorage instances and the storage
    variable.
    '''
    def test_id_is_public(self):
        '''Check for public attribute'''
        city1 = City()
        self.assertEqual(str, type(city1.id))

    def test_created_at_is_public(self):
        '''Check for public attribute created'''
        city1 = City()
        self.assertNotEqual(str, type(city1.created_at))

    def test_updated_at_is_public(self):
        '''Check for public attribute updated'''
        city1 = City()
        self.assertNotEqual(str, type(city1.updated_at))

    def test_two_cities_unique_ids(self):
        '''Check unique ids '''
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_instantiation_with_kwargs(self):
        '''Check instance with kwargs '''
        date = datetime.today()
        date_iso = date.isoformat()
        city1 = City(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city1.id, "345")
        self.assertEqual(city1.created_at, date)
        self.assertEqual(city1.updated_at, date)


class TestCity_save(unittest.TestCase):
    '''Tests cases for inhereted save method '''
    def setUp(self):
        ''' Setup for erasing file.json when starting every test.'''
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

    def create_and_save(self):
        city1 = City()
        city1.save

    def test_save_with_arg(self):
        '''Check none args on save'''
        city1 = City()
        with self.assertRaises(TypeError):
            city1.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        cityid = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(cityid, f.read())


class TestCity_to_dict(unittest.TestCase):
    '''Tests cases for inhereted to_dict method'''
    def test_to_dict_type(self):
        '''Checks returned type of to_dict '''
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        '''Check all inhereted attributes in dict '''
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())
    
    def test_to_dict_contains_added_attributes(self):
        '''Check new attributtes present in dict '''
        city = City()
        city.name = "Holberton"
        city.my_number = 50
        self.assertEqual("Holberton", city.name)
        self.assertIn("my_number", city.to_dict())

if __name__ == "__main__":
    unittest.main()
