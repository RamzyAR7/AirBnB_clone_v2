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
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """Getter attribute to retrieve associated with this state."""
            lst = []
            all_city = models.storage.all(City)
            for city in all_city.values():
                if city.state_id == self.id:
                    lst.append(city)
            return lst
