#!/usr/bin/python3
""" for reload data every process"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
