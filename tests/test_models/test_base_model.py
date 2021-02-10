#!/usr/bin/python3
""" Module for storing the BaseModel class. """
from datetime import datetime
from datetime import strptime
from uuid import uuid4


class BaseModel():
    """ BaseModel class, with unique uuid. """
    def __init__(self, *args, **kwargs):
        if kwargs != None:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at":
                        self.key = strptime(kwargs[key].values(),
                                            '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == "updated_at":
                        self.key = strptime(kwargs[key].values(),
                                            '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.key = setattr(self, key, kwargs[key].values())

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at

    def __str__(self):
        string = "[{}] ({}) <{}>".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):

        dicto = []
        dicto_final = {}

        for name in self.__dict__.keys():
            if name[:1] != '_':
                dicto.append(name)
        dicto.append('__class__')

        for name2 in dicto:
            if name2 == "created_at":
                dicto_final[name2] = self.created_at.isoformat("T")
            elif name2 == "updated_at":
                dicto_final[name2] = self.updated_at.isoformat("T")
            elif name2 == "__class__":
                dicto_final[name2] = self.__class__.__name__
            else:
                dicto_final[name2] = getattr(self, name2)

        return (dicto_final)
