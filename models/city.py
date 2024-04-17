#!/usr/bin/python3
"""this module for class city"""
from models.base_model import BaseModel, Base, getenv
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """class : City to store more data"""
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:
        name = ""
        state_id = ""
