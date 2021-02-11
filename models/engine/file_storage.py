#!/usr/bin/python3
""" Module for storing the BaseModel class. """
import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    # all | Public | method |-------------------------------------------------|
    def all(self):
        return FileStorage.__objects

    # new | Public | method |-------------------------------------------------|
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # save | Public | method |------------------------------------------------|
    def save(self):

        dicto = {}
        for key, obj in FileStorage.__objects.items():
            dicto[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(dicto, f)

    # reload | Public | method |----------------------------------------------|
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())

                for obj_id in FileStorage.__objects.keys():
                    FileStorage.__objects[obj_id] = eval
                    (FileStorage.__objects[obj_id]['__class__'])
                    (**FileStorage.__objects[obj_id])

        except FileNotFoundError:
            pass
