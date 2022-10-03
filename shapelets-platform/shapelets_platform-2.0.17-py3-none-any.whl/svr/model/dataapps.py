from pydantic import  BaseModel, EmailStr
from typing import Optional, Set, Union
from typing_extensions import Literal

DataAppField = Literal['id', 'name', 'version', 'description', 'creationDate', 'spec']
DataAppAllFields: Set[DataAppField] = set(['id', 'name', 'version', 'description', 'creationDate', 'spec'])
DataAppId = Union[int, str]


class DataAppAttributes(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    creationDate: Optional[str] = None
    spec: Optional[str] = None


class DataAppProfile(DataAppAttributes):
    id: str
