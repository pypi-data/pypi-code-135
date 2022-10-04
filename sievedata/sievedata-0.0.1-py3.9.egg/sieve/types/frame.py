import numpy as np
# import time
from typing import List
import json
from pydantic import validator, Extra, ValidationError
import cv2
from .object import TemporalObject, StaticObject, Object, SingleObject, ObjectSlice
from .base import SieveBaseModel

class FrameTemporalObject(TemporalObject, arbitrary_types_allowed=True):
    """
    A frame temporal object is a temporal object that contains image data
    """
    frame_number: int 
    data: bytes
    format: str = ".png"

    def get_array(self):
        """
        Returns the stored image as a numpy array
        """
        return cv2.imdecode(np.frombuffer(self.data, np.uint8), cv2.IMREAD_UNCHANGED)

    @validator('data')
    def check_valid(cls, v):
        """
        Checks if the data is a valid bytearray
        """
        if type(v) != bytes:
            raise ValidationError("must be bytes")
        return v

class FrameStaticObject(StaticObject, extra=Extra.allow):
    """
    A frame static object is a special static data containing static attributes of the frame like fps, width, height, etc.
    """
    cls: str = "frame"
    fps: float
    object_id: str
    width: int
    height: int
    source_url: str = None
    source_type: str = None

    @validator('cls', allow_reuse=True)
    def check_valid(cls, v):
        """
        Makes sure the class is frame
        """
        if v != "frame":
            raise ValidationError("must be 'frame'")
        return v

    @validator('fps')
    def check_valid(cls, v):
        """
        Checks if the fps is a valid float
        """
        if type(v) != float:
            raise ValidationError("must be float")
        return v

class FrameObject(Object, FrameStaticObject, extra=Extra.allow):
    """
    A frame object is a special object that contains all the information about a frame
    """
    temporal_objects: List[FrameTemporalObject]

class FrameObjectSlice(FrameObject, ObjectSlice, extra=Extra.allow):
    """
    A frame object slice is a special single object that contains all the information about a frame + a single temporal object
    """
    pass

    
class FrameSingleObject(FrameObjectSlice, SingleObject, extra=Extra.allow):
    """
    A frame single object is a special single object that contains all the information about a frame + a single temporal object
    """
    temporal_object: FrameTemporalObject
    pass

# For future use
class OutputImage(SieveBaseModel, arbitrary_types_allowed=True):
    """
    The output image is a specific field that allows users to return images from their algorithms
    """
    frame_number: int
    data: bytes
    format: str = ".png"

    def from_array(array: np.ndarray, frame_number: int):
        """
        Creates an output image from a numpy array
        """
        # Check grayscale
        if len(array.shape) == 2:
            format = ".png"
            data = cv2.imencode(format, array)[1].tobytes()
            frame_number = frame_number
            return OutputImage(frame_number=frame_number, data=data, format=format)
        # Check RGB/home/abhinav_ayalur_gmail_com/cli/sieve
        if len(array.shape) != 3:
            raise ValueError("array must have shape (height, width, channels)")
        if array.shape[2] != 3:
            raise ValueError("array must have shape (height, width, 3)")
        return OutputImage(frame_number=frame_number, data=cv2.imencode(format, array)[1].tobytes(), format=format)

    def get_array(self):
        """
        Returns the stored image as a numpy array
        """
        return cv2.imdecode(np.frombuffer(self.data, np.uint8), cv2.IMREAD_UNCHANGED)

    def get_frame(self):
        return self.get_array()
