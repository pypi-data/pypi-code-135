from dataclasses import dataclass
from typing import Optional, Union

from pydantic import BaseModel

from ns.errors import Error


@dataclass
class Request:
    service_name: str
    method_name: str
    args: Union[list, dict]


@dataclass
class Result:
    ok: bool
    data: Optional[any] = None
    error: Optional[Error] = None
