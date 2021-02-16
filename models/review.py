#!/usr/bin/python3
""" Module for storing Review class definition. """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class with place_id, user_id and the text. """
    place_id = ""
    user_id = ""
    text = ""
