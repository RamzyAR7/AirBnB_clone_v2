#!/usr/bin/python3
"""this module for class state"""
from os import getenv
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
from models import storage
from models.city import City


class State(BaseModel):
    """class : state to store more data"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter attribute to retrieve cities associated with this state."""
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]
