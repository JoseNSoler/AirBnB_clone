#!/usr/bin/python3
""" Module for storing City Class definition. """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class with name and state_id. """
    state_id = ""
    name = ""
