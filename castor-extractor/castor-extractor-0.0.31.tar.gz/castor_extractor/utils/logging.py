import logging
import os

from .time import current_timestamp

CASTOR_LOG_FILE = "castor.log"


def add_file_handler(output_directory: str) -> None:
    filename = f"{current_timestamp()}-{CASTOR_LOG_FILE}"
    file_path = os.path.join(output_directory, filename)
    root_logger = logging.getLogger()
    file_handler = logging.FileHandler(file_path)
    root_logger.addHandler(file_handler)
