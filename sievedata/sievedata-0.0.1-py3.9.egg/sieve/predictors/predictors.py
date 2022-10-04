from ..types.frame import FrameObject, FrameSingleObject, FrameObjectSlice
from ..types.misc import  UserMetadata, SieveBaseModel
from ..types.object import Object, ObjectSlice, SingleObject, StaticObject
from cog.predictor import BasePredictor
from typing import Dict, List

# Added in Python 3.8. Can be from typing if we drop support for <3.8.

class SievePredictor(BasePredictor):
    """
    A SievePredictor is a predictor that can be used with the Sieve framework
    """
    ALLOWED_INPUT_TYPES = []
    ALLOWED_OUTPUT_TYPES = []

class TemporalProcessor(SievePredictor):
    """
    A temporal processor is a predictor that processes a objects with a temporal component over the last n frames
    """
    ALLOWED_INPUT_TYPES = [
        FrameObjectSlice,
        UserMetadata, 
        List[ObjectSlice],
        List[SingleObject],
        FrameSingleObject
    ]

    ALLOWED_OUTPUT_TYPES = [
        List[SingleObject],
        SingleObject
    ]

class ObjectProcessor(SievePredictor):
    """
    An object processor is a predictor that processes a single object
    """
    ALLOWED_INPUT_TYPES = [
        FrameObject,
        Object,
        UserMetadata
    ]

    ALLOWED_OUTPUT_TYPES = [
        Object,
        StaticObject,
        ObjectSlice,
        SingleObject,
    ]

class LinearProcessor(SievePredictor):
    ALLOWED_INPUT_TYPES = [
        FrameObjectSlice,
        UserMetadata, 
        List[ObjectSlice],
        List[SingleObject],
        FrameSingleObject
    ]

    ALLOWED_OUTPUT_TYPES = [
        List[SingleObject],
        SingleObject
    ]

