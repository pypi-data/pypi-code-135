from pathlib import Path
from pydantic import BaseModel
from typing import List, Any


class HandlerConfig(BaseModel):
    pass

class DeadMansConfig(HandlerConfig):
    pass