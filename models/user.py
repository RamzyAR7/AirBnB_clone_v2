#!/usr/bin/python3
"""this module for class user"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """class : User to store more data"""
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review",
                               backref=backref("user", cascade="all"),
                               cascade="all, delete-orphan",
                               single_parent=True)
        places = relationship("Place",
                              backref=backref("user", cascade="all"),
                              cascade="all, delete-orphan",
                              single_parent=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
