#!/usr/bin/python3
"""this module for class state"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
import models
from models.city import City


class State(BaseModel, Base):
    """State class to state information."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter attribute to retrieve associated with this state."""
            cities = models.storage.all("City")
            return [city for city in cities.values() if city.state_id == self.id]
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
