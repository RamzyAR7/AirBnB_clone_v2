#!/usr/bin/python3
""" for reload data every process"""
from os import getenv
storageType = getenv('HBNB_TYPE_STORAGE')
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if storageType == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
