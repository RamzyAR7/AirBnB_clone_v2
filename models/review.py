#!/usr/bin/python3
"""this module for class review"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """class : review to store more data"""
    if getenv(models.storageType) == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"),
                          nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"),
                          nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
