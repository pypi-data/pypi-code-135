import datetime
import logging
import os
from pathlib import Path
import threading
import time

import cv2 

from h2cow.utils import configure

class StreamReader:
    def __init__(self, channel: int, rtsp_url: str, save_path: str):
        self.Channel = channel
        self.__save_path = save_path
        self.__stream = self.__open_stream(rtsp_url)
        self.__ready = False
        self.__status = False
        self.__frame = None
        self.__online = True
        if not self.__stream is None:
            self.__thread = threading.Thread(target=self.__update)
            self.__thread.start()
        waited = 0
        while not self.__ready and waited < 10:
            waited += 0.1
            time.sleep(0.1)

    def exit(self):
        self.__online = False
        self.__thread.join()
        logging.info(f"Closed stream on channel {self.Channel}.")

    def get_frame(self):
        path = Path(
            self.__save_path, 
            f"channel_{self.Channel}", 
            f"{datetime.datetime.now().strftime('%Y%m%d')}", 
            f"{datetime.datetime.now().strftime('%H')}"
            )
        if not os.path.isdir(path):
            os.makedirs(path)
        cv2.imwrite(
            str(
                Path(
                    path, 
                    f"{datetime.datetime.now().strftime('%M%S')}.jpeg"
                    )
                ),
            self.__frame
            )

    def isReady(self):
        return self.__status

    def __open_stream(self, rtsp_url: str):
        logging.debug(f"Starting to open stream on channel {self.Channel}")
        cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        if not cap.isOpened():
            logging.error(f"Unable to open stream on channel {self.Channel}.")
            return None
        logging.info(f"Opened stream on channel {self.Channel}.")
        return cap

    def __update(self):
        while self.__online:
            if self.__stream.isOpened():
                self.__status, self.__frame = self.__stream.read()
                if self.__status and not self.__ready:
                    self.__ready = True
                    logging.info(f"Stream on channel {self.Channel} ready.")