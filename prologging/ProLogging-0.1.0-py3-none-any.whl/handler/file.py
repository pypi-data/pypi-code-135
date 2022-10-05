import os
import sys
from datetime import datetime

class FileHandler:
    def __init__(self, path: str = None, mode: int = 0, file: str = None) -> None:
        match (mode):
            case 0:
                self.filemode = "a"
            case 1:
                self.filemode = "w"

        if file is None:
            sys.exit("File is required")
        if path is None:
            sys.exit("Path is required")
        self.file = f"{path}/{file}"

    def __call__(self, msg = None, type = None) -> None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open (self.file, self.filemode) as f:
            f.write(f"{date} - [{type}] {msg}\n")