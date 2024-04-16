#!/usr/bin/python3
"""this module for class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class : User to store more data"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
