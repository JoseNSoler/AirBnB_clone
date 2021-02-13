#!/usr/bin/python3
""" Module for storing the BaseModel class. """
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage():
    """
    FileStorage class for handling serialization and deserialization of objects
    on a JSON format, and managing the file.json for persistance over sessions.
    """
    __file_path = 'file.json'
    __objects = {}

    # all | Public | method |-------------------------------------------------|
    def all(self):
        return self.__objects

    # new | Public | method |-------------------------------------------------|
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # save | Public | method |------------------------------------------------|
    def save(self):

        dicto = {}
        for key, obj in self.__objects.items():
            dicto[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(dicto, f)

    # reload | Public | method |----------------------------------------------|
    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())

                for obj_id, obj in self.__objects.items():
                    self.__objects[obj_id] = eval(obj['__class__'])(**obj)

        except FileNotFoundError:
            pass

    # delete | Public | method |----------------------------------------------|
    def delete(self, id=""):
        """ Deletes an instance currently stored. """
        string = "BaseModel." + id
        switch = False

        for obj_id, obj in self.__objects.items():
            if string == obj_id:
                self.__objects.pop(string)
                self.save()
                switch = True
                return True

        if switch is False:
            return False

    # update | Public | method |----------------------------------------------|
    def update(self, obj_id, key, value):
        try:
            if key != "updated_at" and key != "created_at" and key != "id":
                setattr(self.__objects[obj_id], key, value)
            self.save()
            return True
        except KeyError:
            return False
