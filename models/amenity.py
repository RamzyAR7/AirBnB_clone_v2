#!/usr/bin/python3
"""this module for class amenity"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    class Amenity(BaseModel, Base):
        """class : Amenity to store more data about amenities"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        """class : Amenity to store more data about amenities"""
        name = ""
