from typing import Optional

from pydantic import BaseModel


class KekDTO(BaseModel):
    name: str = '123'
    lol: Optional[float]
    kek: bool


class ProductDTO(KekDTO):
    description: str
    price: float
    products: list[list[dict[str, KekDTO]]]
