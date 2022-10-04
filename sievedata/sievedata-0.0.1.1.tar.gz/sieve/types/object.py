from typing import Optional, List, Dict
from .base import SieveBaseModel
from .misc import Point, BoundingBox
from pydantic import ValidationError, validator, Extra
import uuid

class TemporalObject(SieveBaseModel, extra=Extra.allow):
    """
    A temporal object contains all temporal/state information about an object that may change over time.
    This includes, at minimum, the object's bounding box and its velocity
    """
    bounding_box: BoundingBox
    velocity: Point = Point(x=0, y=0)
    frame_number: int
    def center(self) -> Point:
        return Point(x=(self.bounding_box.x1 + self.bounding_box.x2) / 2, y=(self.bounding_box.y1 + self.bounding_box.y2) / 2)

class StaticObject(SieveBaseModel, extra=Extra.allow):
    """
    A static object contains all static information about an object that does not change over time.
    This includes, at minimum, the object's class and its attributes
    """
    object_id: str
    cls: str
    start_frame: int 
    end_frame: int
    skip_frames: int = 1
    def __init__(self, **data) -> None:
        if "end_frame" not in data and "start_frame" in data:
            data["end_frame"] = data["start_frame"]
        elif "end_frame" not in data and "start_frame" not in data and "frame_number" in data:
            data["start_frame"] = data["frame_number"]
            data["end_frame"] = data["frame_number"]
        if "object_id" not in data:
            data["object_id"] = str(uuid.uuid4())
        if data["end_frame"] < data["start_frame"]:
            raise ValidationError("End frame must be greater than start frame")
        if "object_id" not in data:
            data["object_id"] = str(uuid.uuid4())
        if "class" in data:
            data["cls"] = data["class"]
            del data["class"]
        super().__init__(**data)

    @validator('start_frame', 'end_frame')
    def check_valid(cls, v):
        """
        Check that the start and end frames are valid
        """
        if type(v) != int:
            raise ValidationError("must be int")
        return v

