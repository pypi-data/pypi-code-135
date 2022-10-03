from __future__ import annotations

import typing
import lapidary_base
import pydantic


class PasswordReset(pydantic.BaseModel):
    email: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


PasswordReset.update_forward_refs()
