from __future__ import annotations
import os
from dataclasses import dataclass, field
import re

class Item:
    name: str
    path: str

    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)

    @staticmethod
    def get(path: str) -> Item:
        if os.path.isdir(path):
            return File(path)
        else:
            return Directory(path)

# ddd
class File(Item):
    name: str
    path: str
    size: int
    extension: str
    mtime: int
    ctime: int
    
    def __init__(self, path: str):
        
        super().__init__(path)
        self.size = os.path.getsize(path)
        self.extension = os.path.splitext(path)[1]
        self.mtime = os.path.getmtime(path)
        self.ctime = os.path.getctime(path)
        
class Directory(Item):
    name: str
    path: str
    items: int

    def __init__(self, path: str):
        super().__init__(path)    
        self.items = len(os.listdir(path))
