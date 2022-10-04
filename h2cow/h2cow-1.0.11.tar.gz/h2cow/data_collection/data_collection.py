import datetime
import logging
import os
from pathlib import Path
import time

from .stream_reader import StreamReader
from h2cow.utils.configure import get_rtsp, read_config

def close_connection(readers: list):
    for reader in readers:
        reader.exit()

def get_frame(readers: list):
    for reader in readers: 
        reader.get_frame()

def get_streams(cfg: dict):
    readers = []
    for channel in cfg["channels"]:
        readers.append(
            StreamReader(
                channel, 
                get_rtsp(cfg, channel), 
                Path(
                    cfg["project_path"], 
                    cfg["image_recordings"]
                    )
                )
            )
    return readers

def collection_loop(readers: list):
    try:
        print("Press crtl+c to exit.")
        while True:
            get_frame(readers)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exitting...")
        close_connection(readers)
        logging.info("Application closed")

def capture_frames(config: str):
    cfg = read_config(config)
    # logging.basicConfig(
    #     filename=Path(
    #         cfg["project_path"], 
    #         cfg["logs"], 
    #         f"data_collection{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    #         ), 
    #     level=logging.DEBUG, 
    #     filemode="w",
    #     format="%(asctime)s - %(levelname)s - %(message)s")
    readers = get_streams(cfg)
    offline_readers = [reader for reader in readers if not reader.isReady()]
    readers = [reader for reader in readers if reader.isReady()]
    close_connection(offline_readers)
    if len(readers) == 0:
        raise ConnectionError("Could not connect to any channel.")
    collection_loop(readers)
    