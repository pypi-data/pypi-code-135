from __future__ import annotations

import typing
import lapidary_base
import pydantic


class RenderRequest(pydantic.BaseModel):
    task: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


RenderRequest.update_forward_refs()
