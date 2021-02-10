#!/usr/bin/python3
""" Module for storing the BaseModel class. """
import json

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    # all | Public | method |-------------------------------------------------|
    def all(self):
        return FileStorage.__objects

    # new | Public | method |-------------------------------------------------|
    def new(self, obj):
        key = "{}.{}".format(obj["__class__"], obj["id"])
        self.__objects[key] = obj
        # key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # self.__objects[key] = obj.to_dict()

    # save | Public | method |------------------------------------------------|
    def save(self):

        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    # reload | Public | method |----------------------------------------------|
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
