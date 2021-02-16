#!/usr/bin/python3
""" Module for storing User Class definition. """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class with email, password, first and last name. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""