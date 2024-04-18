#!/usr/bin/python3
"""this module for class amenity"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Table, 
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class : Amenity to store more data"""
    if models.storageType == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
