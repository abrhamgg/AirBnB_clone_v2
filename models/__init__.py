#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DB storage"""
from models.engine.file_storage import FileStorage
from os import environ

storage_type = environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
