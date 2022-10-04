from pydantic import BaseModel
import json 

class SieveBaseModel(BaseModel):
    def to_dict(self):
        """
        Converts the object to a dictionary
        """
        return self.dict()
    
    def to_json(self):
        """
        Converts the object to a JSON string
        """
        return json.dumps(self.to_dict())
    
    def to_json_pretty(self):
        """
        Converts the object to a pretty JSON string
        """
        return json.dumps(self.to_dict(), indent=4)

    def from_dict(self, d):
        """
        Unpacks a dictionary into the object
        """
        return self.parse_obj(d)
    
    def from_json(self, j):
        """
        Unpacks a JSON string into the object
        """
        return self.parse_raw(j)

    def update(self, other_object):
        """
        Recusively update attrs of self with attrs of other_object
        """
        for attr, value in other_object.__dict__.items():
            if isinstance(value, SieveBaseModel):
                self.update(value)
            else:
                setattr(self, attr, value)
