#!/usr/bin/python3
"""
Initializing for filestorage
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
