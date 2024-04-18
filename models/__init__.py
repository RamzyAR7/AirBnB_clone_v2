#!/usr/bin/python3
""" for reload data every process"""
import os
storageType = "db"

if os.getenv('HBNB_TYPE_STORAGE') == storageType:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
