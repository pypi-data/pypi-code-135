import enum
from typing import Annotated, Any, Dict, Literal, Union

from pydantic import Field, root_validator
from pydantic.main import BaseModel


@enum.unique
class TrackType(str, enum.Enum):
    GENERAL = "General"
    VIDEO = "Video"
    AUDIO = "Audio"
    TEXT = "Text"
    MENU = "Menu"


class GeneralData(BaseModel):
    type: Literal[TrackType.GENERAL] = Field(
        alias="@type", default=TrackType.GENERAL, const=True
    )
    unique_id: str = Field(alias="UniqueID")


class AudioData(BaseModel):
    type: Literal[TrackType.AUDIO] = Field(
        alias="@type", default=TrackType.AUDIO, const=True
    )
    id: int = Field(alias="ID")
    unique_id: str = Field(alias="UniqueID")
    codec_id: str = Field(alias="CodecID")


class VideoData(BaseModel):
    class HDR(BaseModel):
        format: str = Field(alias="HDR_Format")
        version: str = Field(alias="HDR_Format_Version")
        profile: str = Field(alias="HDR_Format_Profile")
        level: str = Field(alias="HDR_Format_Level")
        settings: str = Field(alias="HDR_Format_Settings")
        compatibility: str = Field(alias="HDR_Format_Compatibility")

        @property
        def is_dolby_vision(self) -> bool:
            return "Dolby Vision" in self.format

    type: Literal[TrackType.VIDEO] = Field(
        alias="@type", default=TrackType.VIDEO, const=True
    )
    id: int = Field(alias="ID")
    unique_id: str = Field(alias="UniqueID")
    codec_id: str = Field(alias="CodecID")
    hdr: HDR

    # noinspection PyMethodParameters
    @root_validator(pre=True)
    def extract_hdr_info(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        values["hdr"] = cls.HDR.parse_obj(values)
        return values


class TextData(BaseModel):
    type: Literal[TrackType.TEXT] = Field(
        alias="@type", default=TrackType.TEXT, const=True
    )
    id: int = Field(alias="ID")
    unique_id: str = Field(alias="UniqueID")
    codec_id: str = Field(alias="CodecID")


class MenuData(BaseModel):
    type: Literal[TrackType.MENU] = Field(
        alias="@type", default=TrackType.MENU, const=True
    )


TrackData = Annotated[
    Union[GeneralData, AudioData, VideoData, TextData, MenuData],
    Field(discriminator="type"),
]
