#!/usr/bin/python3
"""init for filestorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
