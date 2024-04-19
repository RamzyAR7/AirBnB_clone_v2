#!/usr/bin/python3
"""
this module for base class
"""
from os import getenv
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
import models

if getenv('HBNB_TYPE_STORAGE') == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """BaseModel class the parant for others"""
    if getenv('HBNB_TYPE_STORAGE') == "db":
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ init methoud for BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ str reprecentation """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ to save obj in json file """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ to convert obj"""
        dct = self.__dict__.copy()
        dct['__class__'] = type(self).__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()

        dct.pop('_sa_instance_state', None)

        return dct

    def delete(self):
        """delete the current obj"""
        models.storage.delete(self)
