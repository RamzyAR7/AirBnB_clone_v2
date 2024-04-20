#!/usr/bin/python3
"""this module for class review"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


if getenv('HBNB_TYPE_STORAGE') == "db":
    class Review(BaseModel, Base):
        """class : review to store more data"""
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"),
                          nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"),
                         nullable=False)
else:
    class Review(BaseModel):
        """class : review to store more data"""
        place_id = ""
        user_id = ""
        text = ""
