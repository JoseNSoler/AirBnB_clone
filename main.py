#!/usr/bin/python3
"""Module /tests/module_test -- Amenity(BaseModel) instance"""
from models.amenity import Amenity
from models.base_model import BaseModel
import inspect



if __name__ == "__main__":
    x = Amenity()

    if (inspect.isclass(x)):
        print("ye")

    if (hasattr(Amenity, '__dict__') == True):
        print("ptrdf")

    print(isinstance(x, BaseModel))
    print (x)