class Object(StaticObject, extra=Extra.allow):
    """
    Am object contains all information about an object that is tracked over time.
    This includes, at minimum, the object's bounding box and its velocity.
    It also contains all static information about the object, such as its class and object id
    """
    temporal_objects: List[TemporalObject]

    # init with kwargs
    def __init__(self, **data):
        super().__init__(**data)
        if self.temporal_objects is None:
            self.temporal_objects = []
            data["end_frame"] = data["start_frame"]
    
    @classmethod
    def from_temporal_object(cls, temporal_object: TemporalObject, **data):
        """
        Create a new object from a temporal object with just 1 frame
        """
        if "object_id" not in data:
            data["object_id"] = str(uuid.uuid4())
        return cls(object_id=temporal_object.object_id, cls=temporal_object.cls, start_frame=TemporalObject.frame_number, end_frame=TemporalObject.frame_number, skip_frames=1, temporal_objects=[temporal_object], **data)
    
    def get_temporal_object(self, frame_number: int) -> TemporalObject:
        """
        Get the temporal object at a specific frame number
        """
        if frame_number < self.start_frame or frame_number > self.end_frame:
            return None
        return self.temporal_objects[(frame_number - self.start_frame) // self.skip_frames]

    def append_temporal_object(self, temporal_object: TemporalObject):
        #Create a new tracked temporal object
        if len(self.temporal_objects) == 0:
            self.temporal_objects = [TemporalObject(object_id=self.object_id, frame_number=self.start_frame, cls=temporal_object.cls, bounding_box=temporal_object.bounding_box, velocity=Point(x=0, y=0))]
        else:
            last_temporal_object = self.temporal_objects[-1]
            new_velocity = Point(x=temporal_object.center().x - last_temporal_object.center().x, y=temporal_object.center().y - last_temporal_object.center().y)
            tracked_temporal_object = TemporalObject(object_id=self.object_id, frame_number=self.end_frame+self.skip_frames, cls=temporal_object.cls, bounding_box=temporal_object.bounding_box, velocity=new_velocity)
            self.temporal_objects.append(tracked_temporal_object)
            self.end_frame += self.skip_frames

    def set_temporal_object(self, temporal_object: TemporalObject, interpolate: bool = False):
        """
        Set the temporal object at a specific frame number
        
        If interpolate is True, then the object's BoundingBox will be interpolated between the previous and next frame
        """
        if temporal_object.frame_number < self.start_frame or temporal_object.frame_number > self.end_frame:
            if temporal_object.frame_number > self.end_frame and interpolate:
                #Set all linearly interpolated temporal objects between the last frame and the new temporal object
                last_bounding_box = self.temporal_objects[-1].bounding_box
                new_bounding_box = temporal_object.bounding_box
                new_velocity = Point(x=temporal_object.center().x - self.temporal_objects[-1].center().x, y=temporal_object.center().y - self.temporal_objects[-1].center().y)
                for i in range(self.end_frame + self.skip_frames, temporal_object.frame_number + self.skip_frames, self.skip_frames):
                    interpolated_bounding_box = BoundingBox(
                        x1=last_bounding_box.x1 + (new_bounding_box.x1 - last_bounding_box.x1) * (i - self.end_frame) / (temporal_object.frame_number - self.end_frame), 
                        y1=last_bounding_box.y1 + (new_bounding_box.y1 - last_bounding_box.y1) * (i - self.end_frame) / (temporal_object.frame_number - self.end_frame), 
                        x2=last_bounding_box.x2 + (new_bounding_box.x2 - last_bounding_box.x2) * (i - self.end_frame) / (temporal_object.frame_number - self.end_frame), 
                        y2=last_bounding_box.y2 + (new_bounding_box.y2 - last_bounding_box.y2) * (i - self.end_frame) / (temporal_object.frame_number - self.end_frame)
                    )
                    new_temporal_object = TemporalObject(frame_number=i, bounding_box=interpolated_bounding_box, velocity=new_velocity)
                    self.temporal_objects.append(new_temporal_object)
                    self.end_frame += self.skip_frames
            elif temporal_object.frame_number < self.start_frame and interpolate:
                #Set all linearly interpolated temporal objects between the first frame and the new temporal object
                first_bounding_box = self.temporal_objects[0].bounding_box
                new_bounding_box = temporal_object.bounding_box
                new_velocity = Point(x = self.temporal_objects[0].center().x - temporal_object.center().x, y = self.temporal_objects[0].center().y - temporal_object.center().y)
                self.temporal_objects[0].velocity = new_velocity
                for i in range(self.start_frame - self.skip_frames, temporal_object.frame_number - self.skip_frames, -self.skip_frames):
                    interpolated_bounding_box = BoundingBox(
                        x1=first_bounding_box.x1 + (new_bounding_box.x1 - first_bounding_box.x1) * (i - self.start_frame) / (temporal_object.frame_number - self.start_frame), 
                        y1=first_bounding_box.y1 + (new_bounding_box.y1 - first_bounding_box.y1) * (i - self.start_frame) / (temporal_object.frame_number - self.start_frame), 
                        x2=first_bounding_box.x2 + (new_bounding_box.x2 - first_bounding_box.x2) * (i - self.start_frame) / (temporal_object.frame_number - self.start_frame), 
                        y2=first_bounding_box.y2 + (new_bounding_box.y2 - first_bounding_box.y2) * (i - self.start_frame) / (temporal_object.frame_number - self.start_frame)
                    )
                    if i == temporal_object.frame_number - self.skip_frames:
                        new_velocity = 0
                    new_temporal_object = TemporalObject(frame_number=i, bounding_box=interpolated_bounding_box, velocity=new_velocity)
                    self.temporal_objects.insert(0, new_temporal_object)
                    self.start_frame -= self.skip_frames
            return
        self.temporal_objects[(temporal_object.frame_number - self.start_frame) // self.skip_frames] = temporal_object
    
    def slice(self, start_frame: int = None, end_frame: int = None, frame_number: int = None):
        """
        Slice the temporal object to only include the frames between start_frame and end_frame
        """
        if frame_number is not None:
            if frame_number < self.start_frame or frame_number > self.end_frame:
                return None
            return SingleObject(object_id=self.object_id, start_frame=frame_number, end_frame=frame_number, skip_frames=self.skip_frames, temporal_object=self.temporal_objects[(frame_number - self.start_frame) // self.skip_frames])
        if start_frame < self.start_frame or end_frame > self.end_frame:
            return None
        return ObjectSlice(object_id=self.object_id, start_frame=self.start_frame, slice_start_frame=start_frame, slice_end_frame=end_frame, end_frame=self.end_frame, skip_frames=self.skip_frames, temporal_objects=self.temporal_objects[(start_frame - self.start_frame) // self.skip_frames:(end_frame - self.start_frame) // self.skip_frames + 1])

class ObjectSlice(Object, extra = Extra.allow):
    """
    This is an object that contains the static info of an object and the temporal info of a slice of the object's temporal object
    """
    slice_start_frame: int
    slice_end_frame: int

    def __init__(self, **data):
        if 'slice_start_frame' not in data and 'start_frame' in data:
            data['slice_start_frame'] = data['start_frame']
        if 'slice_end_frame' not in data and 'end_frame' in data:
            data['slice_end_frame'] = data['end_frame']
        if 'slice_start_frame' not in data and 'slice_end_frame' not in data and 'frame_number' in data:
            data['slice_start_frame'] = data['frame_number']
            data['slice_end_frame'] = data['frame_number']
        if "temporal_object" in data:
            temporal_object = data.pop("temporal_object")
            data["temporal_objects"] = [temporal_object]
        super().__init__(**data)
        self.temporal_object = self.temporal_objects[0]

    def get_temporal_object(self, frame_number: int) -> TemporalObject:
        """
        Get the temporal object at a specific frame number
        """
        if frame_number < self.slice_start_frame or frame_number > self.slice_end_frame:
            return None
        return self.temporal_objects[(frame_number - self.slice_start_frame) // self.skip_frames]

    @validator('temporal_objects')
    def check_valid(cls, v):
        """
        Check that the temporal objects are valid
        """
        if len(v) != 1:
            raise ValidationError("must be a single temporal object")
        return v

class SingleObject(ObjectSlice, extra = Extra.allow):
    """
    This is an object that only contains a single temporal instance
    """
    @validator('temporal_objects')
    def check_valid(cls, v):
        """
        Check that the temporal objects are valid
        """
        if len(v) != 1:
            raise ValidationError("must be a single temporal object")
        return v

    def __init__(self, **data):
        if "temporal_object" in data:
            temporal_object = data.pop("temporal_object")
            data["temporal_objects"] = [temporal_object]
        if "frame_number" not in data and "start_frame" not in data and "end_frame" not in data:
            data["frame_number"] = data["temporal_objects"][0].frame_number
            data["start_frame"] = data["temporal_objects"][0].frame_number
            data["end_frame"] = data["temporal_objects"][0].frame_number
        super().__init__(**data)
        self.temporal_object = self.temporal_objects[0]
