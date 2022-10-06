from typing import Union, Any
from PIL import Image
from io import BytesIO


class Tile:
    id: str
    image_url: str
    index: int
    challenge: Any
    data: Union[bytes, "Image"]
    custom_id: str

    def __init__(self, _id, image_url, index=None, challenge=None):
        self.id = _id
        self.image_url = image_url
        self.index = index
        self.challenge = challenge

    def get_image(self, raw: bool = False) -> Union[Image.Image, bytes]:
        if raw:
            return self.data
        image = Image.open(BytesIO(self.data))
        return image
