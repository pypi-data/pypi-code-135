from PIL.Image import Image

from shop.entities import ProductDTO
from shop.models import Product


class ProductsService:
    def get_products(self) -> list[Product]:
        """
        Returns products list
        :return:
        """

    def upload_image(self, product_id: int, image: Image):
        ...

    def get_image(self, product_id: int = 5) -> Image:
        ...

    def test(self, d: dict, l: list[float]) -> Image:
        ...

    def update_product(self, product: list[ProductDTO]) -> Image:
        ...
