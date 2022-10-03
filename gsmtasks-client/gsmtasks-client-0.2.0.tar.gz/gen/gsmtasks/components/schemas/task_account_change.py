from __future__ import annotations

import typing
import lapidary_base
import pydantic


class TaskAccountChange(pydantic.BaseModel):
    account: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


TaskAccountChange.update_forward_refs()
