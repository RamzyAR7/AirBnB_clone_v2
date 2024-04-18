#!/usr/bin/python3
""" for reload data every process"""
from os import getenv
storageType = 'HBNB_TYPE_STORAGE'

if getenv(storageType) == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
