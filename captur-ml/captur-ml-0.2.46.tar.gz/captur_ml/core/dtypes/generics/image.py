from typing import Optional
from pydantic import AnyUrl, root_validator
from pydantic.dataclasses import dataclass as pd_dataclass

from captur_ml.utils.image import load_image_bytes_from_url


__pdoc__ = {"Image.must_contain_url_or_data": False}


@pd_dataclass
class Image:
    #: A unique identifier of the image
    id: str = ""
    #: The image bytes encoded as a UTF-8 string. Required if `url` is not specified.
    data: str = ""
    #: An http[s]:// or gs:// URL pointing to the image resource. Required if `data` is not specified.
    url: Optional[AnyUrl] = None

    @root_validator
    def must_contain_url_or_data(cls, values):
        if not values.get("url") and not values.get("data"):
            raise ValueError("Either `url` or `data` must be specified.")
        return values

    @property
    def bytes(self):
        """The raw image bytes. Will make a network request if only `url` is specified and data has not been loaded yet."""
        if self.data:
            return self.data
        self.data = load_image_bytes_from_url(self.url)
        return self.data
