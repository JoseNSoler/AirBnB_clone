#!/usr/bin/python3
""" Module for storing the BaseModel class. """
from datetime import datetime
import models
from uuid import uuid4


class BaseModel():
    """ BaseModel class, with unique uuid. """
    # __init__ | Private | method |-------------------------------------------|
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                time = '%Y-%m-%dT%H:%M:%S.%f'
                if key == "__class__":
                    continue
                else:
                    if key == "created_at":
                        self.created_at = datetime.strptime(kwargs[key], time)
                    elif key == "updated_at":
                        self.updated_at = datetime.strptime(kwargs[key], time)
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)

    # __str__ | Private | method |--------------------------------------------|
    def __str__(self):
        string = "[{}] ({}) <{}>".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__))
        return string

    # save | Public | method |------------------------------------------------|
    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    # to_dict | Public | method |---------------------------------------------|
    def to_dict(self):
        list_of_keys = []
        dicto_final = {}

        for name in dir(self):
            if name[0] != '_' and name != "to_dict" and name != "save":
                list_of_keys.append(name)
        list_of_keys.append('__class__')

        for name2 in list_of_keys:
            if name2 == "created_at":
                dicto_final[name2] = self.created_at.isoformat("T")
            elif name2 == "updated_at":
                dicto_final[name2] = self.updated_at.isoformat("T")
            elif name2 == "__class__":
                dicto_final[name2] = self.__class__.__name__
            else:
                string = "self.{}".format(name2)

                dicto_final[name2] = eval(string)

        return (dicto_final)
