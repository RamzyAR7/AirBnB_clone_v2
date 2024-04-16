#!/usr/bin/python3
"""this module for class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class : review to store more data"""
    place_id = ""
    user_id = ""
    text = ""
