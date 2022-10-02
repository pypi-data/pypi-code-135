from typing import List

from pydantic import Field
from pydantic.main import BaseModel

from dovi_helpers.models.data import TrackData


class LibraryMeta(BaseModel):
    version: str


class Media(BaseModel):
    ref: str = Field(alias="@ref")
    tracks: List[TrackData] = Field(alias="track")


class MediaInfoData(BaseModel):
    meta: LibraryMeta = Field(alias="creatingLibrary")
    media: Media
