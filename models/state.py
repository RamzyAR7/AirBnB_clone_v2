#!/usr/bin/python3
"""this module for class state"""
from models.base_model import BaseModel, Base, getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
import models
from models.city import City


class State(BaseModel, Base):
    """class : state to store more data"""

    if models.storageType == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref=backref("state",
                                                      cascade="all"),
                              cascade="all, delete-orphan",
                              single_parent=True)
    else:
        name = ""
        @property
        def cities(self):
            """returns the list of City of the current state"""
            return [obj for obj in models.storage.all().values()
                    if (isinstance(obj, City) and
                        (self.id == obj.state_id))]
