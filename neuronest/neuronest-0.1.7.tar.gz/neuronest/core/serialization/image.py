import numpy as np
from cv2 import cv2 as cv


def to_binary(frame: np.ndarray, extension: str = ".jpg") -> bytes:
    return cv.imencode(extension, frame)[1].tobytes()


def from_binary(binary_image: bytes) -> np.ndarray:
    cv.imdecode(np.frombuffer(binary_image, np.uint8), cv.IMREAD_UNCHANGED)
